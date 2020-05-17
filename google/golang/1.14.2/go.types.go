// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package types declares the data types and implements
// the algorithms for type-checking of Go packages. Use
// Config.Check to invoke the type checker for a package.
// Alternatively, create a new type checker with NewChecker
// and invoke it incrementally by calling Checker.Files.
//
// Type-checking consists of several interdependent phases:
//
// Name resolution maps each identifier (ast.Ident) in the program to the
// language object (Object) it denotes.
// Use Info.{Defs,Uses,Implicits} for the results of name resolution.
//
// Constant folding computes the exact constant value (constant.Value)
// for every expression (ast.Expr) that is a compile-time constant.
// Use Info.Types[expr].Value for the results of constant folding.
//
// Type inference computes the type (Type) of every expression (ast.Expr)
// and checks for compliance with the language specification.
// Use Info.Types[expr].Type for the results of type inference.
//
// For a tutorial, see https://golang.org/s/types-tutorial.
//
package types

import (
	"bytes"
	"fmt"
	"go/ast"
	"go/constant"
	"go/token"
)

// An Error describes a type-checking error; it implements the error interface.
// A "soft" error is an error that still permits a valid interpretation of a
// package (such as "unused variable"); "hard" errors may lead to unpredictable
// behavior if ignored.
type Error struct {
	Fset *token.FileSet // file set for interpretation of Pos
	Pos  token.Pos      // error position
	Msg  string         // error message
	Soft bool           // if set, error is "soft"
}

// Error returns an error string formatted as follows:
// filename:line:column: message
func (err Error) Error() string {}

// An Importer resolves import paths to Packages.
//
// CAUTION: This interface does not support the import of locally
// vendored packages. See https://golang.org/s/go15vendor.
// If possible, external implementations should implement ImporterFrom.
type Importer interface {
	// Import returns the imported package for the given import path.
	// The semantics is like for ImporterFrom.ImportFrom except that
	// dir and mode are ignored (since they are not present).
	Import(path string) (*Package, error)
}

// ImportMode is reserved for future use.
type ImportMode int

// An ImporterFrom resolves import paths to packages; it
// supports vendoring per https://golang.org/s/go15vendor.
// Use go/importer to obtain an ImporterFrom implementation.
type ImporterFrom interface {
	// Importer is present for backward-compatibility. Calling
	// Import(path) is the same as calling ImportFrom(path, "", 0);
	// i.e., locally vendored packages may not be found.
	// The types package does not call Import if an ImporterFrom
	// is present.
	Importer

	// ImportFrom returns the imported package for the given import
	// path when imported by a package file located in dir.
	// If the import failed, besides returning an error, ImportFrom
	// is encouraged to cache and return a package anyway, if one
	// was created. This will reduce package inconsistencies and
	// follow-on type checker errors due to the missing package.
	// The mode value must be 0; it is reserved for future use.
	// Two calls to ImportFrom with the same path and dir must
	// return the same package.
	ImportFrom(path, dir string, mode ImportMode) (*Package, error)
}

// A Config specifies the configuration for type checking.
// The zero value for Config is a ready-to-use default configuration.
type Config struct {
	// If IgnoreFuncBodies is set, function bodies are not
	// type-checked.
	IgnoreFuncBodies bool

	// If FakeImportC is set, `import "C"` (for packages requiring Cgo)
	// declares an empty "C" package and errors are omitted for qualified
	// identifiers referring to package C (which won't find an object).
	// This feature is intended for the standard library cmd/api tool.
	//
	// Caution: Effects may be unpredictable due to follow-on errors.
	//          Do not use casually!
	FakeImportC bool

	// If Error != nil, it is called with each error found
	// during type checking; err has dynamic type Error.
	// Secondary errors (for instance, to enumerate all types
	// involved in an invalid recursive type declaration) have
	// error strings that start with a '\t' character.
	// If Error == nil, type-checking stops with the first
	// error found.
	Error func(err error)

	// An importer is used to import packages referred to from
	// import declarations.
	// If the installed importer implements ImporterFrom, the type
	// checker calls ImportFrom instead of Import.
	// The type checker reports an error if an importer is needed
	// but none was installed.
	Importer Importer

	// If Sizes != nil, it provides the sizing functions for package unsafe.
	// Otherwise SizesFor("gc", "amd64") is used instead.
	Sizes Sizes

	// If DisableUnusedImportCheck is set, packages are not checked
	// for unused imports.
	DisableUnusedImportCheck bool
}

// Info holds result type information for a type-checked package.
// Only the information for which a map is provided is collected.
// If the package has type errors, the collected information may
// be incomplete.
type Info struct {
	// Types maps expressions to their types, and for constant
	// expressions, also their values. Invalid expressions are
	// omitted.
	//
	// For (possibly parenthesized) identifiers denoting built-in
	// functions, the recorded signatures are call-site specific:
	// if the call result is not a constant, the recorded type is
	// an argument-specific signature. Otherwise, the recorded type
	// is invalid.
	//
	// The Types map does not record the type of every identifier,
	// only those that appear where an arbitrary expression is
	// permitted. For instance, the identifier f in a selector
	// expression x.f is found only in the Selections map, the
	// identifier z in a variable declaration 'var z int' is found
	// only in the Defs map, and identifiers denoting packages in
	// qualified identifiers are collected in the Uses map.
	Types map[ast.Expr]TypeAndValue

	// Defs maps identifiers to the objects they define (including
	// package names, dots "." of dot-imports, and blank "_" identifiers).
	// For identifiers that do not denote objects (e.g., the package name
	// in package clauses, or symbolic variables t in t := x.(type) of
	// type switch headers), the corresponding objects are nil.
	//
	// For an embedded field, Defs returns the field *Var it defines.
	//
	// Invariant: Defs[id] == nil || Defs[id].Pos() == id.Pos()
	Defs map[*ast.Ident]Object

	// Uses maps identifiers to the objects they denote.
	//
	// For an embedded field, Uses returns the *TypeName it denotes.
	//
	// Invariant: Uses[id].Pos() != id.Pos()
	Uses map[*ast.Ident]Object

	// Implicits maps nodes to their implicitly declared objects, if any.
	// The following node and object types may appear:
	//
	//     node               declared object
	//
	//     *ast.ImportSpec    *PkgName for imports without renames
	//     *ast.CaseClause    type-specific *Var for each type switch case clause (incl. default)
	//     *ast.Field         anonymous parameter *Var (incl. unnamed results)
	//
	Implicits map[ast.Node]Object

	// Selections maps selector expressions (excluding qualified identifiers)
	// to their corresponding selections.
	Selections map[*ast.SelectorExpr]*Selection

	// Scopes maps ast.Nodes to the scopes they define. Package scopes are not
	// associated with a specific node but with all files belonging to a package.
	// Thus, the package scope can be found in the type-checked Package object.
	// Scopes nest, with the Universe scope being the outermost scope, enclosing
	// the package scope, which contains (one or more) files scopes, which enclose
	// function scopes which in turn enclose statement and function literal scopes.
	// Note that even though package-level functions are declared in the package
	// scope, the function scopes are embedded in the file scope of the file
	// containing the function declaration.
	//
	// The following node types may appear in Scopes:
	//
	//     *ast.File
	//     *ast.FuncType
	//     *ast.BlockStmt
	//     *ast.IfStmt
	//     *ast.SwitchStmt
	//     *ast.TypeSwitchStmt
	//     *ast.CaseClause
	//     *ast.CommClause
	//     *ast.ForStmt
	//     *ast.RangeStmt
	//
	Scopes map[ast.Node]*Scope

	// InitOrder is the list of package-level initializers in the order in which
	// they must be executed. Initializers referring to variables related by an
	// initialization dependency appear in topological order, the others appear
	// in source order. Variables without an initialization expression do not
	// appear in this list.
	InitOrder []*Initializer
}
/*
package main

import (
	"bytes"
	"fmt"
	"go/ast"
	"go/format"
	"go/parser"
	"go/token"
	"go/types"
	"log"
	"sort"
	"strings"
)

func main() {
	// Parse a single source file.
	const input = `
package fib

type S string

var a, b, c = len(b), S(c), "hello"

func fib(x int) int {
	if x < 2 {
		return x
	}
	return fib(x-1) - fib(x-2)
}`
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, "fib.go", input, 0)
	if err != nil {
		log.Fatal(err)
	}

	// Type-check the package.
	// We create an empty map for each kind of input
	// we're interested in, and Check populates them.
	info := types.Info{
		Types: make(map[ast.Expr]types.TypeAndValue),
		Defs:  make(map[*ast.Ident]types.Object),
		Uses:  make(map[*ast.Ident]types.Object),
	}
	var conf types.Config
	pkg, err := conf.Check("fib", fset, []*ast.File{f}, &info)
	if err != nil {
		log.Fatal(err)
	}

	// Print package-level variables in initialization order.
	fmt.Printf("InitOrder: %v\n\n", info.InitOrder)

	// For each named object, print the line and
	// column of its definition and each of its uses.
	fmt.Println("Defs and Uses of each named object:")
	usesByObj := make(map[types.Object][]string)
	for id, obj := range info.Uses {
		posn := fset.Position(id.Pos())
		lineCol := fmt.Sprintf("%d:%d", posn.Line, posn.Column)
		usesByObj[obj] = append(usesByObj[obj], lineCol)
	}
	var items []string
	for obj, uses := range usesByObj {
		sort.Strings(uses)
		item := fmt.Sprintf("%s:\n  defined at %s\n  used at %s",
			types.ObjectString(obj, types.RelativeTo(pkg)),
			fset.Position(obj.Pos()),
			strings.Join(uses, ", "))
		items = append(items, item)
	}
	sort.Strings(items) // sort by line:col, in effect
	fmt.Println(strings.Join(items, "\n"))
	fmt.Println()

	fmt.Println("Types and Values of each expression:")
	items = nil
	for expr, tv := range info.Types {
		var buf bytes.Buffer
		posn := fset.Position(expr.Pos())
		tvstr := tv.Type.String()
		if tv.Value != nil {
			tvstr += " = " + tv.Value.String()
		}
		// line:col | expr | mode : type = value
		fmt.Fprintf(&buf, "%2d:%2d | %-19s | %-7s : %s",
			posn.Line, posn.Column, exprString(fset, expr),
			mode(tv), tvstr)
		items = append(items, buf.String())
	}
	sort.Strings(items)
	fmt.Println(strings.Join(items, "\n"))

}

func mode(tv types.TypeAndValue) string {
	switch {
	case tv.IsVoid():
		return "void"
	case tv.IsType():
		return "type"
	case tv.IsBuiltin():
		return "builtin"
	case tv.IsNil():
		return "nil"
	case tv.Assignable():
		if tv.Addressable() {
			return "var"
		}
		return "mapindex"
	case tv.IsValue():
		return "value"
	default:
		return "unknown"
	}
}

func exprString(fset *token.FileSet, expr ast.Expr) string {
	var buf bytes.Buffer
	format.Node(&buf, fset, expr)
	return buf.String()
}
*/

// TypeOf returns the type of expression e, or nil if not found.
// Precondition: the Types, Uses and Defs maps are populated.
//
func (info *Info) TypeOf(e ast.Expr) Type {}

// ObjectOf returns the object denoted by the specified id,
// or nil if not found.
//
// If id is an embedded struct field, ObjectOf returns the field (*Var)
// it defines, not the type (*TypeName) it uses.
//
// Precondition: the Uses and Defs maps are populated.
//
func (info *Info) ObjectOf(id *ast.Ident) Object {}

// TypeAndValue reports the type and value (for constants)
// of the corresponding expression.
type TypeAndValue struct {
	mode  operandMode
	Type  Type
	Value constant.Value
}

// IsVoid reports whether the corresponding expression
// is a function call without results.
func (tv TypeAndValue) IsVoid() bool {}

// IsType reports whether the corresponding expression specifies a type.
func (tv TypeAndValue) IsType() bool {}

// IsBuiltin reports whether the corresponding expression denotes
// a (possibly parenthesized) built-in function.
func (tv TypeAndValue) IsBuiltin() bool {}

// IsValue reports whether the corresponding expression is a value.
// Builtins are not considered values. Constant values have a non-
// nil Value.
func (tv TypeAndValue) IsValue() bool {}

// IsNil reports whether the corresponding expression denotes the
// predeclared value nil.
func (tv TypeAndValue) IsNil() bool {}

// Addressable reports whether the corresponding expression
// is addressable (https://golang.org/ref/spec#Address_operators).
func (tv TypeAndValue) Addressable() bool {}

// Assignable reports whether the corresponding expression
// is assignable to (provided a value of the right type).
func (tv TypeAndValue) Assignable() bool {}

// HasOk reports whether the corresponding expression may be
// used on the rhs of a comma-ok assignment.
func (tv TypeAndValue) HasOk() bool {}

// An Initializer describes a package-level variable, or a list of variables in case
// of a multi-valued initialization expression, and the corresponding initialization
// expression.
type Initializer struct {
	Lhs []*Var // var Lhs = Rhs
	Rhs ast.Expr
}

func (init *Initializer) String() string {}

// Check type-checks a package and returns the resulting package object and
// the first error if any. Additionally, if info != nil, Check populates each
// of the non-nil maps in the Info struct.
//
// The package is marked as complete if no errors occurred, otherwise it is
// incomplete. See Config.Error for controlling behavior in the presence of
// errors.
//
// The package is specified by a list of *ast.Files and corresponding
// file set, and the package path the package is identified with.
// The clean path must not be empty or dot (".").
func (conf *Config) Check(path string, fset *token.FileSet, files []*ast.File, info *Info) (*Package, error) {}

// AssertableTo reports whether a value of type V can be asserted to have type T.
func AssertableTo(V *Interface, T Type) bool {
}

// AssignableTo reports whether a value of type V is assignable to a variable of type T.
func AssignableTo(V, T Type) bool {}

// ConvertibleTo reports whether a value of type V is convertible to a value of type T.
func ConvertibleTo(V, T Type) bool {}

// Implements reports whether type V implements interface T.
func Implements(V Type, T *Interface) bool {}

// Identical reports whether x and y are identical types.
// Receivers of Signature types are ignored.
func Identical(x, y Type) bool {}

// IdenticalIgnoreTags reports whether x and y are identical types if tags are ignored.
// Receivers of Signature types are ignored.
func IdenticalIgnoreTags(x, y Type) bool {}

// A Checker maintains the state of the type checker.
// It must be created with NewChecker.
type Checker struct {
	// package information
	// (initialized by NewChecker, valid for the life-time of checker)
	conf *Config
	fset *token.FileSet
	pkg  *Package
	*Info
	objMap map[Object]*declInfo       // maps package-level objects and (non-interface) methods to declaration info
	impMap map[importKey]*Package     // maps (import path, source directory) to (complete or fake) package
	posMap map[*Interface][]token.Pos // maps interface types to lists of embedded interface positions
	pkgCnt map[string]int             // counts number of imported packages with a given name (for better error messages)

	// information collected during type-checking of a set of package files
	// (initialized by Files, valid only for the duration of check.Files;
	// maps and lists are allocated on demand)
	files            []*ast.File                       // package files
	unusedDotImports map[*Scope]map[*Package]token.Pos // positions of unused dot-imported packages for each file scope

	firstErr error                 // first error encountered
	methods  map[*TypeName][]*Func // maps package scope type names to associated non-blank (non-interface) methods
	untyped  map[ast.Expr]exprInfo // map of expressions without final type
	delayed  []func()              // stack of delayed action segments; segments are processed in FIFO order
	finals   []func()              // list of final actions; processed at the end of type-checking the current set of files
	objPath  []Object              // path of object dependencies during type inference (for cycle reporting)

	// context within which the current object is type-checked
	// (valid only for the duration of type-checking a specific object)
	context

	// debugging
	indent int // indentation for tracing
}

// NewChecker returns a new Checker instance for a given package.
// Package files may be added incrementally via checker.Files.
func NewChecker(conf *Config, fset *token.FileSet, pkg *Package, info *Info) *Checker {}

// Files checks the provided files as part of the checker's package.
func (check *Checker) Files(files []*ast.File) error {}

// Eval returns the type and, if constant, the value for the
// expression expr, evaluated at position pos of package pkg,
// which must have been derived from type-checking an AST with
// complete position information relative to the provided file
// set.
//
// The meaning of the parameters fset, pkg, and pos is the
// same as in CheckExpr. An error is returned if expr cannot
// be parsed successfully, or the resulting expr AST cannot be
// type-checked.
func Eval(fset *token.FileSet, pkg *Package, pos token.Pos, expr string) (_ TypeAndValue, err error) {}

// CheckExpr type checks the expression expr as if it had appeared at
// position pos of package pkg. Type information about the expression
// is recorded in info.
//
// If pkg == nil, the Universe scope is used and the provided
// position pos is ignored. If pkg != nil, and pos is invalid,
// the package scope is used. Otherwise, pos must belong to the
// package.
//
// An error is returned if pos is not within the package or
// if the node cannot be type-checked.
//
// Note: Eval and CheckExpr should not be used instead of running Check
// to compute types and values, but in addition to Check, as these
// functions ignore the context in which an expression is used (e.g., an
// assignment). Thus, top-level untyped constants will return an
// untyped type rather then the respective context-specific type.
//
func CheckExpr(fset *token.FileSet, pkg *Package, pos token.Pos, expr ast.Expr, info *Info) (err error) {}

// ExprString returns the (possibly shortened) string representation for x.
// Shortened representations are suitable for user interfaces but may not
// necessarily follow Go syntax.
func ExprString(x ast.Expr) string {}

// WriteExpr writes the (possibly shortened) string representation for x to buf.
// Shortened representations are suitable for user interfaces but may not
// necessarily follow Go syntax.
func WriteExpr(buf *bytes.Buffer, x ast.Expr) {}

// LookupFieldOrMethod looks up a field or method with given package and name
// in T and returns the corresponding *Var or *Func, an index sequence, and a
// bool indicating if there were any pointer indirections on the path to the
// field or method. If addressable is set, T is the type of an addressable
// variable (only matters for method lookups).
//
// The last index entry is the field or method index in the (possibly embedded)
// type where the entry was found, either:
//
//	1) the list of declared methods of a named type; or
//	2) the list of all methods (method set) of an interface type; or
//	3) the list of fields of a struct type.
//
// The earlier index entries are the indices of the embedded struct fields
// traversed to get to the found entry, starting at depth 0.
//
// If no entry is found, a nil object is returned. In this case, the returned
// index and indirect values have the following meaning:
//
//	- If index != nil, the index sequence points to an ambiguous entry
//	(the same name appeared more than once at the same embedding level).
//
//	- If indirect is set, a method with a pointer receiver type was found
//      but there was no pointer on the path from the actual receiver type to
//	the method's formal receiver base type, nor was the receiver addressable.
//
func LookupFieldOrMethod(T Type, addressable bool, pkg *Package, name string) (obj Object, index []int, indirect bool) {}

// MissingMethod returns (nil, false) if V implements T, otherwise it
// returns a missing method required by T and whether it is missing or
// just has the wrong type.
//
// For non-interface types V, or if static is set, V implements T if all
// methods of T are present in V. Otherwise (V is an interface and static
// is not set), MissingMethod only checks that methods of T which are also
// present in V have matching types (e.g., for a type assertion x.(T) where
// x is of interface type V).
//
func MissingMethod(V Type, T *Interface, static bool) (method *Func, wrongType bool) {}

// A MethodSet is an ordered set of concrete or abstract (interface) methods;
// a method is a MethodVal selection, and they are ordered by ascending m.Obj().Id().
// The zero value for a MethodSet is a ready-to-use empty method set.
type MethodSet struct {
	list []*Selection
}
/*
package main

import (
	"fmt"
	"go/ast"
	"go/importer"
	"go/parser"
	"go/token"
	"go/types"
	"log"
)

func main() {
	// Parse a single source file.
	const input = `
package temperature
import "fmt"
type Celsius float64
func (c Celsius) String() string  { return fmt.Sprintf("%g°C", c) }
func (c *Celsius) SetF(f float64) { *c = Celsius(f - 32 / 9 * 5) }
`
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, "celsius.go", input, 0)
	if err != nil {
		log.Fatal(err)
	}

	// Type-check a package consisting of this file.
	// Type information for the imported packages
	// comes from $GOROOT/pkg/$GOOS_$GOOARCH/fmt.a.
	conf := types.Config{Importer: importer.Default()}
	pkg, err := conf.Check("temperature", fset, []*ast.File{f}, nil)
	if err != nil {
		log.Fatal(err)
	}

	// Print the method sets of Celsius and *Celsius.
	celsius := pkg.Scope().Lookup("Celsius").Type()
	for _, t := range []types.Type{celsius, types.NewPointer(celsius)} {
		fmt.Printf("Method set of %s:\n", t)
		mset := types.NewMethodSet(t)
		for i := 0; i < mset.Len(); i++ {
			fmt.Println(mset.At(i))
		}
		fmt.Println()
	}

}
*/

func (s *MethodSet) String() string {}

// Len returns the number of methods in s.
func (s *MethodSet) Len() int {}

// At returns the i'th method in s for 0 <= i < s.Len().
func (s *MethodSet) At(i int) *Selection {}

// Lookup returns the method with matching package and name, or nil if not found.
func (s *MethodSet) Lookup(pkg *Package, name string) *Selection {}

// Note: NewMethodSet is intended for external use only as it
//       requires interfaces to be complete. If may be used
//       internally if LookupFieldOrMethod completed the same
//       interfaces beforehand.

// NewMethodSet returns the method set for the given type T.
// It always returns a non-nil method set, even if it is empty.
func NewMethodSet(T Type) *MethodSet {}

// An Object describes a named language entity such as a package,
// constant, type, variable, function (incl. methods), or label.
// All objects implement the Object interface.
//
type Object interface {
	Parent() *Scope // scope in which this object is declared; nil for methods and struct fields
	Pos() token.Pos // position of object identifier in declaration
	Pkg() *Package  // package to which this object belongs; nil for labels and objects in the Universe scope
	Name() string   // package local object name
	Type() Type     // object type
	Exported() bool // reports whether the name starts with a capital letter
	Id() string     // object name if exported, qualified name if not exported (see func Id)

	// String returns a human-readable string of the object.
	String() string

	// order reflects a package-level object's source order: if object
	// a is before object b in the source, then a.order() < b.order().
	// order returns a value > 0 for package-level objects; it returns
	// 0 for all other objects (including objects in file scopes).
	order() uint32

	// color returns the object's color.
	color() color

	// setOrder sets the order number of the object. It must be > 0.
	setOrder(uint32)

	// setColor sets the object's color. It must not be white.
	setColor(color color)

	// setParent sets the parent scope of the object.
	setParent(*Scope)

	// sameId reports whether obj.Id() and Id(pkg, name) are the same.
	sameId(pkg *Package, name string) bool

	// scopePos returns the start position of the scope of this Object
	scopePos() token.Pos

	// setScopePos sets the start position of the scope for this Object.
	setScopePos(pos token.Pos)
}

// Id returns name if it is exported, otherwise it
// returns the name qualified with the package path.
func Id(pkg *Package, name string) string {}

// Parent returns the scope in which the object is declared.
// The result is nil for methods and struct fields.
func (obj *object) Parent() *Scope {}

// Pos returns the declaration position of the object's identifier.
func (obj *object) Pos() token.Pos {}

// Pkg returns the package to which the object belongs.
// The result is nil for labels and objects in the Universe scope.
func (obj *object) Pkg() *Package {}

// Name returns the object's (package-local, unqualified) name.
func (obj *object) Name() string {}

// Type returns the object's type.
func (obj *object) Type() Type {}

// Exported reports whether the object is exported (starts with a capital letter).
// It doesn't take into account whether the object is in a local (function) scope
// or not.
func (obj *object) Exported() bool {}

// Id is a wrapper for Id(obj.Pkg(), obj.Name()).
func (obj *object) Id() string {}

func (obj *object) String() string      { /*panic("abstract")*/ }

// A PkgName represents an imported Go package.
// PkgNames don't have a type.
type PkgName struct {
	object
	imported *Package
	used     bool // set if the package was used
}

// NewPkgName returns a new PkgName object representing an imported package.
// The remaining arguments set the attributes found with all Objects.
func NewPkgName(pos token.Pos, pkg *Package, name string, imported *Package) *PkgName {}

// Imported returns the package that was imported.
// It is distinct from Pkg(), which is the package containing the import statement.
func (obj *PkgName) Imported() *Package {}

// A Const represents a declared constant.
type Const struct {
	object
	val constant.Value
}

// NewConst returns a new constant with value val.
// The remaining arguments set the attributes found with all Objects.
func NewConst(pos token.Pos, pkg *Package, name string, typ Type, val constant.Value) *Const {}

// Val returns the constant's value.
func (obj *Const) Val() constant.Value {}

// A TypeName represents a name for a (defined or alias) type.
type TypeName struct {
	object
}

// NewTypeName returns a new type name denoting the given typ.
// The remaining arguments set the attributes found with all Objects.
//
// The typ argument may be a defined (Named) type or an alias type.
// It may also be nil such that the returned TypeName can be used as
// argument for NewNamed, which will set the TypeName's type as a side-
// effect.
func NewTypeName(pos token.Pos, pkg *Package, name string, typ Type) *TypeName {}

// IsAlias reports whether obj is an alias name for a type.
func (obj *TypeName) IsAlias() bool {}

// A Variable represents a declared variable (including function parameters and results, and struct fields).
type Var struct {
	object
	embedded bool // if set, the variable is an embedded struct field, and name is the type name
	isField  bool // var is struct field
	used     bool // set if the variable was used
}

// NewVar returns a new variable.
// The arguments set the attributes found with all Objects.
func NewVar(pos token.Pos, pkg *Package, name string, typ Type) *Var {}

// NewParam returns a new variable representing a function parameter.
func NewParam(pos token.Pos, pkg *Package, name string, typ Type) *Var {}

// NewField returns a new variable representing a struct field.
// For embedded fields, the name is the unqualified type name
/// under which the field is accessible.
func NewField(pos token.Pos, pkg *Package, name string, typ Type, embedded bool) *Var {}

// Anonymous reports whether the variable is an embedded field.
// Same as Embedded; only present for backward-compatibility.
func (obj *Var) Anonymous() bool {}

// Embedded reports whether the variable is an embedded field.
func (obj *Var) Embedded() bool {}

// IsField reports whether the variable is a struct field.
func (obj *Var) IsField() bool {}

// A Func represents a declared function, concrete method, or abstract
// (interface) method. Its Type() is always a *Signature.
// An abstract method may belong to many interfaces due to embedding.
type Func struct {
	object
	hasPtrRecv bool // only valid for methods that don't have a type yet
}

// NewFunc returns a new function with the given signature, representing
// the function's type.
func NewFunc(pos token.Pos, pkg *Package, name string, sig *Signature) *Func {}

// FullName returns the package- or receiver-type-qualified name of
// function or method obj.
func (obj *Func) FullName() string {}

// Scope returns the scope of the function's body block.
func (obj *Func) Scope() *Scope {}

// A Label represents a declared label.
// Labels don't have a type.
type Label struct {
	object
	used bool // set if the label was used
}

// NewLabel returns a new label.
func NewLabel(pos token.Pos, pkg *Package, name string) *Label {}

// A Builtin represents a built-in function.
// Builtins don't have a valid type.
type Builtin struct {
	object
	id builtinId
}

func newBuiltin(id builtinId) *Builtin {}

// Nil represents the predeclared value nil.
type Nil struct {
	object
}

// ObjectString returns the string form of obj.
// The Qualifier controls the printing of
// package-level objects, and may be nil.
func ObjectString(obj Object, qf Qualifier) string {}

func (obj *PkgName) String() string  {}
func (obj *Const) String() string    {}
func (obj *TypeName) String() string {}
func (obj *Var) String() string      {}
func (obj *Func) String() string     {}
func (obj *Label) String() string    {}
func (obj *Builtin) String() string  {}
func (obj *Nil) String() string      {}

// A Package describes a Go package.
type Package struct {
	path     string
	name     string
	scope    *Scope
	complete bool
	imports  []*Package
	fake     bool // scope lookup errors are silently dropped if package is fake (internal use only)
}

// NewPackage returns a new Package for the given package path and name.
// The package is not complete and contains no explicit imports.
func NewPackage(path, name string) *Package {}

// Path returns the package path.
func (pkg *Package) Path() string {}

// Name returns the package name.
func (pkg *Package) Name() string {}

// SetName sets the package name.
func (pkg *Package) SetName(name string) {}

// Scope returns the (complete or incomplete) package scope
// holding the objects declared at package level (TypeNames,
// Consts, Vars, and Funcs).
func (pkg *Package) Scope() *Scope {}

// A package is complete if its scope contains (at least) all
// exported objects; otherwise it is incomplete.
func (pkg *Package) Complete() bool {}

// MarkComplete marks a package as complete.
func (pkg *Package) MarkComplete() {}

// Imports returns the list of packages directly imported by
// pkg; the list is in source order.
//
// If pkg was loaded from export data, Imports includes packages that
// provide package-level objects referenced by pkg. This may be more or
// less than the set of packages directly imported by pkg's source code.
func (pkg *Package) Imports() []*Package {}

// SetImports sets the list of explicitly imported packages to list.
// It is the caller's responsibility to make sure list elements are unique.
func (pkg *Package) SetImports(list []*Package) {}

func (pkg *Package) String() string {}

// IsInterface reports whether typ is an interface type.
func IsInterface(typ Type) bool {}

// Comparable reports whether values of type T are comparable.
func Comparable(T Type) bool {}

// Default returns the default "typed" type for an "untyped" type;
// it returns the incoming type for all other types. The default type
// for untyped nil is untyped nil.
//
func Default(typ Type) Type {}

// A Scope maintains a set of objects and links to its containing
// (parent) and contained (children) scopes. Objects may be inserted
// and looked up by name. The zero value for Scope is a ready-to-use
// empty scope.
type Scope struct {
	parent   *Scope
	children []*Scope
	elems    map[string]Object // lazily allocated
	pos, end token.Pos         // scope extent; may be invalid
	comment  string            // for debugging only
	isFunc   bool              // set if this is a function scope (internal use only)
}
/*
package main

import (
	"bytes"
	"fmt"
	"go/ast"
	"go/importer"
	"go/parser"
	"go/token"
	"go/types"
	"log"
	"regexp"
)

func main() {
	// Parse the source files for a package.
	fset := token.NewFileSet()
	var files []*ast.File
	for _, file := range []struct{ name, input string }{
		{"main.go", `
package main
import "fmt"
func main() {
	freezing := FToC(-18)
	fmt.Println(freezing, Boiling) }
`},
		{"celsius.go", `
package main
import "fmt"
type Celsius float64
func (c Celsius) String() string { return fmt.Sprintf("%g°C", c) }
func FToC(f float64) Celsius { return Celsius(f - 32 / 9 * 5) }
const Boiling Celsius = 100
func Unused() { {}; {{ var x int; _ = x }} } // make sure empty block scopes get printed
`},
	} {
		f, err := parser.ParseFile(fset, file.name, file.input, 0)
		if err != nil {
			log.Fatal(err)
		}
		files = append(files, f)
	}

	// Type-check a package consisting of these files.
	// Type information for the imported "fmt" package
	// comes from $GOROOT/pkg/$GOOS_$GOOARCH/fmt.a.
	conf := types.Config{Importer: importer.Default()}
	pkg, err := conf.Check("temperature", fset, files, nil)
	if err != nil {
		log.Fatal(err)
	}

	// Print the tree of scopes.
	// For determinism, we redact addresses.
	var buf bytes.Buffer
	pkg.Scope().WriteTo(&buf, 0, true)
	rx := regexp.MustCompile(` 0x[a-fA-F0-9]*`)
	fmt.Println(rx.ReplaceAllString(buf.String(), ""))

}
*/

// NewScope returns a new, empty scope contained in the given parent
// scope, if any. The comment is for debugging only.
func NewScope(parent *Scope, pos, end token.Pos, comment string) *Scope {}

// Parent returns the scope's containing (parent) scope.
func (s *Scope) Parent() *Scope {}

// Len returns the number of scope elements.
func (s *Scope) Len() int {}

// Names returns the scope's element names in sorted order.
func (s *Scope) Names() []string {}

// NumChildren returns the number of scopes nested in s.
func (s *Scope) NumChildren() int {}

// Child returns the i'th child scope for 0 <= i < NumChildren().
func (s *Scope) Child(i int) *Scope {}

// Lookup returns the object in scope s with the given name if such an
// object exists; otherwise the result is nil.
func (s *Scope) Lookup(name string) Object {}

// LookupParent follows the parent chain of scopes starting with s until
// it finds a scope where Lookup(name) returns a non-nil object, and then
// returns that scope and object. If a valid position pos is provided,
// only objects that were declared at or before pos are considered.
// If no such scope and object exists, the result is (nil, nil).
//
// Note that obj.Parent() may be different from the returned scope if the
// object was inserted into the scope and already had a parent at that
// time (see Insert). This can only happen for dot-imported objects
// whose scope is the scope of the package that exported them.
func (s *Scope) LookupParent(name string, pos token.Pos) (*Scope, Object) {}

// Insert attempts to insert an object obj into scope s.
// If s already contains an alternative object alt with
// the same name, Insert leaves s unchanged and returns alt.
// Otherwise it inserts obj, sets the object's parent scope
// if not already set, and returns nil.
func (s *Scope) Insert(obj Object) Object {}

// Pos and End describe the scope's source code extent [pos, end).
// The results are guaranteed to be valid only if the type-checked
// AST has complete position information. The extent is undefined
// for Universe and package scopes.
func (s *Scope) Pos() token.Pos { return s.pos }
func (s *Scope) End() token.Pos { return s.end }

// Contains reports whether pos is within the scope's extent.
// The result is guaranteed to be valid only if the type-checked
// AST has complete position information.
func (s *Scope) Contains(pos token.Pos) bool {}

// Innermost returns the innermost (child) scope containing
// pos. If pos is not within any scope, the result is nil.
// The result is also nil for the Universe scope.
// The result is guaranteed to be valid only if the type-checked
// AST has complete position information.
func (s *Scope) Innermost(pos token.Pos) *Scope {}

// WriteTo writes a string representation of the scope to w,
// with the scope elements sorted by name.
// The level of indentation is controlled by n >= 0, with
// n == 0 for no indentation.
// If recurse is set, it also writes nested (children) scopes.
func (s *Scope) WriteTo(w io.Writer, n int, recurse bool) {}

// String returns a string representation of the scope, for debugging.
func (s *Scope) String() string {}

// SelectionKind describes the kind of a selector expression x.f
// (excluding qualified identifiers).
type SelectionKind int

const (
	FieldVal   SelectionKind = iota // x.f is a struct field selector
	MethodVal                       // x.f is a method selector
	MethodExpr                      // x.f is a method expression
)

// A Selection describes a selector expression x.f.
// For the declarations:
//
//	type T struct{ x int; E }
//	type E struct{}
//	func (e E) m() {}
//	var p *T
//
// the following relations exist:
//
//	Selector    Kind          Recv    Obj    Type       Index     Indirect
//
//	p.x         FieldVal      T       x      int        {0}       true
//	p.m         MethodVal     *T      m      func()     {1, 0}    true
//	T.m         MethodExpr    T       m      func(T)    {1, 0}    false
//
type Selection struct {
	kind     SelectionKind
	recv     Type   // type of x
	obj      Object // object denoted by x.f
	index    []int  // path from x to x.f
	indirect bool   // set if there was any pointer indirection on the path
}

// Kind returns the selection kind.
func (s *Selection) Kind() SelectionKind {}

// Recv returns the type of x in x.f.
func (s *Selection) Recv() Type {}

// Obj returns the object denoted by x.f; a *Var for
// a field selection, and a *Func in all other cases.
func (s *Selection) Obj() Object {}

// Type returns the type of x.f, which may be different from the type of f.
// See Selection for more information.
func (s *Selection) Type() Type {}

// Index describes the path from x to f in x.f.
// The last index entry is the field or method index of the type declaring f;
// either:
//
//	1) the list of declared methods of a named type; or
//	2) the list of methods of an interface type; or
//	3) the list of fields of a struct type.
//
// The earlier index entries are the indices of the embedded fields implicitly
// traversed to get from (the type of) x to f, starting at embedding depth 0.
func (s *Selection) Index() []int {}

// Indirect reports whether any pointer indirection was required to get from
// x to f in x.f.
func (s *Selection) Indirect() bool {}

func (s *Selection) String() string {}

// SelectionString returns the string form of s.
// The Qualifier controls the printing of
// package-level objects, and may be nil.
//
// Examples:
//	"field (T) f int"
//	"method (T) f(X) Y"
//	"method expr (T) f(X) Y"
//
func SelectionString(s *Selection, qf Qualifier) string {}

// Sizes defines the sizing functions for package unsafe.
type Sizes interface {
	// Alignof returns the alignment of a variable of type T.
	// Alignof must implement the alignment guarantees required by the spec.
	Alignof(T Type) int64

	// Offsetsof returns the offsets of the given struct fields, in bytes.
	// Offsetsof must implement the offset guarantees required by the spec.
	Offsetsof(fields []*Var) []int64

	// Sizeof returns the size of a variable of type T.
	// Sizeof must implement the size guarantees required by the spec.
	Sizeof(T Type) int64
}

// StdSizes is a convenience type for creating commonly used Sizes.
// It makes the following simplifying assumptions:
//
//	- The size of explicitly sized basic types (int16, etc.) is the
//	  specified size.
//	- The size of strings and interfaces is 2*WordSize.
//	- The size of slices is 3*WordSize.
//	- The size of an array of n elements corresponds to the size of
//	  a struct of n consecutive fields of the array's element type.
//      - The size of a struct is the offset of the last field plus that
//	  field's size. As with all element types, if the struct is used
//	  in an array its size must first be aligned to a multiple of the
//	  struct's alignment.
//	- All other types have size WordSize.
//	- Arrays and structs are aligned per spec definition; all other
//	  types are naturally aligned with a maximum alignment MaxAlign.
//
// *StdSizes implements Sizes.
//
type StdSizes struct {
	WordSize int64 // word size in bytes - must be >= 4 (32bits)
	MaxAlign int64 // maximum alignment in bytes - must be >= 1
}

func (s *StdSizes) Alignof(T Type) int64 {}

func (s *StdSizes) Offsetsof(fields []*Var) []int64 {}

func (s *StdSizes) Sizeof(T Type) int64 {}

// SizesFor returns the Sizes used by a compiler for an architecture.
// The result is nil if a compiler/architecture pair is not known.
//
// Supported architectures for compiler "gc":
// "386", "arm", "arm64", "amd64", "amd64p32", "mips", "mipsle",
// "mips64", "mips64le", "ppc64", "ppc64le", "riscv64", "s390x", "sparc64", "wasm".
func SizesFor(compiler, arch string) Sizes {}

// A Type represents a type of Go.
// All types implement the Type interface.
type Type interface {
	// Underlying returns the underlying type of a type.
	Underlying() Type

	// String returns a string representation of a type.
	String() string
}

// BasicKind describes the kind of basic type.
type BasicKind int

const (
	Invalid BasicKind = iota // type is invalid

	// predeclared types
	Bool
	Int
	Int8
	Int16
	Int32
	Int64
	Uint
	Uint8
	Uint16
	Uint32
	Uint64
	Uintptr
	Float32
	Float64
	Complex64
	Complex128
	String
	UnsafePointer

	// types for untyped values
	UntypedBool
	UntypedInt
	UntypedRune
	UntypedFloat
	UntypedComplex
	UntypedString
	UntypedNil

	// aliases
	Byte = Uint8
	Rune = Int32
)

// BasicInfo is a set of flags describing properties of a basic type.
type BasicInfo int

// Properties of basic types.
const (
	IsBoolean BasicInfo = 1 << iota
	IsInteger
	IsUnsigned
	IsFloat
	IsComplex
	IsString
	IsUntyped

	IsOrdered   = IsInteger | IsFloat | IsString
	IsNumeric   = IsInteger | IsFloat | IsComplex
	IsConstType = IsBoolean | IsNumeric | IsString
)

// A Basic represents a basic type.
type Basic struct {
	kind BasicKind
	info BasicInfo
	name string
}

// Kind returns the kind of basic type b.
func (b *Basic) Kind() BasicKind {}

// Info returns information about properties of basic type b.
func (b *Basic) Info() BasicInfo {}

// Name returns the name of basic type b.
func (b *Basic) Name() string {}

// An Array represents an array type.
type Array struct {
	len  int64
	elem Type
}

// NewArray returns a new array type for the given element type and length.
// A negative length indicates an unknown length.
func NewArray(elem Type, len int64) *Array {}

// Len returns the length of array a.
// A negative result indicates an unknown length.
func (a *Array) Len() int64 {}

// Elem returns element type of array a.
func (a *Array) Elem() Type {}

// A Slice represents a slice type.
type Slice struct {
	elem Type
}

// NewSlice returns a new slice type for the given element type.
func NewSlice(elem Type) *Slice {}

// Elem returns the element type of slice s.
func (s *Slice) Elem() Type {}

// A Struct represents a struct type.
type Struct struct {
	fields []*Var
	tags   []string // field tags; nil if there are no tags
}

// NewStruct returns a new struct with the given fields and corresponding field tags.
// If a field with index i has a tag, tags[i] must be that tag, but len(tags) may be
// only as long as required to hold the tag with the largest index i. Consequently,
// if no field has a tag, tags may be nil.
func NewStruct(fields []*Var, tags []string) *Struct {
	// possible: panic("multiple fields with the same name")
	// possible: panic("more tags than fields")
}

// NumFields returns the number of fields in the struct (including blank and embedded fields).
func (s *Struct) NumFields() int {}

// Field returns the i'th field for 0 <= i < NumFields().
func (s *Struct) Field(i int) *Var {}

// Tag returns the i'th field tag for 0 <= i < NumFields().
func (s *Struct) Tag(i int) string {}

// A Pointer represents a pointer type.
type Pointer struct {
	base Type // element type
}

// NewPointer returns a new pointer type for the given element (base) type.
func NewPointer(elem Type) *Pointer {}

// Elem returns the element type for the given pointer p.
func (p *Pointer) Elem() Type {}

// A Tuple represents an ordered list of variables; a nil *Tuple is a valid (empty) tuple.
// Tuples are used as components of signatures and to represent the type of multiple
// assignments; they are not first class types of Go.
type Tuple struct {
	vars []*Var
}

// NewTuple returns a new tuple for the given variables.
func NewTuple(x ...*Var) *Tuple {}

// Len returns the number variables of tuple t.
func (t *Tuple) Len() int {}

// At returns the i'th variable of tuple t.
func (t *Tuple) At(i int) *Var {}

// A Signature represents a (non-builtin) function or method type.
// The receiver is ignored when comparing signatures for identity.
type Signature struct {
	// We need to keep the scope in Signature (rather than passing it around
	// and store it in the Func Object) because when type-checking a function
	// literal we call the general type checker which returns a general Type.
	// We then unpack the *Signature and use the scope for the literal body.
	scope    *Scope // function scope, present for package-local signatures
	recv     *Var   // nil if not a method
	params   *Tuple // (incoming) parameters from left to right; or nil
	results  *Tuple // (outgoing) results from left to right; or nil
	variadic bool   // true if the last parameter's type is of the form ...T (or string, for append built-in only)
}

// NewSignature returns a new function type for the given receiver, parameters,
// and results, either of which may be nil. If variadic is set, the function
// is variadic, it must have at least one parameter, and the last parameter
// must be of unnamed slice type.
func NewSignature(recv *Var, params, results *Tuple, variadic bool) *Signature {
	// possible: panic("types.NewSignature: variadic function must have at least one parameter")
	// possible: panic("types.NewSignature: variadic parameter must be of unnamed slice type")
}

// Recv returns the receiver of signature s (if a method), or nil if a
// function. It is ignored when comparing signatures for identity.
//
// For an abstract method, Recv returns the enclosing interface either
// as a *Named or an *Interface. Due to embedding, an interface may
// contain methods whose receiver type is a different interface.
func (s *Signature) Recv() *Var {}

// Params returns the parameters of signature s, or nil.
func (s *Signature) Params() *Tuple {}

// Results returns the results of signature s, or nil.
func (s *Signature) Results() *Tuple {}

// Variadic reports whether the signature s is variadic.
func (s *Signature) Variadic() bool {}

// An Interface represents an interface type.
type Interface struct {
	methods   []*Func // ordered list of explicitly declared methods
	embeddeds []Type  // ordered list of explicitly embedded types

	allMethods []*Func // ordered list of methods declared with or embedded in this interface (TODO(gri): replace with mset)
}

// NewInterface returns a new (incomplete) interface for the given methods and embedded types.
// Each embedded type must have an underlying type of interface type.
// NewInterface takes ownership of the provided methods and may modify their types by setting
// missing receivers. To compute the method set of the interface, Complete must be called.
//
// Deprecated: Use NewInterfaceType instead which allows any (even non-defined) interface types
// to be embedded. This is necessary for interfaces that embed alias type names referring to
// non-defined (literal) interface types.
func NewInterface(methods []*Func, embeddeds []*Named) *Interface {}

// NewInterfaceType returns a new (incomplete) interface for the given methods and embedded types.
// Each embedded type must have an underlying type of interface type (this property is not
// verified for defined types, which may be in the process of being set up and which don't
// have a valid underlying type yet).
// NewInterfaceType takes ownership of the provided methods and may modify their types by setting
// missing receivers. To compute the method set of the interface, Complete must be called.
func NewInterfaceType(methods []*Func, embeddeds []Type) *Interface {
	// possible: panic("embedded type is not an interface")
}

// NumExplicitMethods returns the number of explicitly declared methods of interface t.
func (t *Interface) NumExplicitMethods() int {}

// ExplicitMethod returns the i'th explicitly declared method of interface t for 0 <= i < t.NumExplicitMethods().
// The methods are ordered by their unique Id.
func (t *Interface) ExplicitMethod(i int) *Func {}

// NumEmbeddeds returns the number of embedded types in interface t.
func (t *Interface) NumEmbeddeds() int {}

// Embedded returns the i'th embedded defined (*Named) type of interface t for 0 <= i < t.NumEmbeddeds().
// The result is nil if the i'th embedded type is not a defined type.
//
// Deprecated: Use EmbeddedType which is not restricted to defined (*Named) types.
func (t *Interface) Embedded(i int) *Named {}

// EmbeddedType returns the i'th embedded type of interface t for 0 <= i < t.NumEmbeddeds().
func (t *Interface) EmbeddedType(i int) Type {}

// NumMethods returns the total number of methods of interface t.
// The interface must have been completed.
func (t *Interface) NumMethods() int {}

// Method returns the i'th method of interface t for 0 <= i < t.NumMethods().
// The methods are ordered by their unique Id.
// The interface must have been completed.
func (t *Interface) Method(i int) *Func {}

// Empty reports whether t is the empty interface.
// The interface must have been completed.
func (t *Interface) Empty() bool {}

// Complete computes the interface's method set. It must be called by users of
// NewInterfaceType and NewInterface after the interface's embedded types are
// fully defined and before using the interface type in any way other than to
// form other types. The interface must not contain duplicate methods or a
// panic occurs. Complete returns the receiver.
func (t *Interface) Complete() *Interface {}

// A Map represents a map type.
type Map struct {
	key, elem Type
}

// NewMap returns a new map for the given key and element types.
func NewMap(key, elem Type) *Map {}

// Key returns the key type of map m.
func (m *Map) Key() Type {}

// Elem returns the element type of map m.
func (m *Map) Elem() Type {}

// A Chan represents a channel type.
type Chan struct {
	dir  ChanDir
	elem Type
}

// A ChanDir value indicates a channel direction.
type ChanDir int

// The direction of a channel is indicated by one of these constants.
const (
	SendRecv ChanDir = iota
	SendOnly
	RecvOnly
)

// NewChan returns a new channel type for the given direction and element type.
func NewChan(dir ChanDir, elem Type) *Chan {}

// Dir returns the direction of channel c.
func (c *Chan) Dir() ChanDir {}

// Elem returns the element type of channel c.
func (c *Chan) Elem() Type {}

// A Named represents a named type.
type Named struct {
	info       typeInfo  // for cycle detection
	obj        *TypeName // corresponding declared object
	orig       Type      // type (on RHS of declaration) this *Named type is derived of (for cycle reporting)
	underlying Type      // possibly a *Named during setup; never a *Named once set up completely
	methods    []*Func   // methods declared for this type (not the method set of this type); signatures are type-checked lazily
}

// NewNamed returns a new named type for the given type name, underlying type, and associated methods.
// If the given type name obj doesn't have a type yet, its type is set to the returned named type.
// The underlying type must not be a *Named.
func NewNamed(obj *TypeName, underlying Type, methods []*Func) *Named {
	// possible: panic("types.NewNamed: underlying type must not be *Named")
}

// Obj returns the type name for the named type t.
func (t *Named) Obj() *TypeName {}

// NumMethods returns the number of explicit methods whose receiver is named type t.
func (t *Named) NumMethods() int {}

// Method returns the i'th method of named type t for 0 <= i < t.NumMethods().
func (t *Named) Method(i int) *Func {}

// SetUnderlying sets the underlying type and marks t as complete.
func (t *Named) SetUnderlying(underlying Type) {
	// possible: panic("types.Named.SetUnderlying: underlying type must not be nil")
	// possible: panic("types.Named.SetUnderlying: underlying type must not be *Named")
}

// AddMethod adds method m unless it is already in the method list.
func (t *Named) AddMethod(m *Func) {}

// Implementations for Type methods.

func (b *Basic) Underlying() Type     {}
func (a *Array) Underlying() Type     {}
func (s *Slice) Underlying() Type     {}
func (s *Struct) Underlying() Type    {}
func (p *Pointer) Underlying() Type   {}
func (t *Tuple) Underlying() Type     {}
func (s *Signature) Underlying() Type {}
func (t *Interface) Underlying() Type {}
func (m *Map) Underlying() Type       {}
func (c *Chan) Underlying() Type      {}
func (t *Named) Underlying() Type     {}

func (b *Basic) String() string     {}
func (a *Array) String() string     {}
func (s *Slice) String() string     {}
func (s *Struct) String() string    {}
func (p *Pointer) String() string   {}
func (t *Tuple) String() string     {}
func (s *Signature) String() string {}
func (t *Interface) String() string {}
func (m *Map) String() string       {}
func (c *Chan) String() string      {}
func (t *Named) String() string     {}

// A Qualifier controls how named package-level objects are printed in
// calls to TypeString, ObjectString, and SelectionString.
//
// These three formatting routines call the Qualifier for each
// package-level object O, and if the Qualifier returns a non-empty
// string p, the object is printed in the form p.O.
// If it returns an empty string, only the object name O is printed.
//
// Using a nil Qualifier is equivalent to using (*Package).Path: the
// object is qualified by the import path, e.g., "encoding/json.Marshal".
//
type Qualifier func(*Package) string

// RelativeTo returns a Qualifier that fully qualifies members of
// all packages other than pkg.
func RelativeTo(pkg *Package) Qualifier {}

// TypeString returns the string representation of typ.
// The Qualifier controls the printing of
// package-level objects, and may be nil.
func TypeString(typ Type, qf Qualifier) string {}

// WriteType writes the string representation of typ to buf.
// The Qualifier controls the printing of
// package-level objects, and may be nil.
func WriteType(buf *bytes.Buffer, typ Type, qf Qualifier) {}

// WriteSignature writes the representation of the signature sig to buf,
// without a leading "func" keyword.
// The Qualifier controls the printing of
// package-level objects, and may be nil.
func WriteSignature(buf *bytes.Buffer, sig *Signature, qf Qualifier) {}

// The Universe scope contains all predeclared objects of Go.
// It is the outermost scope of any chain of nested scopes.
var Universe *Scope

// The Unsafe package is the package returned by an importer
// for the import path "unsafe".
var Unsafe *Package

// Typ contains the predeclared *Basic types indexed by their
// corresponding BasicKind.
//
// The *Basic type for Typ[Byte] will have the name "uint8".
// Use Universe.Lookup("byte").Type() to obtain the specific
// alias basic type named "byte" (and analogous for "rune").
var Typ = []*Basic{
	Invalid: {Invalid, 0, "invalid type"},

	Bool:          {Bool, IsBoolean, "bool"},
	Int:           {Int, IsInteger, "int"},
	Int8:          {Int8, IsInteger, "int8"},
	Int16:         {Int16, IsInteger, "int16"},
	Int32:         {Int32, IsInteger, "int32"},
	Int64:         {Int64, IsInteger, "int64"},
	Uint:          {Uint, IsInteger | IsUnsigned, "uint"},
	Uint8:         {Uint8, IsInteger | IsUnsigned, "uint8"},
	Uint16:        {Uint16, IsInteger | IsUnsigned, "uint16"},
	Uint32:        {Uint32, IsInteger | IsUnsigned, "uint32"},
	Uint64:        {Uint64, IsInteger | IsUnsigned, "uint64"},
	Uintptr:       {Uintptr, IsInteger | IsUnsigned, "uintptr"},
	Float32:       {Float32, IsFloat, "float32"},
	Float64:       {Float64, IsFloat, "float64"},
	Complex64:     {Complex64, IsComplex, "complex64"},
	Complex128:    {Complex128, IsComplex, "complex128"},
	String:        {String, IsString, "string"},
	UnsafePointer: {UnsafePointer, 0, "Pointer"},

	UntypedBool:    {UntypedBool, IsBoolean | IsUntyped, "untyped bool"},
	UntypedInt:     {UntypedInt, IsInteger | IsUntyped, "untyped int"},
	UntypedRune:    {UntypedRune, IsInteger | IsUntyped, "untyped rune"},
	UntypedFloat:   {UntypedFloat, IsFloat | IsUntyped, "untyped float"},
	UntypedComplex: {UntypedComplex, IsComplex | IsUntyped, "untyped complex"},
	UntypedString:  {UntypedString, IsString | IsUntyped, "untyped string"},
	UntypedNil:     {UntypedNil, IsUntyped, "untyped nil"},
}

var aliases = [...]*Basic{
	{Byte, IsInteger | IsUnsigned, "byte"},
	{Rune, IsInteger, "rune"},
}

// DefPredeclaredTestFuncs defines the assert and trace built-ins.
// These built-ins are intended for debugging and testing of this
// package only.
func DefPredeclaredTestFuncs() {}
