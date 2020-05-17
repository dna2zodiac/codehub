// Copyright 2010 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package cmplx provides basic constants and mathematical functions for
// complex numbers.
package cmplx

import "math"

// Abs returns the absolute value (also called the modulus) of x.
func Abs(x complex128) float64 {}
/*
package main

import (
	"fmt"
	"math/cmplx"
)

func main() {
	fmt.Printf("%.1f", cmplx.Abs(3+4i))
}
*/

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/c9x-complex/clog.c.
// The go code is a simplified version of the original C.
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

// Complex circular arc sine
//
// DESCRIPTION:
//
// Inverse complex sine:
//                               2
// w = -i clog( iz + csqrt( 1 - z ) ).
//
// casin(z) = -i casinh(iz)
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10     10100       2.1e-15     3.4e-16
//    IEEE      -10,+10     30000       2.2e-14     2.7e-15
// Larger relative error can be observed for z near zero.
// Also tested by csin(casin(z)) = z.

// Asin returns the inverse sine of x.
func Asin(x complex128) complex128 {}

// Asinh returns the inverse hyperbolic sine of x.
func Asinh(x complex128) complex128 {}

// Complex circular arc cosine
//
// DESCRIPTION:
//
// w = arccos z  =  PI/2 - arcsin z.
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      5200      1.6e-15      2.8e-16
//    IEEE      -10,+10     30000      1.8e-14      2.2e-15

// Acos returns the inverse cosine of x.
func Acos(x complex128) complex128 {}

// Acosh returns the inverse hyperbolic cosine of x.
func Acosh(x complex128) complex128 {}

// Complex circular arc tangent
//
// DESCRIPTION:
//
// If
//     z = x + iy,
//
// then
//          1       (    2x     )
// Re w  =  - arctan(-----------)  +  k PI
//          2       (     2    2)
//                  (1 - x  - y )
//
//               ( 2         2)
//          1    (x  +  (y+1) )
// Im w  =  - log(------------)
//          4    ( 2         2)
//               (x  +  (y-1) )
//
// Where k is an arbitrary integer.
//
// catan(z) = -i catanh(iz).
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      5900       1.3e-16     7.8e-18
//    IEEE      -10,+10     30000       2.3e-15     8.5e-17
// The check catan( ctan(z) )  =  z, with |x| and |y| < PI/2,
// had peak relative error 1.5e-16, rms relative error
// 2.9e-17.  See also clog().

// Atan returns the inverse tangent of x.
func Atan(x complex128) complex128 {}

// Atanh returns the inverse hyperbolic tangent of x.
func Atanh(x complex128) complex128 {}

// Conj returns the complex conjugate of x.
func Conj(x complex128) complex128 {}

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/c9x-complex/clog.c.
// The go code is a simplified version of the original C.
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

// Complex exponential function
//
// DESCRIPTION:
//
// Returns the complex exponential of the complex argument z.
//
// If
//     z = x + iy,
//     r = exp(x),
// then
//     w = r cos y + i r sin y.
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      8700       3.7e-17     1.1e-17
//    IEEE      -10,+10     30000       3.0e-16     8.7e-17

// Exp returns e**x, the base-e exponential of x.
func Exp(x complex128) complex128 {}
/*
package main

import (
	"fmt"
	"math"
	"math/cmplx"
)

func main() {
	fmt.Printf("%.1f", cmplx.Exp(1i*math.Pi)+1)
}
*/

// IsInf reports whether either real(x) or imag(x) is an infinity.
func IsInf(x complex128) bool {}

// Inf returns a complex infinity, complex(+Inf, +Inf).
func Inf() complex128 {}

// IsNaN reports whether either real(x) or imag(x) is NaN
// and neither is an infinity.
func IsNaN(x complex128) bool {}

// NaN returns a complex ``not-a-number'' value.
func NaN() complex128 {}

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/c9x-complex/clog.c.
// The go code is a simplified version of the original C.
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

// Complex natural logarithm
//
// DESCRIPTION:
//
// Returns complex logarithm to the base e (2.718...) of
// the complex argument z.
//
// If
//       z = x + iy, r = sqrt( x**2 + y**2 ),
// then
//       w = log(r) + i arctan(y/x).
//
// The arctangent ranges from -PI to +PI.
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      7000       8.5e-17     1.9e-17
//    IEEE      -10,+10     30000       5.0e-15     1.1e-16
//
// Larger relative error can be observed for z near 1 +i0.
// In IEEE arithmetic the peak absolute error is 5.2e-16, rms
// absolute error 1.0e-16.

// Log returns the natural logarithm of x.
func Log(x complex128) complex128 {}

// Log10 returns the decimal logarithm of x.
func Log10(x complex128) complex128 {}

// Phase returns the phase (also called the argument) of x.
// The returned value is in the range [-Pi, Pi].
func Phase(x complex128) float64 {}

// Polar returns the absolute value r and phase θ of x,
// such that x = r * e**θi.
// The phase is in the range [-Pi, Pi].
func Polar(x complex128) (r, θ float64) {}
/*
package main

import (
	"fmt"
	"math"
	"math/cmplx"
)

func main() {
	r, theta := cmplx.Polar(2i)
	fmt.Printf("r: %.1f, θ: %.1f*π", r, theta/math.Pi)
}
*/

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/c9x-complex/clog.c.
// The go code is a simplified version of the original C.
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

// Complex power function
//
// DESCRIPTION:
//
// Raises complex A to the complex Zth power.
// Definition is per AMS55 # 4.2.8,
// analytically equivalent to cpow(a,z) = cexp(z clog(a)).
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    IEEE      -10,+10     30000       9.4e-15     1.5e-15

// Pow returns x**y, the base-x exponential of y.
// For generalized compatibility with math.Pow:
//	Pow(0, ±0) returns 1+0i
//	Pow(0, c) for real(c)<0 returns Inf+0i if imag(c) is zero, otherwise Inf+Inf i.
func Pow(x, y complex128) complex128 {}

// Rect returns the complex number x with polar coordinates r, θ.
func Rect(r, θ float64) complex128 {}

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/c9x-complex/clog.c.
// The go code is a simplified version of the original C.
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

// Complex circular sine
//
// DESCRIPTION:
//
// If
//     z = x + iy,
//
// then
//
//     w = sin x  cosh y  +  i cos x sinh y.
//
// csin(z) = -i csinh(iz).
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      8400       5.3e-17     1.3e-17
//    IEEE      -10,+10     30000       3.8e-16     1.0e-16
// Also tested by csin(casin(z)) = z.

// Sin returns the sine of x.
func Sin(x complex128) complex128 {}

// Complex hyperbolic sine
//
// DESCRIPTION:
//
// csinh z = (cexp(z) - cexp(-z))/2
//         = sinh x * cos y  +  i cosh x * sin y .
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    IEEE      -10,+10     30000       3.1e-16     8.2e-17

// Sinh returns the hyperbolic sine of x.
func Sinh(x complex128) complex128 {}

// Complex circular cosine
//
// DESCRIPTION:
//
// If
//     z = x + iy,
//
// then
//
//     w = cos x  cosh y  -  i sin x sinh y.
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      8400       4.5e-17     1.3e-17
//    IEEE      -10,+10     30000       3.8e-16     1.0e-16

// Cos returns the cosine of x.
func Cos(x complex128) complex128 {}

// Complex hyperbolic cosine
//
// DESCRIPTION:
//
// ccosh(z) = cosh x  cos y + i sinh x sin y .
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    IEEE      -10,+10     30000       2.9e-16     8.1e-17

// Cosh returns the hyperbolic cosine of x.
func Cosh(x complex128) complex128 {}

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/c9x-complex/clog.c.
// The go code is a simplified version of the original C.
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

// Complex square root
//
// DESCRIPTION:
//
// If z = x + iy,  r = |z|, then
//
//                       1/2
// Re w  =  [ (r + x)/2 ]   ,
//
//                       1/2
// Im w  =  [ (r - x)/2 ]   .
//
// Cancelation error in r-x or r+x is avoided by using the
// identity  2 Re w Im w  =  y.
//
// Note that -w is also a square root of z. The root chosen
// is always in the right half plane and Im w has the same sign as y.
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10     25000       3.2e-17     9.6e-18
//    IEEE      -10,+10   1,000,000     2.9e-16     6.1e-17

// Sqrt returns the square root of x.
// The result r is chosen so that real(r) ≥ 0 and imag(r) has the same sign as imag(x).
func Sqrt(x complex128) complex128 {}

// The original C code, the long comment, and the constants
// below are from http://netlib.sandia.gov/cephes/c9x-complex/clog.c.
// The go code is a simplified version of the original C.
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

// Complex circular tangent
//
// DESCRIPTION:
//
// If
//     z = x + iy,
//
// then
//
//           sin 2x  +  i sinh 2y
//     w  =  --------------------.
//            cos 2x  +  cosh 2y
//
// On the real axis the denominator is zero at odd multiples
// of PI/2.  The denominator is evaluated by its Taylor
// series near these points.
//
// ctan(z) = -i ctanh(iz).
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      5200       7.1e-17     1.6e-17
//    IEEE      -10,+10     30000       7.2e-16     1.2e-16
// Also tested by ctan * ccot = 1 and catan(ctan(z))  =  z.

// Tan returns the tangent of x.
func Tan(x complex128) complex128 {}

// Complex hyperbolic tangent
//
// DESCRIPTION:
//
// tanh z = (sinh 2x  +  i sin 2y) / (cosh 2x + cos 2y) .
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    IEEE      -10,+10     30000       1.7e-14     2.4e-16

// Tanh returns the hyperbolic tangent of x.
func Tanh(x complex128) complex128 {}

// Complex circular cotangent
//
// DESCRIPTION:
//
// If
//     z = x + iy,
//
// then
//
//           sin 2x  -  i sinh 2y
//     w  =  --------------------.
//            cosh 2y  -  cos 2x
//
// On the real axis, the denominator has zeros at even
// multiples of PI/2.  Near these points it is evaluated
// by a Taylor series.
//
// ACCURACY:
//
//                      Relative error:
// arithmetic   domain     # trials      peak         rms
//    DEC       -10,+10      3000       6.5e-17     1.6e-17
//    IEEE      -10,+10     30000       9.2e-16     1.2e-16
// Also tested by ctan * ccot = 1 + i0.

// Cot returns the cotangent of x.
func Cot(x complex128) complex128 {}
