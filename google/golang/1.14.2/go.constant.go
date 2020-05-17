// Copyright 2013 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package constant implements Values representing untyped
// Go constants and their corresponding operations.
//
// A special Unknown value may be used when a value
// is unknown due to an error. Operations on unknown
// values produce unknown values unless specified
// otherwise.
//
package constant

/*
package main

import (
	"fmt"
	"go/constant"
	"go/token"
)

func main() {
	// Create the complex number 2.3 + 5i.
	ar := constant.MakeFloat64(2.3)
	ai := constant.MakeImag(constant.MakeInt64(5))
	a := constant.BinaryOp(ar, token.ADD, ai)

	// Compute (2.3 + 5i) * 11.
	b := constant.MakeUint64(11)
	c := constant.BinaryOp(a, token.MUL, b)

	// Convert c into a complex128.
	Ar, exact := constant.Float64Val(constant.Real(c))
	if !exact {
		fmt.Printf("Could not represent real part %s exactly as float64\n", constant.Real(c))
	}
	Ai, exact := constant.Float64Val(constant.Imag(c))
	if !exact {
		fmt.Printf("Could not represent imaginary part %s as exactly as float64\n", constant.Imag(c))
	}
	C := complex(Ar, Ai)

	fmt.Println("literal", 25.3+55i)
	fmt.Println("go/constant", c)
	fmt.Println("complex128", C)

}
*/

import (
	"fmt"
	"go/token"
	"math"
	"math/big"
	"strconv"
	"strings"
	"sync"
	"unicode/utf8"
)

// Kind specifies the kind of value represented by a Value.
type Kind int

const (
	// unknown values
	Unknown Kind = iota

	// non-numeric values
	Bool
	String

	// numeric values
	Int
	Float
	Complex
)

// A Value represents the value of a Go constant.
type Value interface {
	// Kind returns the value kind.
	Kind() Kind

	// String returns a short, quoted (human-readable) form of the value.
	// For numeric values, the result may be an approximation;
	// for String values the result may be a shortened string.
	// Use ExactString for a string representing a value exactly.
	String() string

	// ExactString returns an exact, quoted (human-readable) form of the value.
	// If the Value is of Kind String, use StringVal to obtain the unquoted string.
	ExactString() string

	// Prevent external implementations.
	implementsValue()
}

// ----------------------------------------------------------------------------
// Accessors
//
// For unknown arguments the result is the zero value for the respective
// accessor type, except for Sign, where the result is 1.

// BoolVal returns the Go boolean value of x, which must be a Bool or an Unknown.
// If x is Unknown, the result is false.
func BoolVal(x Value) bool {
	// possible: panic(fmt.Sprintf("%v not a Bool", x))
}

// StringVal returns the Go string value of x, which must be a String or an Unknown.
// If x is Unknown, the result is "".
func StringVal(x Value) string {
	// possible: panic(fmt.Sprintf("%v not a String", x))
}

// Int64Val returns the Go int64 value of x and whether the result is exact;
// x must be an Int or an Unknown. If the result is not exact, its value is undefined.
// If x is Unknown, the result is (0, false).
func Int64Val(x Value) (int64, bool) {
	// possible: panic(fmt.Sprintf("%v not an Int", x))
}

// Uint64Val returns the Go uint64 value of x and whether the result is exact;
// x must be an Int or an Unknown. If the result is not exact, its value is undefined.
// If x is Unknown, the result is (0, false).
func Uint64Val(x Value) (uint64, bool) {
	// possible: panic(fmt.Sprintf("%v not an Int", x))
}

// Float32Val is like Float64Val but for float32 instead of float64.
func Float32Val(x Value) (float32, bool) {
	// possible: panic(fmt.Sprintf("%v not a Float", x))
}

// Float64Val returns the nearest Go float64 value of x and whether the result is exact;
// x must be numeric or an Unknown, but not Complex. For values too small (too close to 0)
// to represent as float64, Float64Val silently underflows to 0. The result sign always
// matches the sign of x, even for 0.
// If x is Unknown, the result is (0, false).
func Float64Val(x Value) (float64, bool) {
	// possible: panic(fmt.Sprintf("%v not a Float", x))
}

// Val returns the underlying value for a given constant. Since it returns an
// interface, it is up to the caller to type assert the result to the expected
// type. The possible dynamic return types are:
//
//    x Kind             type of result
//    -----------------------------------------
//    Bool               bool
//    String             string
//    Int                int64 or *big.Int
//    Float              *big.Float or *big.Rat
//    everything else    nil
//
func Val(x Value) interface{} {}
/*
package main

import (
	"fmt"
	"go/constant"
	"math"
)

func main() {
	maxint := constant.MakeInt64(math.MaxInt64)
	fmt.Printf("%v\n", constant.Val(maxint))

	e := constant.MakeFloat64(math.E)
	fmt.Printf("%v\n", constant.Val(e))

	b := constant.MakeBool(true)
	fmt.Printf("%v\n", constant.Val(b))

	b = constant.Make(false)
	fmt.Printf("%v\n", constant.Val(b))

}
*/

// Make returns the Value for x.
//
//    type of x        result Kind
//    ----------------------------
//    bool             Bool
//    string           String
//    int64            Int
//    *big.Int         Int
//    *big.Float       Float
//    *big.Rat         Float
//    anything else    Unknown
//
func Make(x interface{}) Value {}

// BitLen returns the number of bits required to represent
// the absolute value x in binary representation; x must be an Int or an Unknown.
// If x is Unknown, the result is 0.
func BitLen(x Value) int {	
	// possible: panic(fmt.Sprintf("%v not an Int", x))
}

// Sign returns -1, 0, or 1 depending on whether x < 0, x == 0, or x > 0;
// x must be numeric or Unknown. For complex values x, the sign is 0 if x == 0,
// otherwise it is != 0. If x is Unknown, the result is 1.
func Sign(x Value) int {
	// possible: panic(fmt.Sprintf("%v not numeric", x))
}
/*
package main

import (
	"fmt"
	"go/constant"
	"go/token"
)

func main() {
	zero := constant.MakeInt64(0)
	one := constant.MakeInt64(1)
	negOne := constant.MakeInt64(-1)

	mkComplex := func(a, b constant.Value) constant.Value {
		b = constant.MakeImag(b)
		return constant.BinaryOp(a, token.ADD, b)
	}

	vs := []constant.Value{
		negOne,
		mkComplex(zero, negOne),
		mkComplex(one, negOne),
		mkComplex(negOne, one),
		mkComplex(negOne, negOne),
		zero,
		mkComplex(zero, zero),
		one,
		mkComplex(zero, one),
		mkComplex(one, one),
	}

	for _, v := range vs {
		fmt.Printf("% d %s\n", constant.Sign(v), v)
	}

}
*/

// Bytes returns the bytes for the absolute value of x in little-
// endian binary representation; x must be an Int.
func Bytes(x Value) []byte {
	// possible: panic(fmt.Sprintf("%v not an Int", x))
}

// MakeFromBytes returns the Int value given the bytes of its little-endian
// binary representation. An empty byte slice argument represents 0.
func MakeFromBytes(bytes []byte) Value {}

// Num returns the numerator of x; x must be Int, Float, or Unknown.
// If x is Unknown, or if it is too large or small to represent as a
// fraction, the result is Unknown. Otherwise the result is an Int
// with the same sign as x.
func Num(x Value) Value {
	// possible: panic(fmt.Sprintf("%v not Int or Float", x))
}

// Denom returns the denominator of x; x must be Int, Float, or Unknown.
// If x is Unknown, or if it is too large or small to represent as a
// fraction, the result is Unknown. Otherwise the result is an Int >= 1.
func Denom(x Value) Value {
	// possible: panic(fmt.Sprintf("%v not Int or Float", x))
}

// MakeImag returns the Complex value x*i;
// x must be Int, Float, or Unknown.
// If x is Unknown, the result is Unknown.
func MakeImag(x Value) Value {
	// possible: panic(fmt.Sprintf("%v not Int or Float", x))
}

// Real returns the real part of x, which must be a numeric or unknown value.
// If x is Unknown, the result is Unknown.
func Real(x Value) Value {
	// possible: panic(fmt.Sprintf("%v not numeric", x))
}

// Imag returns the imaginary part of x, which must be a numeric or unknown value.
// If x is Unknown, the result is Unknown.
func Imag(x Value) Value {
	// possible: panic(fmt.Sprintf("%v not numeric", x))
}

// ----------------------------------------------------------------------------
// Numeric conversions

// ToInt converts x to an Int value if x is representable as an Int.
// Otherwise it returns an Unknown.
func ToInt(x Value) Value {}

// ToFloat converts x to a Float value if x is representable as a Float.
// Otherwise it returns an Unknown.
func ToFloat(x Value) Value {}

// ToComplex converts x to a Complex value if x is representable as a Complex.
// Otherwise it returns an Unknown.
func ToComplex(x Value) Value {}

// ----------------------------------------------------------------------------
// Operations

// UnaryOp returns the result of the unary expression op y.
// The operation must be defined for the operand.
// If prec > 0 it specifies the ^ (xor) result size in bits.
// If y is Unknown, the result is Unknown.
//
func UnaryOp(op token.Token, y Value, prec uint) Value {
	// possible: panic(fmt.Sprintf("invalid unary operation %s%v", op, y))
}
/*
package main

import (
	"fmt"
	"go/constant"
	"go/token"
)

func main() {
	vs := []constant.Value{
		constant.MakeBool(true),
		constant.MakeFloat64(2.7),
		constant.MakeUint64(42),
	}

	for i, v := range vs {
		switch v.Kind() {
		case constant.Bool:
			vs[i] = constant.UnaryOp(token.NOT, v, 0)

		case constant.Float:
			vs[i] = constant.UnaryOp(token.SUB, v, 0)

		case constant.Int:
			// Use 16-bit precision.
			// This would be equivalent to ^uint16(v).
			vs[i] = constant.UnaryOp(token.XOR, v, 16)
		}
	}

	for _, v := range vs {
		fmt.Println(v)
	}

}
*/

// BinaryOp returns the result of the binary expression x op y.
// The operation must be defined for the operands. If one of the
// operands is Unknown, the result is Unknown.
// BinaryOp doesn't handle comparisons or shifts; use Compare
// or Shift instead.
//
// To force integer division of Int operands, use op == token.QUO_ASSIGN
// instead of token.QUO; the result is guaranteed to be Int in this case.
// Division by zero leads to a run-time panic.
//
func BinaryOp(x_ Value, op token.Token, y_ Value) Value {
	// possible: panic(fmt.Sprintf("invalid binary operation %v %s %v", x_, op, y_))
}
/*
package main

import (
	"fmt"
	"go/constant"
	"go/token"
)

func main() {
	// 11 / 0.5
	a := constant.MakeUint64(11)
	b := constant.MakeFloat64(0.5)
	c := constant.BinaryOp(a, token.QUO, b)
	fmt.Println(c)

}
*/

// Shift returns the result of the shift expression x op s
// with op == token.SHL or token.SHR (<< or >>). x must be
// an Int or an Unknown. If x is Unknown, the result is x.
//
func Shift(x Value, op token.Token, s uint) Value {
	// possible: panic(fmt.Sprintf("invalid shift %v %s %d", x, op, s))
}

// Compare returns the result of the comparison x op y.
// The comparison must be defined for the operands.
// If one of the operands is Unknown, the result is
// false.
//
func Compare(x_ Value, op token.Token, y_ Value) bool {
	// possible: panic(fmt.Sprintf("invalid comparison %v %s %v", x_, op, y_))
}
/*
package main

import (
	"fmt"
	"go/constant"
	"go/token"
	"sort"
)

func main() {
	vs := []constant.Value{
		constant.MakeString("Z"),
		constant.MakeString("bacon"),
		constant.MakeString("go"),
		constant.MakeString("Frame"),
		constant.MakeString("defer"),
		constant.MakeFromLiteral(`"a"`, token.STRING, 0),
	}

	sort.Slice(vs, func(i, j int) bool {
		// Equivalent to vs[i] <= vs[j].
		return constant.Compare(vs[i], token.LEQ, vs[j])
	})

	for _, v := range vs {
		fmt.Println(constant.StringVal(v))
	}

}
*/
