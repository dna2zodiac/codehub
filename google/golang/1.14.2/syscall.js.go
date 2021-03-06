// Copyright 2018 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// +build js,wasm

// Package js gives access to the WebAssembly host environment when using the js/wasm architecture.
// Its API is based on JavaScript semantics.
//
// This package is EXPERIMENTAL. Its current scope is only to allow tests to run, but not yet to provide a
// comprehensive API for users. It is exempt from the Go compatibility promise.
package js

// Wrapper is implemented by types that are backed by a JavaScript value.
type Wrapper interface {
	// JSValue returns a JavaScript value associated with an object.
	JSValue() Value
}

// Value represents a JavaScript value. The zero value is the JavaScript value "undefined".
// Values can be checked for equality with the Equal method.
type Value struct {
	_     [0]func() // uncomparable; to make == not compile
	ref   ref       // identifies a JavaScript value, see ref type
	gcPtr *ref      // used to trigger the finalizer when the Value is not referenced any more
}

// JSValue implements Wrapper interface.
func (v Value) JSValue() Value {}

// Error wraps a JavaScript error.
type Error struct {
	// Value is the underlying JavaScript error value.
	Value
}

// Error implements the error interface.
func (e Error) Error() string {}

// Equal reports whether v and w are equal according to JavaScript's === operator.
func (v Value) Equal(w Value) bool {}

// Undefined returns the JavaScript value "undefined".
func Undefined() Value {}

// IsUndefined reports whether v is the JavaScript value "undefined".
func (v Value) IsUndefined() bool {}

// Null returns the JavaScript value "null".
func Null() Value {}

// IsNull reports whether v is the JavaScript value "null".
func (v Value) IsNull() bool {}

// IsNaN reports whether v is the JavaScript value "NaN".
func (v Value) IsNaN() bool {}

// Global returns the JavaScript global object, usually "window" or "global".
func Global() Value {}

// ValueOf returns x as a JavaScript value:
//
//  | Go                     | JavaScript             |
//  | ---------------------- | ---------------------- |
//  | js.Value               | [its value]            |
//  | js.Func                | function               |
//  | nil                    | null                   |
//  | bool                   | boolean                |
//  | integers and floats    | number                 |
//  | string                 | string                 |
//  | []interface{}          | new array              |
//  | map[string]interface{} | new object             |
//
// Panics if x is not one of the expected types.
func ValueOf(x interface{}) Value {
	// possible: panic("ValueOf: invalid value")
}

// Type represents the JavaScript type of a Value.
type Type int

const (
	TypeUndefined Type = iota
	TypeNull
	TypeBoolean
	TypeNumber
	TypeString
	TypeSymbol
	TypeObject
	TypeFunction
)

func (t Type) String() string {
	// possible: panic("bad type")
}

// Type returns the JavaScript type of the value v. It is similar to JavaScript's typeof operator,
// except that it returns TypeNull instead of TypeObject for null.
func (v Value) Type() Type {
	// possible: panic("bad type flag")
}

// Get returns the JavaScript property p of value v.
// It panics if v is not a JavaScript object.
func (v Value) Get(p string) Value {}

// Set sets the JavaScript property p of value v to ValueOf(x).
// It panics if v is not a JavaScript object.
func (v Value) Set(p string, x interface{}) {}

// Delete deletes the JavaScript property p of value v.
// It panics if v is not a JavaScript object.
func (v Value) Delete(p string) {
	// possible: panic(&ValueError{"Value.Delete", vType})
}

// Index returns JavaScript index i of value v.
// It panics if v is not a JavaScript object.
func (v Value) Index(i int) Value {
	// possible: panic(&ValueError{"Value.Index", vType})
}

// SetIndex sets the JavaScript index i of value v to ValueOf(x).
// It panics if v is not a JavaScript object.
func (v Value) SetIndex(i int, x interface{}) {
	// possbile: panic(&ValueError{"Value.SetIndex", vType})
}

// Length returns the JavaScript property "length" of v.
// It panics if v is not a JavaScript object.
func (v Value) Length() int {
	// possible: panic(&ValueError{"Value.SetIndex", vType})
}

// Call does a JavaScript call to the method m of value v with the given arguments.
// It panics if v has no method m.
// The arguments get mapped to JavaScript values according to the ValueOf function.
func (v Value) Call(m string, args ...interface{}) Value {
	// possible: panic(&ValueError{"Value.Call", vType})
	// possible: panic("syscall/js: Value.Call: property " + m + " is not a function, got " + propType.String())
	// possible: panic(Error{makeValue(res)})
}

// Invoke does a JavaScript call of the value v with the given arguments.
// It panics if v is not a JavaScript function.
// The arguments get mapped to JavaScript values according to the ValueOf function.
func (v Value) Invoke(args ...interface{}) Value {
	// possible: panic(&ValueError{"Value.Invoke", vType})
	// possible: panic(Error{makeValue(res)})
}

// New uses JavaScript's "new" operator with value v as constructor and the given arguments.
// It panics if v is not a JavaScript function.
// The arguments get mapped to JavaScript values according to the ValueOf function.
func (v Value) New(args ...interface{}) Value {
	// possible: panic(&ValueError{"Value.Invoke", vType})
	// possible: panic(Error{makeValue(res)})
}

// Float returns the value v as a float64.
// It panics if v is not a JavaScript number.
func (v Value) Float() float64 {}

// Int returns the value v truncated to an int.
// It panics if v is not a JavaScript number.
func (v Value) Int() int {}

// Bool returns the value v as a bool.
// It panics if v is not a JavaScript boolean.
func (v Value) Bool() bool {
	// possible: panic(&ValueError{"Value.Bool", v.Type()})
}

// Truthy returns the JavaScript "truthiness" of the value v. In JavaScript,
// false, 0, "", null, undefined, and NaN are "falsy", and everything else is
// "truthy". See https://developer.mozilla.org/en-US/docs/Glossary/Truthy.
func (v Value) Truthy() bool {
	// possible: panic("bad type")
}

// String returns the value v as a string.
// String is a special case because of Go's String method convention. Unlike the other getters,
// it does not panic if v's Type is not TypeString. Instead, it returns a string of the form "<T>"
// or "<T: V>" where T is v's type and V is a string representation of v's value.
func (v Value) String() string {
	// possible: panic("bad type")
}

// InstanceOf reports whether v is an instance of type t according to JavaScript's instanceof operator.
func (v Value) InstanceOf(t Value) bool {}

// A ValueError occurs when a Value method is invoked on
// a Value that does not support it. Such cases are documented
// in the description of each method.
type ValueError struct {
	Method string
	Type   Type
}

func (e *ValueError) Error() string {}

// CopyBytesToGo copies bytes from the Uint8Array src to dst.
// It returns the number of bytes copied, which will be the minimum of the lengths of src and dst.
// CopyBytesToGo panics if src is not an Uint8Array.
func CopyBytesToGo(dst []byte, src Value) int {
	// possible: panic("syscall/js: CopyBytesToGo: expected src to be an Uint8Array")
}

// CopyBytesToJS copies bytes from src to the Uint8Array dst.
// It returns the number of bytes copied, which will be the minimum of the lengths of src and dst.
// CopyBytesToJS panics if dst is not an Uint8Array.
func CopyBytesToJS(dst Value, src []byte) int {
	// possible: panic("syscall/js: CopyBytesToJS: expected dst to be an Uint8Array")
}

// Func is a wrapped Go function to be called by JavaScript.
type Func struct {
	Value // the JavaScript function that invokes the Go function
	id    uint32
}

// FuncOf returns a wrapped function.
//
// Invoking the JavaScript function will synchronously call the Go function fn with the value of JavaScript's
// "this" keyword and the arguments of the invocation.
// The return value of the invocation is the result of the Go function mapped back to JavaScript according to ValueOf.
//
// A wrapped function triggered during a call from Go to JavaScript gets executed on the same goroutine.
// A wrapped function triggered by JavaScript's event loop gets executed on an extra goroutine.
// Blocking operations in the wrapped function will block the event loop.
// As a consequence, if one wrapped function blocks, other wrapped funcs will not be processed.
// A blocking function should therefore explicitly start a new goroutine.
//
// Func.Release must be called to free up resources when the function will not be used any more.
func FuncOf(fn func(this Value, args []Value) interface{}) Func {}
/*
var cb js.Func
cb = js.FuncOf(func(this js.Value, args []js.Value) interface{} {
    fmt.Println("button clicked")
    cb.Release() // release the function if the button will not be clicked again
    return nil
})
js.Global().Get("document").Call("getElementById", "myButton").Call("addEventListener", "click", cb)
*/

// Release frees up resources allocated for the function.
// The function must not be invoked after calling Release.
func (c Func) Release() {}
