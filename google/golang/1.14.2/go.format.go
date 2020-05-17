// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package format implements standard formatting of Go source.
//
// Note that formatting of Go source code changes over time, so tools relying on
// consistent formatting should execute a specific version of the gofmt binary
// instead of using this package. That way, the formatting will be stable, and
// the tools won't need to be recompiled each time gofmt changes.
//
// For example, pre-submit checks that use this package directly would behave
// differently depending on what Go version each developer uses, causing the
// check to be inherently fragile.
package format

import (
	"bytes"
	"fmt"
	"go/ast"
	"go/parser"
	"go/printer"
	"go/token"
	"io"
)

// Node formats node in canonical gofmt style and writes the result to dst.
//
// The node type must be *ast.File, *printer.CommentedNode, []ast.Decl,
// []ast.Stmt, or assignment-compatible to ast.Expr, ast.Decl, ast.Spec,
// or ast.Stmt. Node does not modify node. Imports are not sorted for
// nodes representing partial source files (for instance, if the node is
// not an *ast.File or a *printer.CommentedNode not wrapping an *ast.File).
//
// The function may return early (before the entire result is written)
// and return a formatting error, for instance due to an incorrect AST.
//
func Node(dst io.Writer, fset *token.FileSet, node interface{}) error {}
/*
package main

import (
	"bytes"
	"fmt"
	"go/format"
	"go/parser"
	"go/token"
	"log"
)

func main() {
	const expr = "(6+2*3)/4"

	// parser.ParseExpr parses the argument and returns the
	// corresponding ast.Node.
	node, err := parser.ParseExpr(expr)
	if err != nil {
		log.Fatal(err)
	}

	// Create a FileSet for node. Since the node does not come
	// from a real source file, fset will be empty.
	fset := token.NewFileSet()

	var buf bytes.Buffer
	err = format.Node(&buf, fset, node)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(buf.String())

}
*/

// Source formats src in canonical gofmt style and returns the result
// or an (I/O or syntax) error. src is expected to be a syntactically
// correct Go source file, or a list of Go declarations or statements.
//
// If src is a partial source file, the leading and trailing space of src
// is applied to the result (such that it has the same leading and trailing
// space as src), and the result is indented by the same amount as the first
// line of src containing code. Imports are not sorted for partial source files.
//
func Source(src []byte) ([]byte, error) {}
