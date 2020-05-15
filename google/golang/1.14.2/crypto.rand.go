// Copyright 2010 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package rand implements a cryptographically secure
// random number generator.
package rand // crypto/rand

import (
	"io"
	"math/big"
)

// Reader is a global, shared instance of a cryptographically
// secure random number generator.
//
// On Linux and FreeBSD, Reader uses getrandom(2) if available, /dev/urandom otherwise.
// On OpenBSD, Reader uses getentropy(2).
// On other Unix-like systems, Reader reads from /dev/urandom.
// On Windows systems, Reader uses the CryptGenRandom API.
// On Wasm, Reader uses the Web Crypto API.
var Reader io.Reader

// Read is a helper function that calls Reader.Read using io.ReadFull.
// On return, n == len(b) if and only if err == nil.
func Read(b []byte) (n int, err error) {}
/*
package main

import (
	"bytes"
	"crypto/rand"
	"fmt"
)

func main() {
	c := 10
	b := make([]byte, c)
	_, err := rand.Read(b)
	if err != nil {
		fmt.Println("error:", err)
		return
	}
	// The slice should now contain random bytes instead of only zeroes.
	fmt.Println(bytes.Equal(b, make([]byte, c)))

}
*/

// Prime returns a number, p, of the given size, such that p is prime
// with high probability.
// Prime will return error for any error returned by rand.Read or if bits < 2.
func Prime(rand io.Reader, bits int) (p *big.Int, err error) {}

// Int returns a uniform random value in [0, max). It panics if max <= 0.
func Int(rand io.Reader, max *big.Int) (n *big.Int, err error) {
	// possible: panic("crypto/rand: argument to Int is <= 0")
}
