// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package crc32 implements the 32-bit cyclic redundancy check, or CRC-32,
// checksum. See https://en.wikipedia.org/wiki/Cyclic_redundancy_check for
// information.
//
// Polynomials are represented in LSB-first form also known as reversed representation.
//
// See https://en.wikipedia.org/wiki/Mathematics_of_cyclic_redundancy_checks#Reversed_representations_and_reciprocal_polynomials
// for information.
package crc32

import (
	"errors"
	"hash"
	"sync"
)

// The size of a CRC-32 checksum in bytes.
const Size = 4

// Predefined polynomials.
const (
	// IEEE is by far and away the most common CRC-32 polynomial.
	// Used by ethernet (IEEE 802.3), v.42, fddi, gzip, zip, png, ...
	IEEE = 0xedb88320

	// Castagnoli's polynomial, used in iSCSI.
	// Has better error detection characteristics than IEEE.
	// https://dx.doi.org/10.1109/26.231911
	Castagnoli = 0x82f63b78

	// Koopman's polynomial.
	// Also has better error detection characteristics than IEEE.
	// https://dx.doi.org/10.1109/DSN.2002.1028931
	Koopman = 0xeb31d82e
)

// Table is a 256-word table representing the polynomial for efficient processing.
type Table [256]uint32

// This file makes use of functions implemented in architecture-specific files.
// The interface that they implement is as follows:
//
//    // archAvailableIEEE reports whether an architecture-specific CRC32-IEEE
//    // algorithm is available.
//    archAvailableIEEE() bool
//
//    // archInitIEEE initializes the architecture-specific CRC3-IEEE algorithm.
//    // It can only be called if archAvailableIEEE() returns true.
//    archInitIEEE()
//
//    // archUpdateIEEE updates the given CRC32-IEEE. It can only be called if
//    // archInitIEEE() was previously called.
//    archUpdateIEEE(crc uint32, p []byte) uint32
//
//    // archAvailableCastagnoli reports whether an architecture-specific
//    // CRC32-C algorithm is available.
//    archAvailableCastagnoli() bool
//
//    // archInitCastagnoli initializes the architecture-specific CRC32-C
//    // algorithm. It can only be called if archAvailableCastagnoli() returns
//    // true.
//    archInitCastagnoli()
//
//    // archUpdateCastagnoli updates the given CRC32-C. It can only be called
//    // if archInitCastagnoli() was previously called.
//    archUpdateCastagnoli(crc uint32, p []byte) uint32

// IEEETable is the table for the IEEE polynomial.
var IEEETable *Table

// MakeTable returns a Table constructed from the specified polynomial.
// The contents of this Table must not be modified.
func MakeTable(poly uint32) *Table {}
/*
package main

import (
	"fmt"
	"hash/crc32"
)

func main() {
	// In this package, the CRC polynomial is represented in reversed notation,
	// or LSB-first representation.
	//
	// LSB-first representation is a hexadecimal number with n bits, in which the
	// most significant bit represents the coefficient of x⁰ and the least significant
	// bit represents the coefficient of xⁿ⁻¹ (the coefficient for xⁿ is implicit).
	//
	// For example, CRC32-Q, as defined by the following polynomial,
	//	x³²+ x³¹+ x²⁴+ x²²+ x¹⁶+ x¹⁴+ x⁸+ x⁷+ x⁵+ x³+ x¹+ x⁰
	// has the reversed notation 0b11010101100000101000001010000001, so the value
	// that should be passed to MakeTable is 0xD5828281.
	crc32q := crc32.MakeTable(0xD5828281)
	fmt.Printf("%08x\n", crc32.Checksum([]byte("Hello world"), crc32q))
}
*/

// New creates a new hash.Hash32 computing the CRC-32 checksum using the
// polynomial represented by the Table. Its Sum method will lay the
// value out in big-endian byte order. The returned Hash32 also
// implements encoding.BinaryMarshaler and encoding.BinaryUnmarshaler to
// marshal and unmarshal the internal state of the hash.
func New(tab *Table) hash.Hash32 {}

// NewIEEE creates a new hash.Hash32 computing the CRC-32 checksum using
// the IEEE polynomial. Its Sum method will lay the value out in
// big-endian byte order. The returned Hash32 also implements
// encoding.BinaryMarshaler and encoding.BinaryUnmarshaler to marshal
// and unmarshal the internal state of the hash.
func NewIEEE() hash.Hash32 {}

// Checksum returns the CRC-32 checksum of data
// using the polynomial represented by the Table.
func Checksum(data []byte, tab *Table) uint32 {}

// ChecksumIEEE returns the CRC-32 checksum of data
// using the IEEE polynomial.
func ChecksumIEEE(data []byte) uint32 {}
