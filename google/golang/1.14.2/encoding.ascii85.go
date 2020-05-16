// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package ascii85 implements the ascii85 data encoding
// as used in the btoa tool and Adobe's PostScript and PDF document formats.
package ascii85

import (
	"io"
)

/*
 * Encoder
 */

// Encode encodes src into at most MaxEncodedLen(len(src))
// bytes of dst, returning the actual number of bytes written.
//
// The encoding handles 4-byte chunks, using a special encoding
// for the last fragment, so Encode is not appropriate for use on
// individual blocks of a large data stream. Use NewEncoder() instead.
//
// Often, ascii85-encoded data is wrapped in <~ and ~> symbols.
// Encode does not add these.
func Encode(dst, src []byte) int {}

// MaxEncodedLen returns the maximum length of an encoding of n source bytes.
func MaxEncodedLen(n int) int {}

// NewEncoder returns a new ascii85 stream encoder. Data written to
// the returned writer will be encoded and then written to w.
// Ascii85 encodings operate in 32-bit blocks; when finished
// writing, the caller must Close the returned encoder to flush any
// trailing partial block.
func NewEncoder(w io.Writer) io.WriteCloser {}

type encoder struct {
	err  error
	w    io.Writer
	buf  [4]byte    // buffered data waiting to be encoded
	nbuf int        // number of bytes in buf
	out  [1024]byte // output buffer
}

func (e *encoder) Write(p []byte) (n int, err error) {}

// Close flushes any pending output from the encoder.
// It is an error to call Write after calling Close.
func (e *encoder) Close() error {
	// If there's anything left in the buffer, flush it out
	if e.err == nil && e.nbuf > 0 {
		nout := Encode(e.out[0:], e.buf[0:e.nbuf])
		e.nbuf = 0
		_, e.err = e.w.Write(e.out[0:nout])
	}
	return e.err
}

/*
 * Decoder
 */

type CorruptInputError int64

func (e CorruptInputError) Error() string {}

// Decode decodes src into dst, returning both the number
// of bytes written to dst and the number consumed from src.
// If src contains invalid ascii85 data, Decode will return the
// number of bytes successfully written and a CorruptInputError.
// Decode ignores space and control characters in src.
// Often, ascii85-encoded data is wrapped in <~ and ~> symbols.
// Decode expects these to have been stripped by the caller.
//
// If flush is true, Decode assumes that src represents the
// end of the input stream and processes it completely rather
// than wait for the completion of another 32-bit block.
//
// NewDecoder wraps an io.Reader interface around Decode.
//
func Decode(dst, src []byte, flush bool) (ndst, nsrc int, err error) {}

// NewDecoder constructs a new ascii85 stream decoder.
func NewDecoder(r io.Reader) io.Reader {}

type decoder struct {
	err     error
	readErr error
	r       io.Reader
	buf     [1024]byte // leftover input
	nbuf    int
	out     []byte // leftover decoded output
	outbuf  [1024]byte
}

func (d *decoder) Read(p []byte) (n int, err error) {}
