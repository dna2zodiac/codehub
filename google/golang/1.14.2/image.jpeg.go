// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package jpeg implements a JPEG image decoder and encoder.
//
// JPEG is defined in ITU-T T.81: https://www.w3.org/Graphics/JPEG/itu-t81.pdf.
package jpeg

import (
	"image"
	"image/color"
	"io"
)

// TODO(nigeltao): fix up the doc comment style so that sentences start with
// the name of the type or function that they annotate.

// A FormatError reports that the input is not a valid JPEG.
type FormatError string

func (e FormatError) Error() string {}

// An UnsupportedError reports that the input uses a valid but unimplemented JPEG feature.
type UnsupportedError string

func (e UnsupportedError) Error() string {}

var errUnsupportedSubsamplingRatio = UnsupportedError("luma/chroma subsampling ratio")

// Deprecated: Reader is not used by the image/jpeg package and should
// not be used by others. It is kept for compatibility.
type Reader interface {
	io.ByteReader
	io.Reader
}

// errMissingFF00 means that readByteStuffedByte encountered an 0xff byte (a
// marker byte) that wasn't the expected byte-stuffed sequence 0xff, 0x00.
var errMissingFF00 = FormatError("missing 0xff00 sequence")

// Decode reads a JPEG image from r and returns it as an image.Image.
func Decode(r io.Reader) (image.Image, error) {}

// DecodeConfig returns the color model and dimensions of a JPEG image without
// decoding the entire image.
func DecodeConfig(r io.Reader) (image.Config, error) {}

func init() {
	image.RegisterFormat("jpeg", "\xff\xd8", Decode, DecodeConfig)
}

// DefaultQuality is the default quality encoding parameter.
const DefaultQuality = 75

// Options are the encoding parameters.
// Quality ranges from 1 to 100 inclusive, higher is better.
type Options struct {
	Quality int
}

// Encode writes the Image m to w in JPEG 4:2:0 baseline format with the given
// options. Default parameters are used if a nil *Options is passed.
func Encode(w io.Writer, m image.Image, o *Options) error {}
