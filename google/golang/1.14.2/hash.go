// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package hash provides interfaces for hash functions.
package hash

/* BinaryMarshaler
package main

import (
	"bytes"
	"crypto/sha256"
	"encoding"
	"fmt"
	"log"
)

func main() {
	const (
		input1 = "The tunneling gopher digs downwards, "
		input2 = "unaware of what he will find."
	)

	first := sha256.New()
	first.Write([]byte(input1))

	marshaler, ok := first.(encoding.BinaryMarshaler)
	if !ok {
		log.Fatal("first does not implement encoding.BinaryMarshaler")
	}
	state, err := marshaler.MarshalBinary()
	if err != nil {
		log.Fatal("unable to marshal hash:", err)
	}

	second := sha256.New()

	unmarshaler, ok := second.(encoding.BinaryUnmarshaler)
	if !ok {
		log.Fatal("second does not implement encoding.BinaryUnmarshaler")
	}
	if err := unmarshaler.UnmarshalBinary(state); err != nil {
		log.Fatal("unable to unmarshal hash:", err)
	}

	first.Write([]byte(input2))
	second.Write([]byte(input2))

	fmt.Printf("%x\n", first.Sum(nil))
	fmt.Println(bytes.Equal(first.Sum(nil), second.Sum(nil)))
}
*/

import "io"

// Hash is the common interface implemented by all hash functions.
//
// Hash implementations in the standard library (e.g. hash/crc32 and
// crypto/sha256) implement the encoding.BinaryMarshaler and
// encoding.BinaryUnmarshaler interfaces. Marshaling a hash implementation
// allows its internal state to be saved and used for additional processing
// later, without having to re-write the data previously written to the hash.
// The hash state may contain portions of the input in its original form,
// which users are expected to handle for any possible security implications.
//
// Compatibility: Any future changes to hash or crypto packages will endeavor
// to maintain compatibility with state encoded using previous versions.
// That is, any released versions of the packages should be able to
// decode data written with any previously released version,
// subject to issues such as security fixes.
// See the Go compatibility document for background: https://golang.org/doc/go1compat
type Hash interface {
	// Write (via the embedded io.Writer interface) adds more data to the running hash.
	// It never returns an error.
	io.Writer

	// Sum appends the current hash to b and returns the resulting slice.
	// It does not change the underlying hash state.
	Sum(b []byte) []byte

	// Reset resets the Hash to its initial state.
	Reset()

	// Size returns the number of bytes Sum will return.
	Size() int

	// BlockSize returns the hash's underlying block size.
	// The Write method must be able to accept any amount
	// of data, but it may operate more efficiently if all writes
	// are a multiple of the block size.
	BlockSize() int
}

// Hash32 is the common interface implemented by all 32-bit hash functions.
type Hash32 interface {
	Hash
	Sum32() uint32
}

// Hash64 is the common interface implemented by all 64-bit hash functions.
type Hash64 interface {
	Hash
	Sum64() uint64
}
