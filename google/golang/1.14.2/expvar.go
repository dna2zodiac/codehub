// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package expvar provides a standardized interface to public variables, such
// as operation counters in servers. It exposes these variables via HTTP at
// /debug/vars in JSON format.
//
// Operations to set or modify these public variables are atomic.
//
// In addition to adding the HTTP handler, this package registers the
// following variables:
//
//	cmdline   os.Args
//	memstats  runtime.Memstats
//
// The package is sometimes only imported for the side effect of
// registering its HTTP handler and the above variables. To use it
// this way, link this package into your program:
//	import _ "expvar"
//
package expvar

import (
	"net/http"
	"os"
	"runtime"
	"sync"
	"sync/atomic"
)

// Var is an abstract type for all exported variables.
type Var interface {
	// String returns a valid JSON value for the variable.
	// Types with String methods that do not return valid JSON
	// (such as time.Time) must not be used as a Var.
	String() string
}

// Int is a 64-bit integer variable that satisfies the Var interface.
type Int struct {
	i int64
}

func (v *Int) Value() int64 {}

func (v *Int) String() string {}

func (v *Int) Add(delta int64) {}

func (v *Int) Set(value int64) {}

// Float is a 64-bit float variable that satisfies the Var interface.
type Float struct {
	f uint64
}

func (v *Float) Value() float64 {}

func (v *Float) String() string {}

// Add adds delta to v.
func (v *Float) Add(delta float64) {}

// Set sets v to value.
func (v *Float) Set(value float64) {}

// Map is a string-to-Var map variable that satisfies the Var interface.
type Map struct {
	m      sync.Map // map[string]Var
	keysMu sync.RWMutex
	keys   []string // sorted
}

// KeyValue represents a single entry in a Map.
type KeyValue struct {
	Key   string
	Value Var
}

func (v *Map) String() string {}

// Init removes all keys from the map.
func (v *Map) Init() *Map {}

func (v *Map) Get(key string) Var {}

func (v *Map) Set(key string, av Var) {}

// Add adds delta to the *Int value stored under the given map key.
func (v *Map) Add(key string, delta int64) {}

// AddFloat adds delta to the *Float value stored under the given map key.
func (v *Map) AddFloat(key string, delta float64) {}

// Delete deletes the given key from the map.
func (v *Map) Delete(key string) {}

// Do calls f for each entry in the map.
// The map is locked during the iteration,
// but existing entries may be concurrently updated.
func (v *Map) Do(f func(KeyValue)) {}

// String is a string variable, and satisfies the Var interface.
type String struct {
	s atomic.Value // string
}

func (v *String) Value() string {}

// String implements the Var interface. To get the unquoted string
// use Value.
func (v *String) String() string {}

func (v *String) Set(value string) {}

// Func implements Var by calling the function
// and formatting the returned value using JSON.
type Func func() interface{}

func (f Func) Value() interface{} {}

func (f Func) String() string {}

// Publish declares a named exported variable. This should be called from a
// package's init function when it creates its Vars. If the name is already
// registered then this will log.Panic.
func Publish(name string, v Var) {}

// Get retrieves a named exported variable. It returns nil if the name has
// not been registered.
func Get(name string) Var {}

// Convenience functions for creating new exported variables.

func NewInt(name string) *Int {}

func NewFloat(name string) *Float {}

func NewMap(name string) *Map {}

func NewString(name string) *String {}

// Do calls f for each exported variable.
// The global variable map is locked during the iteration,
// but existing entries may be concurrently updated.
func Do(f func(KeyValue)) {}

// Handler returns the expvar HTTP Handler.
//
// This is only needed to install the handler in a non-standard location.
func Handler() http.Handler {
	return http.HandlerFunc(expvarHandler)
}

func cmdline() interface{} {
	return os.Args
}

func memstats() interface{} {
	stats := new(runtime.MemStats)
	runtime.ReadMemStats(stats)
	return *stats
}

func init() {
	http.HandleFunc("/debug/vars", expvarHandler)
	Publish("cmdline", Func(cmdline))
	Publish("memstats", Func(memstats))
}
