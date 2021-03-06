// Copyright 2017 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

//go:generate go run make_tables.go

// Package bits implements bit counting and manipulation
// functions for the predeclared unsigned integer types.
package bits

// UintSize is the size of a uint in bits.
const UintSize = uintSize

// --- LeadingZeros ---

// LeadingZeros returns the number of leading zero bits in x; the result is UintSize for x == 0.
func LeadingZeros(x uint) int {}

// LeadingZeros8 returns the number of leading zero bits in x; the result is 8 for x == 0.
func LeadingZeros8(x uint8) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("LeadingZeros8(%08b) = %d\n", 1, bits.LeadingZeros8(1))
}
*/

// LeadingZeros16 returns the number of leading zero bits in x; the result is 16 for x == 0.
func LeadingZeros16(x uint16) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("LeadingZeros16(%016b) = %d\n", 1, bits.LeadingZeros16(1))
}
*/

// LeadingZeros32 returns the number of leading zero bits in x; the result is 32 for x == 0.
func LeadingZeros32(x uint32) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("LeadingZeros32(%032b) = %d\n", 1, bits.LeadingZeros32(1))
}
*/

// LeadingZeros64 returns the number of leading zero bits in x; the result is 64 for x == 0.
func LeadingZeros64(x uint64) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("LeadingZeros64(%064b) = %d\n", 1, bits.LeadingZeros64(1))
}
*/

// TrailingZeros returns the number of trailing zero bits in x; the result is UintSize for x == 0.
func TrailingZeros(x uint) int {}

// TrailingZeros8 returns the number of trailing zero bits in x; the result is 8 for x == 0.
func TrailingZeros8(x uint8) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("TrailingZeros8(%08b) = %d\n", 14, bits.TrailingZeros8(14))
}
*/

// TrailingZeros16 returns the number of trailing zero bits in x; the result is 16 for x == 0.
func TrailingZeros16(x uint16) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("TrailingZeros16(%016b) = %d\n", 14, bits.TrailingZeros16(14))
}
*/

// TrailingZeros32 returns the number of trailing zero bits in x; the result is 32 for x == 0.
func TrailingZeros32(x uint32) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("TrailingZeros32(%032b) = %d\n", 14, bits.TrailingZeros32(14))
}
*/

// TrailingZeros64 returns the number of trailing zero bits in x; the result is 64 for x == 0.
func TrailingZeros64(x uint64) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("TrailingZeros64(%064b) = %d\n", 14, bits.TrailingZeros64(14))
}
*/

// OnesCount returns the number of one bits ("population count") in x.
func OnesCount(x uint) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("OnesCount(%b) = %d\n", 14, bits.OnesCount(14))
}
*/

// OnesCount8 returns the number of one bits ("population count") in x.
func OnesCount8(x uint8) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("OnesCount8(%08b) = %d\n", 14, bits.OnesCount8(14))
}
*/

// OnesCount16 returns the number of one bits ("population count") in x.
func OnesCount16(x uint16) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("OnesCount16(%016b) = %d\n", 14, bits.OnesCount16(14))
}
*/

// OnesCount32 returns the number of one bits ("population count") in x.
func OnesCount32(x uint32) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("OnesCount32(%032b) = %d\n", 14, bits.OnesCount32(14))
}
*/

// OnesCount64 returns the number of one bits ("population count") in x.
func OnesCount64(x uint64) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("OnesCount64(%064b) = %d\n", 14, bits.OnesCount64(14))
}
*/

// --- RotateLeft ---

// RotateLeft returns the value of x rotated left by (k mod UintSize) bits.
// To rotate x right by k bits, call RotateLeft(x, -k).
//
// This function's execution time does not depend on the inputs.
func RotateLeft(x uint, k int) uint {}

// RotateLeft8 returns the value of x rotated left by (k mod 8) bits.
// To rotate x right by k bits, call RotateLeft8(x, -k).
//
// This function's execution time does not depend on the inputs.
func RotateLeft8(x uint8, k int) uint8 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%08b\n", 15)
	fmt.Printf("%08b\n", bits.RotateLeft8(15, 2))
	fmt.Printf("%08b\n", bits.RotateLeft8(15, -2))
}
*/

// RotateLeft16 returns the value of x rotated left by (k mod 16) bits.
// To rotate x right by k bits, call RotateLeft16(x, -k).
//
// This function's execution time does not depend on the inputs.
func RotateLeft16(x uint16, k int) uint16 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%016b\n", 15)
	fmt.Printf("%016b\n", bits.RotateLeft16(15, 2))
	fmt.Printf("%016b\n", bits.RotateLeft16(15, -2))
}
*/

// RotateLeft32 returns the value of x rotated left by (k mod 32) bits.
// To rotate x right by k bits, call RotateLeft32(x, -k).
//
// This function's execution time does not depend on the inputs.
func RotateLeft32(x uint32, k int) uint32 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%032b\n", 15)
	fmt.Printf("%032b\n", bits.RotateLeft32(15, 2))
	fmt.Printf("%032b\n", bits.RotateLeft32(15, -2))
}
*/

// RotateLeft64 returns the value of x rotated left by (k mod 64) bits.
// To rotate x right by k bits, call RotateLeft64(x, -k).
//
// This function's execution time does not depend on the inputs.
func RotateLeft64(x uint64, k int) uint64 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%064b\n", 15)
	fmt.Printf("%064b\n", bits.RotateLeft64(15, 2))
	fmt.Printf("%064b\n", bits.RotateLeft64(15, -2))
}
*/

// --- Reverse ---

// Reverse returns the value of x with its bits in reversed order.
func Reverse(x uint) uint {}

// Reverse8 returns the value of x with its bits in reversed order.
func Reverse8(x uint8) uint8 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%08b\n", 19)
	fmt.Printf("%08b\n", bits.Reverse8(19))
}
*/

// Reverse16 returns the value of x with its bits in reversed order.
func Reverse16(x uint16) uint16 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%016b\n", 19)
	fmt.Printf("%016b\n", bits.Reverse16(19))
}
*/

// Reverse32 returns the value of x with its bits in reversed order.
func Reverse32(x uint32) uint32 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%032b\n", 19)
	fmt.Printf("%032b\n", bits.Reverse32(19))
}
*/

// Reverse64 returns the value of x with its bits in reversed order.
func Reverse64(x uint64) uint64 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%064b\n", 19)
	fmt.Printf("%064b\n", bits.Reverse64(19))
}
*/

// --- ReverseBytes ---

// ReverseBytes returns the value of x with its bytes in reversed order.
//
// This function's execution time does not depend on the inputs.
func ReverseBytes(x uint) uint {}

// ReverseBytes16 returns the value of x with its bytes in reversed order.
//
// This function's execution time does not depend on the inputs.
func ReverseBytes16(x uint16) uint16 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%016b\n", 15)
	fmt.Printf("%016b\n", bits.ReverseBytes16(15))
}
*/

// ReverseBytes32 returns the value of x with its bytes in reversed order.
//
// This function's execution time does not depend on the inputs.
func ReverseBytes32(x uint32) uint32 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%032b\n", 15)
	fmt.Printf("%032b\n", bits.ReverseBytes32(15))
}
*/

// ReverseBytes64 returns the value of x with its bytes in reversed order.
//
// This function's execution time does not depend on the inputs.
func ReverseBytes64(x uint64) uint64 {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("%064b\n", 15)
	fmt.Printf("%064b\n", bits.ReverseBytes64(15))
}
*/

// --- Len ---

// Len returns the minimum number of bits required to represent x; the result is 0 for x == 0.
func Len(x uint) int {}

// Len8 returns the minimum number of bits required to represent x; the result is 0 for x == 0.
func Len8(x uint8) int {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("Len8(%08b) = %d\n", 8, bits.Len8(8))
}
*/

// Len16 returns the minimum number of bits required to represent x; the result is 0 for x == 0.
func Len16(x uint16) (n int) {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("Len16(%016b) = %d\n", 8, bits.Len16(8))
}
*/

// Len32 returns the minimum number of bits required to represent x; the result is 0 for x == 0.
func Len32(x uint32) (n int) {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("Len32(%032b) = %d\n", 8, bits.Len32(8))
}
*/

// Len64 returns the minimum number of bits required to represent x; the result is 0 for x == 0.
func Len64(x uint64) (n int) {}
/*
package main

import (
	"fmt"
	"math/bits"
)

func main() {
	fmt.Printf("Len64(%064b) = %d\n", 8, bits.Len64(8))
}
*/

// --- Add with carry ---

// Add returns the sum with carry of x, y and carry: sum = x + y + carry.
// The carry input must be 0 or 1; otherwise the behavior is undefined.
// The carryOut output is guaranteed to be 0 or 1.
//
// This function's execution time does not depend on the inputs.
func Add(x, y, carry uint) (sum, carryOut uint) {}

// Add32 returns the sum with carry of x, y and carry: sum = x + y + carry.
// The carry input must be 0 or 1; otherwise the behavior is undefined.
// The carryOut output is guaranteed to be 0 or 1.
//
// This function's execution time does not depend on the inputs.
func Add32(x, y, carry uint32) (sum, carryOut uint32) {}

// Add64 returns the sum with carry of x, y and carry: sum = x + y + carry.
// The carry input must be 0 or 1; otherwise the behavior is undefined.
// The carryOut output is guaranteed to be 0 or 1.
//
// This function's execution time does not depend on the inputs.
func Add64(x, y, carry uint64) (sum, carryOut uint64) {}

// --- Subtract with borrow ---

// Sub returns the difference of x, y and borrow: diff = x - y - borrow.
// The borrow input must be 0 or 1; otherwise the behavior is undefined.
// The borrowOut output is guaranteed to be 0 or 1.
//
// This function's execution time does not depend on the inputs.
func Sub(x, y, borrow uint) (diff, borrowOut uint) {}

// Sub32 returns the difference of x, y and borrow, diff = x - y - borrow.
// The borrow input must be 0 or 1; otherwise the behavior is undefined.
// The borrowOut output is guaranteed to be 0 or 1.
//
// This function's execution time does not depend on the inputs.
func Sub32(x, y, borrow uint32) (diff, borrowOut uint32) {}

// Sub64 returns the difference of x, y and borrow: diff = x - y - borrow.
// The borrow input must be 0 or 1; otherwise the behavior is undefined.
// The borrowOut output is guaranteed to be 0 or 1.
//
// This function's execution time does not depend on the inputs.
func Sub64(x, y, borrow uint64) (diff, borrowOut uint64) {}

// --- Full-width multiply ---

// Mul returns the full-width product of x and y: (hi, lo) = x * y
// with the product bits' upper half returned in hi and the lower
// half returned in lo.
//
// This function's execution time does not depend on the inputs.
func Mul(x, y uint) (hi, lo uint) {}

// Mul32 returns the 64-bit product of x and y: (hi, lo) = x * y
// with the product bits' upper half returned in hi and the lower
// half returned in lo.
//
// This function's execution time does not depend on the inputs.
func Mul32(x, y uint32) (hi, lo uint32) {}

// Mul64 returns the 128-bit product of x and y: (hi, lo) = x * y
// with the product bits' upper half returned in hi and the lower
// half returned in lo.
//
// This function's execution time does not depend on the inputs.
func Mul64(x, y uint64) (hi, lo uint64) {}

// --- Full-width divide ---

// Div returns the quotient and remainder of (hi, lo) divided by y:
// quo = (hi, lo)/y, rem = (hi, lo)%y with the dividend bits' upper
// half in parameter hi and the lower half in parameter lo.
// Div panics for y == 0 (division by zero) or y <= hi (quotient overflow).
func Div(hi, lo, y uint) (quo, rem uint) {}

// Div32 returns the quotient and remainder of (hi, lo) divided by y:
// quo = (hi, lo)/y, rem = (hi, lo)%y with the dividend bits' upper
// half in parameter hi and the lower half in parameter lo.
// Div32 panics for y == 0 (division by zero) or y <= hi (quotient overflow).
func Div32(hi, lo, y uint32) (quo, rem uint32) {}

// Div64 returns the quotient and remainder of (hi, lo) divided by y:
// quo = (hi, lo)/y, rem = (hi, lo)%y with the dividend bits' upper
// half in parameter hi and the lower half in parameter lo.
// Div64 panics for y == 0 (division by zero) or y <= hi (quotient overflow).
func Div64(hi, lo, y uint64) (quo, rem uint64) {}

// Rem returns the remainder of (hi, lo) divided by y. Rem panics for
// y == 0 (division by zero) but, unlike Div, it doesn't panic on a
// quotient overflow.
func Rem(hi, lo, y uint) uint {}

// Rem32 returns the remainder of (hi, lo) divided by y. Rem32 panics
// for y == 0 (division by zero) but, unlike Div32, it doesn't panic
// on a quotient overflow.
func Rem32(hi, lo, y uint32) uint32 {}

// Rem64 returns the remainder of (hi, lo) divided by y. Rem64 panics
// for y == 0 (division by zero) but, unlike Div64, it doesn't panic
// on a quotient overflow.
func Rem64(hi, lo, y uint64) uint64 {}
