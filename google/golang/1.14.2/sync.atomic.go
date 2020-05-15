// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package atomic provides low-level atomic memory primitives
// useful for implementing synchronization algorithms.
//
// These functions require great care to be used correctly.
// Except for special, low-level applications, synchronization is better
// done with channels or the facilities of the sync package.
// Share memory by communicating;
// don't communicate by sharing memory.
//
// The swap operation, implemented by the SwapT functions, is the atomic
// equivalent of:
//
//	old = *addr
//	*addr = new
//	return old
//
// The compare-and-swap operation, implemented by the CompareAndSwapT
// functions, is the atomic equivalent of:
//
//	if *addr == old {
//		*addr = new
//		return true
//	}
//	return false
//
// The add operation, implemented by the AddT functions, is the atomic
// equivalent of:
//
//	*addr += delta
//	return *addr
//
// The load and store operations, implemented by the LoadT and StoreT
// functions, are the atomic equivalents of "return *addr" and
// "*addr = val".
//
package atomic

import (
	"unsafe"
)

// BUG(rsc): On x86-32, the 64-bit functions use instructions unavailable before the Pentium MMX.
//
// On non-Linux ARM, the 64-bit functions use instructions unavailable before the ARMv6k core.
//
// On ARM, x86-32, and 32-bit MIPS,
// it is the caller's responsibility to arrange for 64-bit
// alignment of 64-bit words accessed atomically. The first word in a
// variable or in an allocated struct, array, or slice can be relied upon to be
// 64-bit aligned.

// SwapInt32 atomically stores new into *addr and returns the previous *addr value.
func SwapInt32(addr *int32, new int32) (old int32)

// SwapInt64 atomically stores new into *addr and returns the previous *addr value.
func SwapInt64(addr *int64, new int64) (old int64)

// SwapUint32 atomically stores new into *addr and returns the previous *addr value.
func SwapUint32(addr *uint32, new uint32) (old uint32)

// SwapUint64 atomically stores new into *addr and returns the previous *addr value.
func SwapUint64(addr *uint64, new uint64) (old uint64)

// SwapUintptr atomically stores new into *addr and returns the previous *addr value.
func SwapUintptr(addr *uintptr, new uintptr) (old uintptr)

// SwapPointer atomically stores new into *addr and returns the previous *addr value.
func SwapPointer(addr *unsafe.Pointer, new unsafe.Pointer) (old unsafe.Pointer)

// CompareAndSwapInt32 executes the compare-and-swap operation for an int32 value.
func CompareAndSwapInt32(addr *int32, old, new int32) (swapped bool)

// CompareAndSwapInt64 executes the compare-and-swap operation for an int64 value.
func CompareAndSwapInt64(addr *int64, old, new int64) (swapped bool)

// CompareAndSwapUint32 executes the compare-and-swap operation for a uint32 value.
func CompareAndSwapUint32(addr *uint32, old, new uint32) (swapped bool)

// CompareAndSwapUint64 executes the compare-and-swap operation for a uint64 value.
func CompareAndSwapUint64(addr *uint64, old, new uint64) (swapped bool)

// CompareAndSwapUintptr executes the compare-and-swap operation for a uintptr value.
func CompareAndSwapUintptr(addr *uintptr, old, new uintptr) (swapped bool)

// CompareAndSwapPointer executes the compare-and-swap operation for a unsafe.Pointer value.
func CompareAndSwapPointer(addr *unsafe.Pointer, old, new unsafe.Pointer) (swapped bool)

// AddInt32 atomically adds delta to *addr and returns the new value.
func AddInt32(addr *int32, delta int32) (new int32)

// AddUint32 atomically adds delta to *addr and returns the new value.
// To subtract a signed positive constant value c from x, do AddUint32(&x, ^uint32(c-1)).
// In particular, to decrement x, do AddUint32(&x, ^uint32(0)).
func AddUint32(addr *uint32, delta uint32) (new uint32)

// AddInt64 atomically adds delta to *addr and returns the new value.
func AddInt64(addr *int64, delta int64) (new int64)

// AddUint64 atomically adds delta to *addr and returns the new value.
// To subtract a signed positive constant value c from x, do AddUint64(&x, ^uint64(c-1)).
// In particular, to decrement x, do AddUint64(&x, ^uint64(0)).
func AddUint64(addr *uint64, delta uint64) (new uint64)

// AddUintptr atomically adds delta to *addr and returns the new value.
func AddUintptr(addr *uintptr, delta uintptr) (new uintptr)

// LoadInt32 atomically loads *addr.
func LoadInt32(addr *int32) (val int32)

// LoadInt64 atomically loads *addr.
func LoadInt64(addr *int64) (val int64)

// LoadUint32 atomically loads *addr.
func LoadUint32(addr *uint32) (val uint32)

// LoadUint64 atomically loads *addr.
func LoadUint64(addr *uint64) (val uint64)

// LoadUintptr atomically loads *addr.
func LoadUintptr(addr *uintptr) (val uintptr)

// LoadPointer atomically loads *addr.
func LoadPointer(addr *unsafe.Pointer) (val unsafe.Pointer)

// StoreInt32 atomically stores val into *addr.
func StoreInt32(addr *int32, val int32)

// StoreInt64 atomically stores val into *addr.
func StoreInt64(addr *int64, val int64)

// StoreUint32 atomically stores val into *addr.
func StoreUint32(addr *uint32, val uint32)

// StoreUint64 atomically stores val into *addr.
func StoreUint64(addr *uint64, val uint64)

// StoreUintptr atomically stores val into *addr.
func StoreUintptr(addr *uintptr, val uintptr)

// StorePointer atomically stores val into *addr.
func StorePointer(addr *unsafe.Pointer, val unsafe.Pointer)

// A Value provides an atomic load and store of a consistently typed value.
// The zero value for a Value returns nil from Load.
// Once Store has been called, a Value must not be copied.
//
// A Value must not be copied after first use.
type Value struct {
	v interface{}
}
/* Config: The following example shows how to use Value for periodic program config updates and propagation of the changes to worker goroutines.
package main

import (
	"sync/atomic"
	"time"
)

func loadConfig() map[string]string {
	return make(map[string]string)
}

func requests() chan int {
	return make(chan int)
}

func main() {
	var config atomic.Value // holds current server configuration
	// Create initial config value and store into config.
	config.Store(loadConfig())
	go func() {
		// Reload config every 10 seconds
		// and update config value with the new version.
		for {
			time.Sleep(10 * time.Second)
			config.Store(loadConfig())
		}
	}()
	// Create worker goroutines that handle incoming requests
	// using the latest config value.
	for i := 0; i < 10; i++ {
		go func() {
			for r := range requests() {
				c := config.Load()
				// Handle request r using config c.
				_, _ = r, c
			}
		}()
	}
}
*/
/* ReadMostly: The following example shows how to maintain a scalable frequently read,
					but infrequently updated data structure using copy-on-write idiom.
package main

import (
	"sync"
	"sync/atomic"
)

func main() {
	type Map map[string]string
	var m atomic.Value
	m.Store(make(Map))
	var mu sync.Mutex // used only by writers
	// read function can be used to read the data without further synchronization
	read := func(key string) (val string) {
		m1 := m.Load().(Map)
		return m1[key]
	}
	// insert function can be used to update the data without further synchronization
	insert := func(key, val string) {
		mu.Lock() // synchronize with other potential writers
		defer mu.Unlock()
		m1 := m.Load().(Map) // load current value of the data structure
		m2 := make(Map)      // create a new value
		for k, v := range m1 {
			m2[k] = v // copy all data from the current object to the new one
		}
		m2[key] = val // do the update that we need
		m.Store(m2)   // atomically replace the current object with the new one
		// At this point all new readers start working with the new version.
		// The old version will be garbage collected once the existing readers
		// (if any) are done with it.
	}
	_, _ = read, insert
}
*/

// Load returns the value set by the most recent Store.
// It returns nil if there has been no call to Store for this Value.
func (v *Value) Load() (x interface{}) {}

// Store sets the value of the Value to x.
// All calls to Store for a given Value must use values of the same concrete type.
// Store of an inconsistent type panics, as does Store(nil).
func (v *Value) Store(x interface{}) {
	// possible: panic("sync/atomic: store of nil value into Value")
	// possible: panic("sync/atomic: store of inconsistently typed value into Value")
}
