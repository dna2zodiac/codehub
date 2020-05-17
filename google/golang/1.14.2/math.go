// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package math provides basic constants and mathematical functions.
//
// This package does not guarantee bit-identical results across architectures.
package math

// Mathematical constants.
const (
	E   = 2.71828182845904523536028747135266249775724709369995957496696763 // https://oeis.org/A001113
	Pi  = 3.14159265358979323846264338327950288419716939937510582097494459 // https://oeis.org/A000796
	Phi = 1.61803398874989484820458683436563811772030917980576286213544862 // https://oeis.org/A001622

	Sqrt2   = 1.41421356237309504880168872420969807856967187537694807317667974 // https://oeis.org/A002193
	SqrtE   = 1.64872127070012814684865078781416357165377610071014801157507931 // https://oeis.org/A019774
	SqrtPi  = 1.77245385090551602729816748334114518279754945612238712821380779 // https://oeis.org/A002161
	SqrtPhi = 1.27201964951406896425242246173749149171560804184009624861664038 // https://oeis.org/A139339

	Ln2    = 0.693147180559945309417232121458176568075500134360255254120680009 // https://oeis.org/A002162
	Log2E  = 1 / Ln2
	Ln10   = 2.30258509299404568401799145468436420760110148862877297603332790 // https://oeis.org/A002392
	Log10E = 1 / Ln10
)

// Floating-point limit values.
// Max is the largest finite value representable by the type.
// SmallestNonzero is the smallest positive, non-zero value representable by the type.
const (
	MaxFloat32             = 3.40282346638528859811704183484516925440e+38  // 2**127 * (2**24 - 1) / 2**23
	SmallestNonzeroFloat32 = 1.401298464324817070923729583289916131280e-45 // 1 / 2**(127 - 1 + 23)

	MaxFloat64             = 1.797693134862315708145274237317043567981e+308 // 2**1023 * (2**53 - 1) / 2**52
	SmallestNonzeroFloat64 = 4.940656458412465441765687928682213723651e-324 // 1 / 2**(1023 - 1 + 52)
)

// Integer limit values.
const (
	MaxInt8   = 1<<7 - 1
	MinInt8   = -1 << 7
	MaxInt16  = 1<<15 - 1
	MinInt16  = -1 << 15
	MaxInt32  = 1<<31 - 1
	MinInt32  = -1 << 31
	MaxInt64  = 1<<63 - 1
	MinInt64  = -1 << 63
	MaxUint8  = 1<<8 - 1
	MaxUint16 = 1<<16 - 1
	MaxUint32 = 1<<32 - 1
	MaxUint64 = 1<<64 - 1
)

// Abs returns the absolute value of x.
//
// Special cases are:
//	Abs(±Inf) = +Inf
//	Abs(NaN) = NaN
func Abs(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	x := math.Abs(-2)
	fmt.Printf("%.1f\n", x)

	y := math.Abs(2)
	fmt.Printf("%.1f\n", y)
}
*/

// The original C code, the long comment, and the constants
// below are from FreeBSD's /usr/src/lib/msun/src/e_acosh.c
// and came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
//
// __ieee754_acosh(x)
// Method :
//	Based on
//	        acosh(x) = log [ x + sqrt(x*x-1) ]
//	we have
//	        acosh(x) := log(x)+ln2,	if x is large; else
//	        acosh(x) := log(2x-1/(sqrt(x*x-1)+x)) if x>2; else
//	        acosh(x) := log1p(t+sqrt(2.0*t+t*t)); where t=x-1.
//
// Special cases:
//	acosh(x) is NaN with signal if x<1.
//	acosh(NaN) is NaN without signal.
//

// Acosh returns the inverse hyperbolic cosine of x.
//
// Special cases are:
//	Acosh(+Inf) = +Inf
//	Acosh(x) = NaN if x < 1
//	Acosh(NaN) = NaN
func Acosh(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Acosh(1))
}
*/

/*
	Floating-point arcsine and arccosine.

	They are implemented by computing the arctangent
	after appropriate range reduction.
*/

// Asin returns the arcsine, in radians, of x.
//
// Special cases are:
//	Asin(±0) = ±0
//	Asin(x) = NaN if x < -1 or x > 1
func Asin(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Asin(0))
}
*/

// Acos returns the arccosine, in radians, of x.
//
// Special case is:
//	Acos(x) = NaN if x < -1 or x > 1
func Acos(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Acos(1))
}
*/

// The original C code, the long comment, and the constants
// below are from FreeBSD's /usr/src/lib/msun/src/s_asinh.c
// and came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
//
// asinh(x)
// Method :
//	Based on
//	        asinh(x) = sign(x) * log [ |x| + sqrt(x*x+1) ]
//	we have
//	asinh(x) := x  if  1+x*x=1,
//	         := sign(x)*(log(x)+ln2)) for large |x|, else
//	         := sign(x)*log(2|x|+1/(|x|+sqrt(x*x+1))) if|x|>2, else
//	         := sign(x)*log1p(|x| + x**2/(1 + sqrt(1+x**2)))
//

// Asinh returns the inverse hyperbolic sine of x.
//
// Special cases are:
//	Asinh(±0) = ±0
//	Asinh(±Inf) = ±Inf
//	Asinh(NaN) = NaN
func Asinh(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Asinh(0))
}
*/

/*
	Floating-point arctangent.
*/

// The original C code, the long comment, and the constants below were
// from http://netlib.sandia.gov/cephes/cmath/atan.c, available from
// http://www.netlib.org/cephes/cmath.tgz.
// The go code is a version of the original C.
//
// atan.c
// Inverse circular tangent (arctangent)
//
// SYNOPSIS:
// double x, y, atan();
// y = atan( x );
//
// DESCRIPTION:
// Returns radian angle between -pi/2 and +pi/2 whose tangent is x.
//
// Range reduction is from three intervals into the interval from zero to 0.66.
// The approximant uses a rational function of degree 4/5 of the form
// x + x**3 P(x)/Q(x).
//
// ACCURACY:
//                      Relative error:
// arithmetic   domain    # trials  peak     rms
//    DEC       -10, 10   50000     2.4e-17  8.3e-18
//    IEEE      -10, 10   10^6      1.8e-16  5.0e-17
//
// Cephes Math Library Release 2.8:  June, 2000
// Copyright 1984, 1987, 1989, 1992, 2000 by Stephen L. Moshier
//
// The readme file at http://netlib.sandia.gov/cephes/ says:
//    Some software in this archive may be from the book _Methods and
// Programs for Mathematical Functions_ (Prentice-Hall or Simon & Schuster
// International, 1989) or from the Cephes Mathematical Library, a
// commercial product. In either event, it is copyrighted by the author.
// What you see here may be used freely but it comes with no support or
// guarantee.
//
//   The two known misprints in the book are repaired here in the
// source listings for the gamma function and the incomplete beta
// integral.
//
//   Stephen L. Moshier
//   moshier@na-net.ornl.gov

// Atan returns the arctangent, in radians, of x.
//
// Special cases are:
//      Atan(±0) = ±0
//      Atan(±Inf) = ±Pi/2
func Atan(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Atan(0))
}
*/

// Atan2 returns the arc tangent of y/x, using
// the signs of the two to determine the quadrant
// of the return value.
//
// Special cases are (in order):
//	Atan2(y, NaN) = NaN
//	Atan2(NaN, x) = NaN
//	Atan2(+0, x>=0) = +0
//	Atan2(-0, x>=0) = -0
//	Atan2(+0, x<=-0) = +Pi
//	Atan2(-0, x<=-0) = -Pi
//	Atan2(y>0, 0) = +Pi/2
//	Atan2(y<0, 0) = -Pi/2
//	Atan2(+Inf, +Inf) = +Pi/4
//	Atan2(-Inf, +Inf) = -Pi/4
//	Atan2(+Inf, -Inf) = 3Pi/4
//	Atan2(-Inf, -Inf) = -3Pi/4
//	Atan2(y, +Inf) = 0
//	Atan2(y>0, -Inf) = +Pi
//	Atan2(y<0, -Inf) = -Pi
//	Atan2(+Inf, x) = +Pi/2
//	Atan2(-Inf, x) = -Pi/2
func Atan2(y, x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Atan2(0, 0))
}
*/

// The original C code, the long comment, and the constants
// below are from FreeBSD's /usr/src/lib/msun/src/e_atanh.c
// and came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
//
// __ieee754_atanh(x)
// Method :
//	1. Reduce x to positive by atanh(-x) = -atanh(x)
//	2. For x>=0.5
//	            1              2x                          x
//	atanh(x) = --- * log(1 + -------) = 0.5 * log1p(2 * --------)
//	            2             1 - x                      1 - x
//
//	For x<0.5
//	atanh(x) = 0.5*log1p(2x+2x*x/(1-x))
//
// Special cases:
//	atanh(x) is NaN if |x| > 1 with signal;
//	atanh(NaN) is that NaN with no signal;
//	atanh(+-1) is +-INF with signal.
//

// Atanh returns the inverse hyperbolic tangent of x.
//
// Special cases are:
//	Atanh(1) = +Inf
//	Atanh(±0) = ±0
//	Atanh(-1) = -Inf
//	Atanh(x) = NaN if x < -1 or x > 1
//	Atanh(NaN) = NaN
func Atanh(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Atanh(0))
}
*/

// Inf returns positive infinity if sign >= 0, negative infinity if sign < 0.
func Inf(sign int) float64 {}

// NaN returns an IEEE 754 ``not-a-number'' value.
func NaN() float64 {}

// IsNaN reports whether f is an IEEE 754 ``not-a-number'' value.
func IsNaN(f float64) (is bool) {}

// IsInf reports whether f is an infinity, according to sign.
// If sign > 0, IsInf reports whether f is positive infinity.
// If sign < 0, IsInf reports whether f is negative infinity.
// If sign == 0, IsInf reports whether f is either infinity.
func IsInf(f float64, sign int) bool {}

// The go code is a modified version of the original C code from
// http://www.netlib.org/fdlibm/s_cbrt.c and came with this notice.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunSoft, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================

// Cbrt returns the cube root of x.
//
// Special cases are:
//	Cbrt(±0) = ±0
//	Cbrt(±Inf) = ±Inf
//	Cbrt(NaN) = NaN
func Cbrt(x float64) float64 {}


// Copysign returns a value with the magnitude
// of x and the sign of y.
func Copysign(x, y float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Copysign(3.2, -1))
}
*/

// Dim returns the maximum of x-y or 0.
//
// Special cases are:
//	Dim(+Inf, +Inf) = NaN
//	Dim(-Inf, -Inf) = NaN
//	Dim(x, NaN) = Dim(NaN, x) = NaN
func Dim(x, y float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f\n", math.Dim(4, -2))
	fmt.Printf("%.2f\n", math.Dim(-4, 2))
}
*/

// Max returns the larger of x or y.
//
// Special cases are:
//	Max(x, +Inf) = Max(+Inf, x) = +Inf
//	Max(x, NaN) = Max(NaN, x) = NaN
//	Max(+0, ±0) = Max(±0, +0) = +0
//	Max(-0, -0) = -0
func Max(x, y float64) float64 {}

// Min returns the smaller of x or y.
//
// Special cases are:
//	Min(x, -Inf) = Min(-Inf, x) = -Inf
//	Min(x, NaN) = Min(NaN, x) = NaN
//	Min(-0, ±0) = Min(±0, -0) = -0
func Min(x, y float64) float64 {}

/*
	Floating-point error function and complementary error function.
*/

// The original C code and the long comment below are
// from FreeBSD's /usr/src/lib/msun/src/s_erf.c and
// came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
//
// double erf(double x)
// double erfc(double x)
//                           x
//                    2      |\
//     erf(x)  =  ---------  | exp(-t*t)dt
//                 sqrt(pi) \|
//                           0
//
//     erfc(x) =  1-erf(x)
//  Note that
//              erf(-x) = -erf(x)
//              erfc(-x) = 2 - erfc(x)
//
// Method:
//      1. For |x| in [0, 0.84375]
//          erf(x)  = x + x*R(x**2)
//          erfc(x) = 1 - erf(x)           if x in [-.84375,0.25]
//                  = 0.5 + ((0.5-x)-x*R)  if x in [0.25,0.84375]
//         where R = P/Q where P is an odd poly of degree 8 and
//         Q is an odd poly of degree 10.
//                                               -57.90
//                      | R - (erf(x)-x)/x | <= 2
//
//
//         Remark. The formula is derived by noting
//          erf(x) = (2/sqrt(pi))*(x - x**3/3 + x**5/10 - x**7/42 + ....)
//         and that
//          2/sqrt(pi) = 1.128379167095512573896158903121545171688
//         is close to one. The interval is chosen because the fix
//         point of erf(x) is near 0.6174 (i.e., erf(x)=x when x is
//         near 0.6174), and by some experiment, 0.84375 is chosen to
//         guarantee the error is less than one ulp for erf.
//
//      2. For |x| in [0.84375,1.25], let s = |x| - 1, and
//         c = 0.84506291151 rounded to single (24 bits)
//              erf(x)  = sign(x) * (c  + P1(s)/Q1(s))
//              erfc(x) = (1-c)  - P1(s)/Q1(s) if x > 0
//                        1+(c+P1(s)/Q1(s))    if x < 0
//              |P1/Q1 - (erf(|x|)-c)| <= 2**-59.06
//         Remark: here we use the taylor series expansion at x=1.
//              erf(1+s) = erf(1) + s*Poly(s)
//                       = 0.845.. + P1(s)/Q1(s)
//         That is, we use rational approximation to approximate
//                      erf(1+s) - (c = (single)0.84506291151)
//         Note that |P1/Q1|< 0.078 for x in [0.84375,1.25]
//         where
//              P1(s) = degree 6 poly in s
//              Q1(s) = degree 6 poly in s
//
//      3. For x in [1.25,1/0.35(~2.857143)],
//              erfc(x) = (1/x)*exp(-x*x-0.5625+R1/S1)
//              erf(x)  = 1 - erfc(x)
//         where
//              R1(z) = degree 7 poly in z, (z=1/x**2)
//              S1(z) = degree 8 poly in z
//
//      4. For x in [1/0.35,28]
//              erfc(x) = (1/x)*exp(-x*x-0.5625+R2/S2) if x > 0
//                      = 2.0 - (1/x)*exp(-x*x-0.5625+R2/S2) if -6<x<0
//                      = 2.0 - tiny            (if x <= -6)
//              erf(x)  = sign(x)*(1.0 - erfc(x)) if x < 6, else
//              erf(x)  = sign(x)*(1.0 - tiny)
//         where
//              R2(z) = degree 6 poly in z, (z=1/x**2)
//              S2(z) = degree 7 poly in z
//
//      Note1:
//         To compute exp(-x*x-0.5625+R/S), let s be a single
//         precision number and s := x; then
//              -x*x = -s*s + (s-x)*(s+x)
//              exp(-x*x-0.5626+R/S) =
//                      exp(-s*s-0.5625)*exp((s-x)*(s+x)+R/S);
//      Note2:
//         Here 4 and 5 make use of the asymptotic series
//                        exp(-x*x)
//              erfc(x) ~ ---------- * ( 1 + Poly(1/x**2) )
//                        x*sqrt(pi)
//         We use rational approximation to approximate
//              g(s)=f(1/x**2) = log(erfc(x)*x) - x*x + 0.5625
//         Here is the error bound for R1/S1 and R2/S2
//              |R1/S1 - f(x)|  < 2**(-62.57)
//              |R2/S2 - f(x)|  < 2**(-61.52)
//
//      5. For inf > x >= 28
//              erf(x)  = sign(x) *(1 - tiny)  (raise inexact)
//              erfc(x) = tiny*tiny (raise underflow) if x > 0
//                      = 2 - tiny if x<0
//
//      7. Special case:
//              erf(0)  = 0, erf(inf)  = 1, erf(-inf) = -1,
//              erfc(0) = 1, erfc(inf) = 0, erfc(-inf) = 2,
//              erfc/erf(NaN) is NaN

// Erf returns the error function of x.
//
// Special cases are:
//	Erf(+Inf) = 1
//	Erf(-Inf) = -1
//	Erf(NaN) = NaN
func Erf(x float64) float64 {}

// Erfc returns the complementary error function of x.
//
// Special cases are:
//	Erfc(+Inf) = 0
//	Erfc(-Inf) = 2
//	Erfc(NaN) = NaN
func Erfc(x float64) float64 {}

/*
	Inverse of the floating-point error function.
*/

// This implementation is based on the rational approximation
// of percentage points of normal distribution available from
// https://www.jstor.org/stable/2347330.

// Erfinv returns the inverse error function of x.
//
// Special cases are:
//	Erfinv(1) = +Inf
//	Erfinv(-1) = -Inf
//	Erfinv(x) = NaN if x < -1 or x > 1
//	Erfinv(NaN) = NaN
func Erfinv(x float64) float64 {}

// Erfcinv returns the inverse of Erfc(x).
//
// Special cases are:
//	Erfcinv(0) = +Inf
//	Erfcinv(2) = -Inf
//	Erfcinv(x) = NaN if x < 0 or x > 2
//	Erfcinv(NaN) = NaN
func Erfcinv(x float64) float64 {}

// Exp returns e**x, the base-e exponential of x.
//
// Special cases are:
//	Exp(+Inf) = +Inf
//	Exp(NaN) = NaN
// Very large values overflow to 0 or +Inf.
// Very small values underflow to 1.
func Exp(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f\n", math.Exp(1))
	fmt.Printf("%.2f\n", math.Exp(2))
	fmt.Printf("%.2f\n", math.Exp(-1))
}
*/

// The original C code, the long comment, and the constants
// below are from FreeBSD's /usr/src/lib/msun/src/e_exp.c
// and came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 2004 by Sun Microsystems, Inc. All rights reserved.
//
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
//
// exp(x)
// Returns the exponential of x.
//
// Method
//   1. Argument reduction:
//      Reduce x to an r so that |r| <= 0.5*ln2 ~ 0.34658.
//      Given x, find r and integer k such that
//
//               x = k*ln2 + r,  |r| <= 0.5*ln2.
//
//      Here r will be represented as r = hi-lo for better
//      accuracy.
//
//   2. Approximation of exp(r) by a special rational function on
//      the interval [0,0.34658]:
//      Write
//          R(r**2) = r*(exp(r)+1)/(exp(r)-1) = 2 + r*r/6 - r**4/360 + ...
//      We use a special Remez algorithm on [0,0.34658] to generate
//      a polynomial of degree 5 to approximate R. The maximum error
//      of this polynomial approximation is bounded by 2**-59. In
//      other words,
//          R(z) ~ 2.0 + P1*z + P2*z**2 + P3*z**3 + P4*z**4 + P5*z**5
//      (where z=r*r, and the values of P1 to P5 are listed below)
//      and
//          |                  5          |     -59
//          | 2.0+P1*z+...+P5*z   -  R(z) | <= 2
//          |                             |
//      The computation of exp(r) thus becomes
//                             2*r
//              exp(r) = 1 + -------
//                            R - r
//                                 r*R1(r)
//                     = 1 + r + ----------- (for better accuracy)
//                                2 - R1(r)
//      where
//                               2       4             10
//              R1(r) = r - (P1*r  + P2*r  + ... + P5*r   ).
//
//   3. Scale back to obtain exp(x):
//      From step 1, we have
//         exp(x) = 2**k * exp(r)
//
// Special cases:
//      exp(INF) is INF, exp(NaN) is NaN;
//      exp(-INF) is 0, and
//      for finite argument, only exp(0)=1 is exact.
//
// Accuracy:
//      according to an error analysis, the error is always less than
//      1 ulp (unit in the last place).
//
// Misc. info.
//      For IEEE double
//          if x >  7.09782712893383973096e+02 then exp(x) overflow
//          if x < -7.45133219101941108420e+02 then exp(x) underflow
//
// Constants:
// The hexadecimal values are the intended ones for the following
// constants. The decimal values may be used, provided that the
// compiler will convert from decimal to binary accurately enough
// to produce the hexadecimal values shown.

// Exp2 returns 2**x, the base-2 exponential of x.
//
// Special cases are the same as Exp.
func Exp2(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f\n", math.Exp2(1))
	fmt.Printf("%.2f\n", math.Exp2(-3))
}
*/

// The original C code, the long comment, and the constants
// below are from FreeBSD's /usr/src/lib/msun/src/s_expm1.c
// and came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// expm1(x)
// Returns exp(x)-1, the exponential of x minus 1.
//
// Method
//   1. Argument reduction:
//      Given x, find r and integer k such that
//
//               x = k*ln2 + r,  |r| <= 0.5*ln2 ~ 0.34658
//
//      Here a correction term c will be computed to compensate
//      the error in r when rounded to a floating-point number.
//
//   2. Approximating expm1(r) by a special rational function on
//      the interval [0,0.34658]:
//      Since
//          r*(exp(r)+1)/(exp(r)-1) = 2+ r**2/6 - r**4/360 + ...
//      we define R1(r*r) by
//          r*(exp(r)+1)/(exp(r)-1) = 2+ r**2/6 * R1(r*r)
//      That is,
//          R1(r**2) = 6/r *((exp(r)+1)/(exp(r)-1) - 2/r)
//                   = 6/r * ( 1 + 2.0*(1/(exp(r)-1) - 1/r))
//                   = 1 - r**2/60 + r**4/2520 - r**6/100800 + ...
//      We use a special Reme algorithm on [0,0.347] to generate
//      a polynomial of degree 5 in r*r to approximate R1. The
//      maximum error of this polynomial approximation is bounded
//      by 2**-61. In other words,
//          R1(z) ~ 1.0 + Q1*z + Q2*z**2 + Q3*z**3 + Q4*z**4 + Q5*z**5
//      where   Q1  =  -1.6666666666666567384E-2,
//              Q2  =   3.9682539681370365873E-4,
//              Q3  =  -9.9206344733435987357E-6,
//              Q4  =   2.5051361420808517002E-7,
//              Q5  =  -6.2843505682382617102E-9;
//      (where z=r*r, and the values of Q1 to Q5 are listed below)
//      with error bounded by
//          |                  5           |     -61
//          | 1.0+Q1*z+...+Q5*z   -  R1(z) | <= 2
//          |                              |
//
//      expm1(r) = exp(r)-1 is then computed by the following
//      specific way which minimize the accumulation rounding error:
//                             2     3
//                            r     r    [ 3 - (R1 + R1*r/2)  ]
//            expm1(r) = r + --- + --- * [--------------------]
//                            2     2    [ 6 - r*(3 - R1*r/2) ]
//
//      To compensate the error in the argument reduction, we use
//              expm1(r+c) = expm1(r) + c + expm1(r)*c
//                         ~ expm1(r) + c + r*c
//      Thus c+r*c will be added in as the correction terms for
//      expm1(r+c). Now rearrange the term to avoid optimization
//      screw up:
//                      (      2                                    2 )
//                      ({  ( r    [ R1 -  (3 - R1*r/2) ]  )  }    r  )
//       expm1(r+c)~r - ({r*(--- * [--------------------]-c)-c} - --- )
//                      ({  ( 2    [ 6 - r*(3 - R1*r/2) ]  )  }    2  )
//                      (                                             )
//
//                 = r - E
//   3. Scale back to obtain expm1(x):
//      From step 1, we have
//         expm1(x) = either 2**k*[expm1(r)+1] - 1
//                  = or     2**k*[expm1(r) + (1-2**-k)]
//   4. Implementation notes:
//      (A). To save one multiplication, we scale the coefficient Qi
//           to Qi*2**i, and replace z by (x**2)/2.
//      (B). To achieve maximum accuracy, we compute expm1(x) by
//        (i)   if x < -56*ln2, return -1.0, (raise inexact if x!=inf)
//        (ii)  if k=0, return r-E
//        (iii) if k=-1, return 0.5*(r-E)-0.5
//        (iv)  if k=1 if r < -0.25, return 2*((r+0.5)- E)
//                     else          return  1.0+2.0*(r-E);
//        (v)   if (k<-2||k>56) return 2**k(1-(E-r)) - 1 (or exp(x)-1)
//        (vi)  if k <= 20, return 2**k((1-2**-k)-(E-r)), else
//        (vii) return 2**k(1-((E+2**-k)-r))
//
// Special cases:
//      expm1(INF) is INF, expm1(NaN) is NaN;
//      expm1(-INF) is -1, and
//      for finite argument, only expm1(0)=0 is exact.
//
// Accuracy:
//      according to an error analysis, the error is always less than
//      1 ulp (unit in the last place).
//
// Misc. info.
//      For IEEE double
//          if x >  7.09782712893383973096e+02 then expm1(x) overflow
//
// Constants:
// The hexadecimal values are the intended ones for the following
// constants. The decimal values may be used, provided that the
// compiler will convert from decimal to binary accurately enough
// to produce the hexadecimal values shown.
//

// Expm1 returns e**x - 1, the base-e exponential of x minus 1.
// It is more accurate than Exp(x) - 1 when x is near zero.
//
// Special cases are:
//	Expm1(+Inf) = +Inf
//	Expm1(-Inf) = -1
//	Expm1(NaN) = NaN
// Very large values overflow to -1 or +Inf.
func Expm1(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.6f\n", math.Expm1(0.01))
	fmt.Printf("%.6f\n", math.Expm1(-1))
}
*/

// Floor returns the greatest integer value less than or equal to x.
//
// Special cases are:
//	Floor(±0) = ±0
//	Floor(±Inf) = ±Inf
//	Floor(NaN) = NaN
func Floor(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	c := math.Floor(1.51)
	fmt.Printf("%.1f", c)
}
*/

// Ceil returns the least integer value greater than or equal to x.
//
// Special cases are:
//	Ceil(±0) = ±0
//	Ceil(±Inf) = ±Inf
//	Ceil(NaN) = NaN
func Ceil(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	c := math.Ceil(1.49)
	fmt.Printf("%.1f", c)
}
*/

// Trunc returns the integer value of x.
//
// Special cases are:
//	Trunc(±0) = ±0
//	Trunc(±Inf) = ±Inf
//	Trunc(NaN) = NaN
func Trunc(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f\n", math.Trunc(math.Pi))
	fmt.Printf("%.2f\n", math.Trunc(-1.2345))
}
*/

// Round returns the nearest integer, rounding half away from zero.
//
// Special cases are:
//	Round(±0) = ±0
//	Round(±Inf) = ±Inf
//	Round(NaN) = NaN
func Round(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	p := math.Round(10.5)
	fmt.Printf("%.1f\n", p)

	n := math.Round(-10.5)
	fmt.Printf("%.1f\n", n)
}
*/

// RoundToEven returns the nearest integer, rounding ties to even.
//
// Special cases are:
//	RoundToEven(±0) = ±0
//	RoundToEven(±Inf) = ±Inf
//	RoundToEven(NaN) = NaN
func RoundToEven(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	u := math.RoundToEven(11.5)
	fmt.Printf("%.1f\n", u)

	d := math.RoundToEven(12.5)
	fmt.Printf("%.1f\n", d)
}
*/

// FMA returns x * y + z, computed with only one rounding.
// (That is, FMA returns the fused multiply-add of x, y, and z.)
func FMA(x, y, z float64) float64 {}

// Frexp breaks f into a normalized fraction
// and an integral power of two.
// It returns frac and exp satisfying f == frac × 2**exp,
// with the absolute value of frac in the interval [½, 1).
//
// Special cases are:
//	Frexp(±0) = ±0, 0
//	Frexp(±Inf) = ±Inf, 0
//	Frexp(NaN) = NaN, 0
func Frexp(f float64) (frac float64, exp int) {}

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/cprob/gamma.c.
// The go code is a simplified version of the original C.
//
//      tgamma.c
//
//      Gamma function
//
// SYNOPSIS:
//
// double x, y, tgamma();
// extern int signgam;
//
// y = tgamma( x );
//
// DESCRIPTION:
//
// Returns gamma function of the argument. The result is
// correctly signed, and the sign (+1 or -1) is also
// returned in a global (extern) variable named signgam.
// This variable is also filled in by the logarithmic gamma
// function lgamma().
//
// Arguments |x| <= 34 are reduced by recurrence and the function
// approximated by a rational function of degree 6/7 in the
// interval (2,3).  Large arguments are handled by Stirling's
// formula. Large negative arguments are made positive using
// a reflection formula.
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC      -34, 34      10000       1.3e-16     2.5e-17
//    IEEE    -170,-33      20000       2.3e-15     3.3e-16
//    IEEE     -33,  33     20000       9.4e-16     2.2e-16
//    IEEE      33, 171.6   20000       2.3e-15     3.2e-16
//
// Error for arguments outside the test range will be larger
// owing to error amplification by the exponential function.
//
// Cephes Math Library Release 2.8:  June, 2000
// Copyright 1984, 1987, 1989, 1992, 2000 by Stephen L. Moshier
//
// The readme file at http://netlib.sandia.gov/cephes/ says:
//    Some software in this archive may be from the book _Methods and
// Programs for Mathematical Functions_ (Prentice-Hall or Simon & Schuster
// International, 1989) or from the Cephes Mathematical Library, a
// commercial product. In either event, it is copyrighted by the author.
// What you see here may be used freely but it comes with no support or
// guarantee.
//
//   The two known misprints in the book are repaired here in the
// source listings for the gamma function and the incomplete beta
// integral.
//
//   Stephen L. Moshier
//   moshier@na-net.ornl.gov

// Gamma returns the Gamma function of x.
//
// Special cases are:
//	Gamma(+Inf) = +Inf
//	Gamma(+0) = +Inf
//	Gamma(-0) = -Inf
//	Gamma(x) = NaN for integer x < 0
//	Gamma(-Inf) = NaN
//	Gamma(NaN) = NaN
func Gamma(x float64) float64 {}

/*
	Hypot -- sqrt(p*p + q*q), but overflows only if the result does.
*/

// Hypot returns Sqrt(p*p + q*q), taking care to avoid
// unnecessary overflow and underflow.
//
// Special cases are:
//	Hypot(±Inf, q) = +Inf
//	Hypot(p, ±Inf) = +Inf
//	Hypot(NaN, q) = NaN
//	Hypot(p, NaN) = NaN
func Hypot(p, q float64) float64 {}

/*
	Bessel function of the first and second kinds of order zero.
*/

// The original C code and the long comment below are
// from FreeBSD's /usr/src/lib/msun/src/e_j0.c and
// came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// __ieee754_j0(x), __ieee754_y0(x)
// Bessel function of the first and second kinds of order zero.
// Method -- j0(x):
//      1. For tiny x, we use j0(x) = 1 - x**2/4 + x**4/64 - ...
//      2. Reduce x to |x| since j0(x)=j0(-x),  and
//         for x in (0,2)
//              j0(x) = 1-z/4+ z**2*R0/S0,  where z = x*x;
//         (precision:  |j0-1+z/4-z**2R0/S0 |<2**-63.67 )
//         for x in (2,inf)
//              j0(x) = sqrt(2/(pi*x))*(p0(x)*cos(x0)-q0(x)*sin(x0))
//         where x0 = x-pi/4. It is better to compute sin(x0),cos(x0)
//         as follow:
//              cos(x0) = cos(x)cos(pi/4)+sin(x)sin(pi/4)
//                      = 1/sqrt(2) * (cos(x) + sin(x))
//              sin(x0) = sin(x)cos(pi/4)-cos(x)sin(pi/4)
//                      = 1/sqrt(2) * (sin(x) - cos(x))
//         (To avoid cancellation, use
//              sin(x) +- cos(x) = -cos(2x)/(sin(x) -+ cos(x))
//         to compute the worse one.)
//
//      3 Special cases
//              j0(nan)= nan
//              j0(0) = 1
//              j0(inf) = 0
//
// Method -- y0(x):
//      1. For x<2.
//         Since
//              y0(x) = 2/pi*(j0(x)*(ln(x/2)+Euler) + x**2/4 - ...)
//         therefore y0(x)-2/pi*j0(x)*ln(x) is an even function.
//         We use the following function to approximate y0,
//              y0(x) = U(z)/V(z) + (2/pi)*(j0(x)*ln(x)), z= x**2
//         where
//              U(z) = u00 + u01*z + ... + u06*z**6
//              V(z) = 1  + v01*z + ... + v04*z**4
//         with absolute approximation error bounded by 2**-72.
//         Note: For tiny x, U/V = u0 and j0(x)~1, hence
//              y0(tiny) = u0 + (2/pi)*ln(tiny), (choose tiny<2**-27)
//      2. For x>=2.
//              y0(x) = sqrt(2/(pi*x))*(p0(x)*cos(x0)+q0(x)*sin(x0))
//         where x0 = x-pi/4. It is better to compute sin(x0),cos(x0)
//         by the method mentioned above.
//      3. Special cases: y0(0)=-inf, y0(x<0)=NaN, y0(inf)=0.
//

// J0 returns the order-zero Bessel function of the first kind.
//
// Special cases are:
//	J0(±Inf) = 0
//	J0(0) = 1
//	J0(NaN) = NaN
func J0(x float64) float64 {}

// Y0 returns the order-zero Bessel function of the second kind.
//
// Special cases are:
//	Y0(+Inf) = 0
//	Y0(0) = -Inf
//	Y0(x < 0) = NaN
//	Y0(NaN) = NaN
func Y0(x float64) float64 {}

/*
	Bessel function of the first and second kinds of order one.
*/

// The original C code and the long comment below are
// from FreeBSD's /usr/src/lib/msun/src/e_j1.c and
// came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// __ieee754_j1(x), __ieee754_y1(x)
// Bessel function of the first and second kinds of order one.
// Method -- j1(x):
//      1. For tiny x, we use j1(x) = x/2 - x**3/16 + x**5/384 - ...
//      2. Reduce x to |x| since j1(x)=-j1(-x),  and
//         for x in (0,2)
//              j1(x) = x/2 + x*z*R0/S0,  where z = x*x;
//         (precision:  |j1/x - 1/2 - R0/S0 |<2**-61.51 )
//         for x in (2,inf)
//              j1(x) = sqrt(2/(pi*x))*(p1(x)*cos(x1)-q1(x)*sin(x1))
//              y1(x) = sqrt(2/(pi*x))*(p1(x)*sin(x1)+q1(x)*cos(x1))
//         where x1 = x-3*pi/4. It is better to compute sin(x1),cos(x1)
//         as follow:
//              cos(x1) =  cos(x)cos(3pi/4)+sin(x)sin(3pi/4)
//                      =  1/sqrt(2) * (sin(x) - cos(x))
//              sin(x1) =  sin(x)cos(3pi/4)-cos(x)sin(3pi/4)
//                      = -1/sqrt(2) * (sin(x) + cos(x))
//         (To avoid cancellation, use
//              sin(x) +- cos(x) = -cos(2x)/(sin(x) -+ cos(x))
//         to compute the worse one.)
//
//      3 Special cases
//              j1(nan)= nan
//              j1(0) = 0
//              j1(inf) = 0
//
// Method -- y1(x):
//      1. screen out x<=0 cases: y1(0)=-inf, y1(x<0)=NaN
//      2. For x<2.
//         Since
//              y1(x) = 2/pi*(j1(x)*(ln(x/2)+Euler)-1/x-x/2+5/64*x**3-...)
//         therefore y1(x)-2/pi*j1(x)*ln(x)-1/x is an odd function.
//         We use the following function to approximate y1,
//              y1(x) = x*U(z)/V(z) + (2/pi)*(j1(x)*ln(x)-1/x), z= x**2
//         where for x in [0,2] (abs err less than 2**-65.89)
//              U(z) = U0[0] + U0[1]*z + ... + U0[4]*z**4
//              V(z) = 1  + v0[0]*z + ... + v0[4]*z**5
//         Note: For tiny x, 1/x dominate y1 and hence
//              y1(tiny) = -2/pi/tiny, (choose tiny<2**-54)
//      3. For x>=2.
//               y1(x) = sqrt(2/(pi*x))*(p1(x)*sin(x1)+q1(x)*cos(x1))
//         where x1 = x-3*pi/4. It is better to compute sin(x1),cos(x1)
//         by method mentioned above.

// J1 returns the order-one Bessel function of the first kind.
//
// Special cases are:
//	J1(±Inf) = 0
//	J1(NaN) = NaN
func J1(x float64) float64 {}

// Y1 returns the order-one Bessel function of the second kind.
//
// Special cases are:
//	Y1(+Inf) = 0
//	Y1(0) = -Inf
//	Y1(x < 0) = NaN
//	Y1(NaN) = NaN
func Y1(x float64) float64 {}

/*
	Bessel function of the first and second kinds of order n.
*/

// The original C code and the long comment below are
// from FreeBSD's /usr/src/lib/msun/src/e_jn.c and
// came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// __ieee754_jn(n, x), __ieee754_yn(n, x)
// floating point Bessel's function of the 1st and 2nd kind
// of order n
//
// Special cases:
//      y0(0)=y1(0)=yn(n,0) = -inf with division by zero signal;
//      y0(-ve)=y1(-ve)=yn(n,-ve) are NaN with invalid signal.
// Note 2. About jn(n,x), yn(n,x)
//      For n=0, j0(x) is called,
//      for n=1, j1(x) is called,
//      for n<x, forward recursion is used starting
//      from values of j0(x) and j1(x).
//      for n>x, a continued fraction approximation to
//      j(n,x)/j(n-1,x) is evaluated and then backward
//      recursion is used starting from a supposed value
//      for j(n,x). The resulting value of j(0,x) is
//      compared with the actual value to correct the
//      supposed value of j(n,x).
//
//      yn(n,x) is similar in all respects, except
//      that forward recursion is used for all
//      values of n>1.

// Jn returns the order-n Bessel function of the first kind.
//
// Special cases are:
//	Jn(n, ±Inf) = 0
//	Jn(n, NaN) = NaN
func Jn(n int, x float64) float64 {}

// Yn returns the order-n Bessel function of the second kind.
//
// Special cases are:
//	Yn(n, +Inf) = 0
//	Yn(n ≥ 0, 0) = -Inf
//	Yn(n < 0, 0) = +Inf if n is odd, -Inf if n is even
//	Yn(n, x < 0) = NaN
//	Yn(n, NaN) = NaN
func Yn(n int, x float64) float64 {}

// Ldexp is the inverse of Frexp.
// It returns frac × 2**exp.
//
// Special cases are:
//	Ldexp(±0, exp) = ±0
//	Ldexp(±Inf, exp) = ±Inf
//	Ldexp(NaN, exp) = NaN
func Ldexp(frac float64, exp int) float64 {}

/*
	Floating-point logarithm of the Gamma function.
*/

// The original C code and the long comment below are
// from FreeBSD's /usr/src/lib/msun/src/e_lgamma_r.c and
// came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// __ieee754_lgamma_r(x, signgamp)
// Reentrant version of the logarithm of the Gamma function
// with user provided pointer for the sign of Gamma(x).
//
// Method:
//   1. Argument Reduction for 0 < x <= 8
//      Since gamma(1+s)=s*gamma(s), for x in [0,8], we may
//      reduce x to a number in [1.5,2.5] by
//              lgamma(1+s) = log(s) + lgamma(s)
//      for example,
//              lgamma(7.3) = log(6.3) + lgamma(6.3)
//                          = log(6.3*5.3) + lgamma(5.3)
//                          = log(6.3*5.3*4.3*3.3*2.3) + lgamma(2.3)
//   2. Polynomial approximation of lgamma around its
//      minimum (ymin=1.461632144968362245) to maintain monotonicity.
//      On [ymin-0.23, ymin+0.27] (i.e., [1.23164,1.73163]), use
//              Let z = x-ymin;
//              lgamma(x) = -1.214862905358496078218 + z**2*poly(z)
//              poly(z) is a 14 degree polynomial.
//   2. Rational approximation in the primary interval [2,3]
//      We use the following approximation:
//              s = x-2.0;
//              lgamma(x) = 0.5*s + s*P(s)/Q(s)
//      with accuracy
//              |P/Q - (lgamma(x)-0.5s)| < 2**-61.71
//      Our algorithms are based on the following observation
//
//                             zeta(2)-1    2    zeta(3)-1    3
// lgamma(2+s) = s*(1-Euler) + --------- * s  -  --------- * s  + ...
//                                 2                 3
//
//      where Euler = 0.5772156649... is the Euler constant, which
//      is very close to 0.5.
//
//   3. For x>=8, we have
//      lgamma(x)~(x-0.5)log(x)-x+0.5*log(2pi)+1/(12x)-1/(360x**3)+....
//      (better formula:
//         lgamma(x)~(x-0.5)*(log(x)-1)-.5*(log(2pi)-1) + ...)
//      Let z = 1/x, then we approximation
//              f(z) = lgamma(x) - (x-0.5)(log(x)-1)
//      by
//                                  3       5             11
//              w = w0 + w1*z + w2*z  + w3*z  + ... + w6*z
//      where
//              |w - f(z)| < 2**-58.74
//
//   4. For negative x, since (G is gamma function)
//              -x*G(-x)*G(x) = pi/sin(pi*x),
//      we have
//              G(x) = pi/(sin(pi*x)*(-x)*G(-x))
//      since G(-x) is positive, sign(G(x)) = sign(sin(pi*x)) for x<0
//      Hence, for x<0, signgam = sign(sin(pi*x)) and
//              lgamma(x) = log(|Gamma(x)|)
//                        = log(pi/(|x*sin(pi*x)|)) - lgamma(-x);
//      Note: one should avoid computing pi*(-x) directly in the
//            computation of sin(pi*(-x)).
//
//   5. Special Cases
//              lgamma(2+s) ~ s*(1-Euler) for tiny s
//              lgamma(1)=lgamma(2)=0
//              lgamma(x) ~ -log(x) for tiny x
//              lgamma(0) = lgamma(inf) = inf
//              lgamma(-integer) = +-inf
//
//

// Lgamma returns the natural logarithm and sign (-1 or +1) of Gamma(x).
//
// Special cases are:
//	Lgamma(+Inf) = +Inf
//	Lgamma(0) = +Inf
//	Lgamma(-integer) = +Inf
//	Lgamma(-Inf) = -Inf
//	Lgamma(NaN) = NaN
func Lgamma(x float64) (lgamma float64, sign int) {}

/*
	Floating-point logarithm.
*/

// The original C code, the long comment, and the constants
// below are from FreeBSD's /usr/src/lib/msun/src/e_log.c
// and came with this notice. The go code is a simpler
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// __ieee754_log(x)
// Return the logarithm of x
//
// Method :
//   1. Argument Reduction: find k and f such that
//			x = 2**k * (1+f),
//	   where  sqrt(2)/2 < 1+f < sqrt(2) .
//
//   2. Approximation of log(1+f).
//	Let s = f/(2+f) ; based on log(1+f) = log(1+s) - log(1-s)
//		 = 2s + 2/3 s**3 + 2/5 s**5 + .....,
//	     	 = 2s + s*R
//      We use a special Reme algorithm on [0,0.1716] to generate
//	a polynomial of degree 14 to approximate R.  The maximum error
//	of this polynomial approximation is bounded by 2**-58.45. In
//	other words,
//		        2      4      6      8      10      12      14
//	    R(z) ~ L1*s +L2*s +L3*s +L4*s +L5*s  +L6*s  +L7*s
//	(the values of L1 to L7 are listed in the program) and
//	    |      2          14          |     -58.45
//	    | L1*s +...+L7*s    -  R(z) | <= 2
//	    |                             |
//	Note that 2s = f - s*f = f - hfsq + s*hfsq, where hfsq = f*f/2.
//	In order to guarantee error in log below 1ulp, we compute log by
//		log(1+f) = f - s*(f - R)		(if f is not too large)
//		log(1+f) = f - (hfsq - s*(hfsq+R)).	(better accuracy)
//
//	3. Finally,  log(x) = k*Ln2 + log(1+f).
//			    = k*Ln2_hi+(f-(hfsq-(s*(hfsq+R)+k*Ln2_lo)))
//	   Here Ln2 is split into two floating point number:
//			Ln2_hi + Ln2_lo,
//	   where n*Ln2_hi is always exact for |n| < 2000.
//
// Special cases:
//	log(x) is NaN with signal if x < 0 (including -INF) ;
//	log(+INF) is +INF; log(0) is -INF with signal;
//	log(NaN) is that NaN with no signal.
//
// Accuracy:
//	according to an error analysis, the error is always less than
//	1 ulp (unit in the last place).
//
// Constants:
// The hexadecimal values are the intended ones for the following
// constants. The decimal values may be used, provided that the
// compiler will convert from decimal to binary accurately enough
// to produce the hexadecimal values shown.

// Log returns the natural logarithm of x.
//
// Special cases are:
//	Log(+Inf) = +Inf
//	Log(0) = -Inf
//	Log(x < 0) = NaN
//	Log(NaN) = NaN
func Log(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	x := math.Log(1)
	fmt.Printf("%.1f\n", x)

	y := math.Log(2.7183)
	fmt.Printf("%.1f\n", y)
}
*/

// The original C code, the long comment, and the constants
// below are from FreeBSD's /usr/src/lib/msun/src/s_log1p.c
// and came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
//
// double log1p(double x)
//
// Method :
//   1. Argument Reduction: find k and f such that
//                      1+x = 2**k * (1+f),
//         where  sqrt(2)/2 < 1+f < sqrt(2) .
//
//      Note. If k=0, then f=x is exact. However, if k!=0, then f
//      may not be representable exactly. In that case, a correction
//      term is need. Let u=1+x rounded. Let c = (1+x)-u, then
//      log(1+x) - log(u) ~ c/u. Thus, we proceed to compute log(u),
//      and add back the correction term c/u.
//      (Note: when x > 2**53, one can simply return log(x))
//
//   2. Approximation of log1p(f).
//      Let s = f/(2+f) ; based on log(1+f) = log(1+s) - log(1-s)
//               = 2s + 2/3 s**3 + 2/5 s**5 + .....,
//               = 2s + s*R
//      We use a special Reme algorithm on [0,0.1716] to generate
//      a polynomial of degree 14 to approximate R The maximum error
//      of this polynomial approximation is bounded by 2**-58.45. In
//      other words,
//                      2      4      6      8      10      12      14
//          R(z) ~ Lp1*s +Lp2*s +Lp3*s +Lp4*s +Lp5*s  +Lp6*s  +Lp7*s
//      (the values of Lp1 to Lp7 are listed in the program)
//      and
//          |      2          14          |     -58.45
//          | Lp1*s +...+Lp7*s    -  R(z) | <= 2
//          |                             |
//      Note that 2s = f - s*f = f - hfsq + s*hfsq, where hfsq = f*f/2.
//      In order to guarantee error in log below 1ulp, we compute log
//      by
//              log1p(f) = f - (hfsq - s*(hfsq+R)).
//
//   3. Finally, log1p(x) = k*ln2 + log1p(f).
//                        = k*ln2_hi+(f-(hfsq-(s*(hfsq+R)+k*ln2_lo)))
//      Here ln2 is split into two floating point number:
//                   ln2_hi + ln2_lo,
//      where n*ln2_hi is always exact for |n| < 2000.
//
// Special cases:
//      log1p(x) is NaN with signal if x < -1 (including -INF) ;
//      log1p(+INF) is +INF; log1p(-1) is -INF with signal;
//      log1p(NaN) is that NaN with no signal.
//
// Accuracy:
//      according to an error analysis, the error is always less than
//      1 ulp (unit in the last place).
//
// Constants:
// The hexadecimal values are the intended ones for the following
// constants. The decimal values may be used, provided that the
// compiler will convert from decimal to binary accurately enough
// to produce the hexadecimal values shown.
//
// Note: Assuming log() return accurate answer, the following
//       algorithm can be used to compute log1p(x) to within a few ULP:
//
//              u = 1+x;
//              if(u==1.0) return x ; else
//                         return log(u)*(x/(u-1.0));
//
//       See HP-15C Advanced Functions Handbook, p.193.

// Log1p returns the natural logarithm of 1 plus its argument x.
// It is more accurate than Log(1 + x) when x is near zero.
//
// Special cases are:
//	Log1p(+Inf) = +Inf
//	Log1p(±0) = ±0
//	Log1p(-1) = -Inf
//	Log1p(x < -1) = NaN
//	Log1p(NaN) = NaN
func Log1p(x float64) float64 {}

// Log10 returns the decimal logarithm of x.
// The special cases are the same as for Log.
func Log10(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.1f", math.Log10(100))
}
*/

// Log2 returns the binary logarithm of x.
// The special cases are the same as for Log.
func Log2(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.1f", math.Log2(256))
}
*/

// Logb returns the binary exponent of x.
//
// Special cases are:
//	Logb(±Inf) = +Inf
//	Logb(0) = -Inf
//	Logb(NaN) = NaN
func Logb(x float64) float64 {}

// Ilogb returns the binary exponent of x as an integer.
//
// Special cases are:
//	Ilogb(±Inf) = MaxInt32
//	Ilogb(0) = MinInt32
//	Ilogb(NaN) = MaxInt32
func Ilogb(x float64) int {}

/*
	Floating-point mod function.
*/

// Mod returns the floating-point remainder of x/y.
// The magnitude of the result is less than y and its
// sign agrees with that of x.
//
// Special cases are:
//	Mod(±Inf, y) = NaN
//	Mod(NaN, y) = NaN
//	Mod(x, 0) = NaN
//	Mod(x, ±Inf) = x
//	Mod(x, NaN) = NaN
func Mod(x, y float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	c := math.Mod(7, 4)
	fmt.Printf("%.1f", c)
}
*/

// Modf returns integer and fractional floating-point numbers
// that sum to f. Both values have the same sign as f.
//
// Special cases are:
//	Modf(±Inf) = ±Inf, NaN
//	Modf(NaN) = NaN, NaN
func Modf(f float64) (int float64, frac float64) {}

// Nextafter32 returns the next representable float32 value after x towards y.
//
// Special cases are:
//	Nextafter32(x, x)   = x
//	Nextafter32(NaN, y) = NaN
//	Nextafter32(x, NaN) = NaN
func Nextafter32(x, y float32) (r float32) {}

// Nextafter returns the next representable float64 value after x towards y.
//
// Special cases are:
//	Nextafter(x, x)   = x
//	Nextafter(NaN, y) = NaN
//	Nextafter(x, NaN) = NaN
func Nextafter(x, y float64) (r float64) {}

// Special cases taken from FreeBSD's /usr/src/lib/msun/src/e_pow.c
// updated by IEEE Std. 754-2008 "Section 9.2.1 Special values".

// Pow returns x**y, the base-x exponential of y.
//
// Special cases are (in order):
//	Pow(x, ±0) = 1 for any x
//	Pow(1, y) = 1 for any y
//	Pow(x, 1) = x for any x
//	Pow(NaN, y) = NaN
//	Pow(x, NaN) = NaN
//	Pow(±0, y) = ±Inf for y an odd integer < 0
//	Pow(±0, -Inf) = +Inf
//	Pow(±0, +Inf) = +0
//	Pow(±0, y) = +Inf for finite y < 0 and not an odd integer
//	Pow(±0, y) = ±0 for y an odd integer > 0
//	Pow(±0, y) = +0 for finite y > 0 and not an odd integer
//	Pow(-1, ±Inf) = 1
//	Pow(x, +Inf) = +Inf for |x| > 1
//	Pow(x, -Inf) = +0 for |x| > 1
//	Pow(x, +Inf) = +0 for |x| < 1
//	Pow(x, -Inf) = +Inf for |x| < 1
//	Pow(+Inf, y) = +Inf for y > 0
//	Pow(+Inf, y) = +0 for y < 0
//	Pow(-Inf, y) = Pow(-0, -y)
//	Pow(x, y) = NaN for finite x < 0 and finite non-integer y
func Pow(x, y float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	c := math.Pow(2, 3)
	fmt.Printf("%.1f", c)
}
*/

// Pow10 returns 10**n, the base-10 exponential of n.
//
// Special cases are:
//	Pow10(n) =    0 for n < -323
//	Pow10(n) = +Inf for n > 308
func Pow10(n int) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	c := math.Pow10(2)
	fmt.Printf("%.1f", c)
}
*/

// The original C code and the comment below are from
// FreeBSD's /usr/src/lib/msun/src/e_remainder.c and came
// with this notice. The go code is a simplified version of
// the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// __ieee754_remainder(x,y)
// Return :
//      returns  x REM y  =  x - [x/y]*y  as if in infinite
//      precision arithmetic, where [x/y] is the (infinite bit)
//      integer nearest x/y (in half way cases, choose the even one).
// Method :
//      Based on Mod() returning  x - [x/y]chopped * y  exactly.

// Remainder returns the IEEE 754 floating-point remainder of x/y.
//
// Special cases are:
//	Remainder(±Inf, y) = NaN
//	Remainder(NaN, y) = NaN
//	Remainder(x, 0) = NaN
//	Remainder(x, ±Inf) = x
//	Remainder(x, NaN) = NaN
func Remainder(x, y float64) float64 {}

// Signbit reports whether x is negative or negative zero.
func Signbit(x float64) bool {}

/*
	Floating-point sine and cosine.
*/

// The original C code, the long comment, and the constants
// below were from http://netlib.sandia.gov/cephes/cmath/sin.c,
// available from http://www.netlib.org/cephes/cmath.tgz.
// The go code is a simplified version of the original C.
//
//      sin.c
//
//      Circular sine
//
// SYNOPSIS:
//
// double x, y, sin();
// y = sin( x );
//
// DESCRIPTION:
//
// Range reduction is into intervals of pi/4.  The reduction error is nearly
// eliminated by contriving an extended precision modular arithmetic.
//
// Two polynomial approximating functions are employed.
// Between 0 and pi/4 the sine is approximated by
//      x  +  x**3 P(x**2).
// Between pi/4 and pi/2 the cosine is represented as
//      1  -  x**2 Q(x**2).
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain      # trials      peak         rms
//    DEC       0, 10       150000       3.0e-17     7.8e-18
//    IEEE -1.07e9,+1.07e9  130000       2.1e-16     5.4e-17
//
// Partial loss of accuracy begins to occur at x = 2**30 = 1.074e9.  The loss
// is not gradual, but jumps suddenly to about 1 part in 10e7.  Results may
// be meaningless for x > 2**49 = 5.6e14.
//
//      cos.c
//
//      Circular cosine
//
// SYNOPSIS:
//
// double x, y, cos();
// y = cos( x );
//
// DESCRIPTION:
//
// Range reduction is into intervals of pi/4.  The reduction error is nearly
// eliminated by contriving an extended precision modular arithmetic.
//
// Two polynomial approximating functions are employed.
// Between 0 and pi/4 the cosine is approximated by
//      1  -  x**2 Q(x**2).
// Between pi/4 and pi/2 the sine is represented as
//      x  +  x**3 P(x**2).
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain      # trials      peak         rms
//    IEEE -1.07e9,+1.07e9  130000       2.1e-16     5.4e-17
//    DEC        0,+1.07e9   17000       3.0e-17     7.2e-18
//
// Cephes Math Library Release 2.8:  June, 2000
// Copyright 1984, 1987, 1989, 1992, 2000 by Stephen L. Moshier
//
// The readme file at http://netlib.sandia.gov/cephes/ says:
//    Some software in this archive may be from the book _Methods and
// Programs for Mathematical Functions_ (Prentice-Hall or Simon & Schuster
// International, 1989) or from the Cephes Mathematical Library, a
// commercial product. In either event, it is copyrighted by the author.
// What you see here may be used freely but it comes with no support or
// guarantee.
//
//   The two known misprints in the book are repaired here in the
// source listings for the gamma function and the incomplete beta
// integral.
//
//   Stephen L. Moshier
//   moshier@na-net.ornl.gov

// Cos returns the cosine of the radian argument x.
//
// Special cases are:
//	Cos(±Inf) = NaN
//	Cos(NaN) = NaN
func Cos(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Cos(math.Pi/2))
}
*/

// Sin returns the sine of the radian argument x.
//
// Special cases are:
//	Sin(±0) = ±0
//	Sin(±Inf) = NaN
//	Sin(NaN) = NaN
func Sin(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Sin(math.Pi))
}
*/

// Coefficients _sin[] and _cos[] are found in pkg/math/sin.go.

// Sincos returns Sin(x), Cos(x).
//
// Special cases are:
//	Sincos(±0) = ±0, 1
//	Sincos(±Inf) = NaN, NaN
//	Sincos(NaN) = NaN, NaN
func Sincos(x float64) (sin, cos float64) {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	sin, cos := math.Sincos(0)
	fmt.Printf("%.2f, %.2f", sin, cos)
}
*/

/*
	Floating-point hyperbolic sine and cosine.

	The exponential func is called for arguments
	greater in magnitude than 0.5.

	A series is used for arguments smaller in magnitude than 0.5.

	Cosh(x) is computed from the exponential func for
	all arguments.
*/

// Sinh returns the hyperbolic sine of x.
//
// Special cases are:
//	Sinh(±0) = ±0
//	Sinh(±Inf) = ±Inf
//	Sinh(NaN) = NaN
func Sinh(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Sinh(0))
}
*/

// Cosh returns the hyperbolic cosine of x.
//
// Special cases are:
//	Cosh(±0) = 1
//	Cosh(±Inf) = +Inf
//	Cosh(NaN) = NaN
func Cosh(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Cosh(0))
}
*/

// The original C code and the long comment below are
// from FreeBSD's /usr/src/lib/msun/src/e_sqrt.c and
// came with this notice. The go code is a simplified
// version of the original C.
//
// ====================================================
// Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
//
// Developed at SunPro, a Sun Microsystems, Inc. business.
// Permission to use, copy, modify, and distribute this
// software is freely granted, provided that this notice
// is preserved.
// ====================================================
//
// __ieee754_sqrt(x)
// Return correctly rounded sqrt.
//           -----------------------------------------
//           | Use the hardware sqrt if you have one |
//           -----------------------------------------
// Method:
//   Bit by bit method using integer arithmetic. (Slow, but portable)
//   1. Normalization
//      Scale x to y in [1,4) with even powers of 2:
//      find an integer k such that  1 <= (y=x*2**(2k)) < 4, then
//              sqrt(x) = 2**k * sqrt(y)
//   2. Bit by bit computation
//      Let q  = sqrt(y) truncated to i bit after binary point (q = 1),
//           i                                                   0
//                                     i+1         2
//          s  = 2*q , and      y  =  2   * ( y - q  ).          (1)
//           i      i            i                 i
//
//      To compute q    from q , one checks whether
//                  i+1       i
//
//                            -(i+1) 2
//                      (q + 2      )  <= y.                     (2)
//                        i
//                                                            -(i+1)
//      If (2) is false, then q   = q ; otherwise q   = q  + 2      .
//                             i+1   i             i+1   i
//
//      With some algebraic manipulation, it is not difficult to see
//      that (2) is equivalent to
//                             -(i+1)
//                      s  +  2       <= y                       (3)
//                       i                i
//
//      The advantage of (3) is that s  and y  can be computed by
//                                    i      i
//      the following recurrence formula:
//          if (3) is false
//
//          s     =  s  ,       y    = y   ;                     (4)
//           i+1      i          i+1    i
//
//      otherwise,
//                         -i                      -(i+1)
//          s     =  s  + 2  ,  y    = y  -  s  - 2              (5)
//           i+1      i          i+1    i     i
//
//      One may easily use induction to prove (4) and (5).
//      Note. Since the left hand side of (3) contain only i+2 bits,
//            it does not necessary to do a full (53-bit) comparison
//            in (3).
//   3. Final rounding
//      After generating the 53 bits result, we compute one more bit.
//      Together with the remainder, we can decide whether the
//      result is exact, bigger than 1/2ulp, or less than 1/2ulp
//      (it will never equal to 1/2ulp).
//      The rounding mode can be detected by checking whether
//      huge + tiny is equal to huge, and whether huge - tiny is
//      equal to huge for some floating point number "huge" and "tiny".
//
//
// Notes:  Rounding mode detection omitted. The constants "mask", "shift",
// and "bias" are found in src/math/bits.go

// Sqrt returns the square root of x.
//
// Special cases are:
//	Sqrt(+Inf) = +Inf
//	Sqrt(±0) = ±0
//	Sqrt(x < 0) = NaN
//	Sqrt(NaN) = NaN
func Sqrt(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	const (
		a = 3
		b = 4
	)
	c := math.Sqrt(a*a + b*b)
	fmt.Printf("%.1f", c)
}
*/

/*
	Floating-point tangent.
*/

// The original C code, the long comment, and the constants
// below were from http://netlib.sandia.gov/cephes/cmath/sin.c,
// available from http://www.netlib.org/cephes/cmath.tgz.
// The go code is a simplified version of the original C.
//
//      tan.c
//
//      Circular tangent
//
// SYNOPSIS:
//
// double x, y, tan();
// y = tan( x );
//
// DESCRIPTION:
//
// Returns the circular tangent of the radian argument x.
//
// Range reduction is modulo pi/4.  A rational function
//       x + x**3 P(x**2)/Q(x**2)
// is employed in the basic interval [0, pi/4].
//
// ACCURACY:
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC      +-1.07e9      44000      4.1e-17     1.0e-17
//    IEEE     +-1.07e9      30000      2.9e-16     8.1e-17
//
// Partial loss of accuracy begins to occur at x = 2**30 = 1.074e9.  The loss
// is not gradual, but jumps suddenly to about 1 part in 10e7.  Results may
// be meaningless for x > 2**49 = 5.6e14.
// [Accuracy loss statement from sin.go comments.]
//
// Cephes Math Library Release 2.8:  June, 2000
// Copyright 1984, 1987, 1989, 1992, 2000 by Stephen L. Moshier
//
// The readme file at http://netlib.sandia.gov/cephes/ says:
//    Some software in this archive may be from the book _Methods and
// Programs for Mathematical Functions_ (Prentice-Hall or Simon & Schuster
// International, 1989) or from the Cephes Mathematical Library, a
// commercial product. In either event, it is copyrighted by the author.
// What you see here may be used freely but it comes with no support or
// guarantee.
//
//   The two known misprints in the book are repaired here in the
// source listings for the gamma function and the incomplete beta
// integral.
//
//   Stephen L. Moshier
//   moshier@na-net.ornl.gov

// Tan returns the tangent of the radian argument x.
//
// Special cases are:
//	Tan(±0) = ±0
//	Tan(±Inf) = NaN
//	Tan(NaN) = NaN
func Tan(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Tan(0))
}
*/

// The original C code, the long comment, and the constants
// below were from http://netlib.sandia.gov/cephes/cmath/sin.c,
// available from http://www.netlib.org/cephes/cmath.tgz.
// The go code is a simplified version of the original C.
//      tanh.c
//
//      Hyperbolic tangent
//
// SYNOPSIS:
//
// double x, y, tanh();
//
// y = tanh( x );
//
// DESCRIPTION:
//
// Returns hyperbolic tangent of argument in the range MINLOG to MAXLOG.
//      MAXLOG = 8.8029691931113054295988e+01 = log(2**127)
//      MINLOG = -8.872283911167299960540e+01 = log(2**-128)
//
// A rational function is used for |x| < 0.625.  The form
// x + x**3 P(x)/Q(x) of Cody & Waite is employed.
// Otherwise,
//      tanh(x) = sinh(x)/cosh(x) = 1  -  2/(exp(2x) + 1).
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    IEEE      -2,2        30000       2.5e-16     5.8e-17
//
// Cephes Math Library Release 2.8:  June, 2000
// Copyright 1984, 1987, 1989, 1992, 2000 by Stephen L. Moshier
//
// The readme file at http://netlib.sandia.gov/cephes/ says:
//    Some software in this archive may be from the book _Methods and
// Programs for Mathematical Functions_ (Prentice-Hall or Simon & Schuster
// International, 1989) or from the Cephes Mathematical Library, a
// commercial product. In either event, it is copyrighted by the author.
// What you see here may be used freely but it comes with no support or
// guarantee.
//
//   The two known misprints in the book are repaired here in the
// source listings for the gamma function and the incomplete beta
// integral.
//
//   Stephen L. Moshier
//   moshier@na-net.ornl.gov
//

// Tanh returns the hyperbolic tangent of x.
//
// Special cases are:
//	Tanh(±0) = ±0
//	Tanh(±Inf) = ±1
//	Tanh(NaN) = NaN
func Tanh(x float64) float64 {}
/*
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", math.Tanh(0))
}
*/

// Float32bits returns the IEEE 754 binary representation of f,
// with the sign bit of f and the result in the same bit position.
// Float32bits(Float32frombits(x)) == x.
func Float32bits(f float32) uint32 {}

// Float32frombits returns the floating-point number corresponding
// to the IEEE 754 binary representation b, with the sign bit of b
// and the result in the same bit position.
// Float32frombits(Float32bits(x)) == x.
func Float32frombits(b uint32) float32 {}

// Float64bits returns the IEEE 754 binary representation of f,
// with the sign bit of f and the result in the same bit position,
// and Float64bits(Float64frombits(x)) == x.
func Float64bits(f float64) uint64 {}

// Float64frombits returns the floating-point number corresponding
// to the IEEE 754 binary representation b, with the sign bit of b
// and the result in the same bit position.
// Float64frombits(Float64bits(x)) == x.
func Float64frombits(b uint64) float64 {}
