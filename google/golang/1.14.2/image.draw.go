// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package draw provides image composition functions.
//
// See "The Go image/draw package" for an introduction to this package:
// https://golang.org/doc/articles/image_draw.html
package draw

import (
	"image"
	"image/color"
)

// Image is an image.Image with a Set method to change a single pixel.
type Image interface {
	image.Image
	Set(x, y int, c color.Color)
}

// Quantizer produces a palette for an image.
type Quantizer interface {
	// Quantize appends up to cap(p) - len(p) colors to p and returns the
	// updated palette suitable for converting m to a paletted image.
	Quantize(p color.Palette, m image.Image) color.Palette
}

// Op is a Porter-Duff compositing operator.
type Op int

const (
	// Over specifies ``(src in mask) over dst''.
	Over Op = iota
	// Src specifies ``src in mask''.
	Src
)

// Draw implements the Drawer interface by calling the Draw function with this
// Op.
func (op Op) Draw(dst Image, r image.Rectangle, src image.Image, sp image.Point) {}

// Drawer contains the Draw method.
type Drawer interface {
	// Draw aligns r.Min in dst with sp in src and then replaces the
	// rectangle r in dst with the result of drawing src on dst.
	Draw(dst Image, r image.Rectangle, src image.Image, sp image.Point)
}

// FloydSteinberg is a Drawer that is the Src Op with Floyd-Steinberg error
// diffusion.
var FloydSteinberg Drawer = floydSteinberg{}
/*
package main

import (
	"fmt"
	"image"
	"image/color"
	"image/draw"
	"math"
)

func main() {
	const width = 130
	const height = 50

	im := image.NewGray(image.Rectangle{Max: image.Point{X: width, Y: height}})
	for x := 0; x < width; x++ {
		for y := 0; y < height; y++ {
			dist := math.Sqrt(math.Pow(float64(x-width/2), 2)/3+math.Pow(float64(y-height/2), 2)) / (height / 1.5) * 255
			var gray uint8
			if dist > 255 {
				gray = 255
			} else {
				gray = uint8(dist)
			}
			im.SetGray(x, y, color.Gray{Y: 255 - gray})
		}
	}
	pi := image.NewPaletted(im.Bounds(), []color.Color{
		color.Gray{Y: 255},
		color.Gray{Y: 160},
		color.Gray{Y: 70},
		color.Gray{Y: 35},
		color.Gray{Y: 0},
	})

	draw.FloydSteinberg.Draw(pi, im.Bounds(), im, image.ZP)
	shade := []string{" ", "░", "▒", "▓", "█"}
	for i, p := range pi.Pix {
		fmt.Print(shade[p])
		if (i+1)%width == 0 {
			fmt.Print("\n")
		}
	}
}
*/

type floydSteinberg struct{}

func (floydSteinberg) Draw(dst Image, r image.Rectangle, src image.Image, sp image.Point) {}

// Draw calls DrawMask with a nil mask.
func Draw(dst Image, r image.Rectangle, src image.Image, sp image.Point, op Op) {}

// DrawMask aligns r.Min in dst with sp in src and mp in mask and then replaces the rectangle r
// in dst with the result of a Porter-Duff composition. A nil mask is treated as opaque.
func DrawMask(dst Image, r image.Rectangle, src image.Image, sp image.Point, mask image.Image, mp image.Point, op Op) {}
