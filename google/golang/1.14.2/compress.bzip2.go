// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package bzip2 implements bzip2 decompression.
package bzip2 // compress/bzip2

import "io"

// There's no RFC for bzip2. I used the Wikipedia page for reference and a lot
// of guessing: https://en.wikipedia.org/wiki/Bzip2
// The source code to pyflate was useful for debugging:
// http://www.paul.sladen.org/projects/pyflate

// A StructuralError is returned when the bzip2 data is found to be
// syntactically invalid.
type StructuralError string

func (s StructuralError) Error() string {}

// NewReader returns an io.Reader which decompresses bzip2 data from r.
// If r does not also implement io.ByteReader,
// the decompressor may read more data than necessary from r.
func NewReader(r io.Reader) io.Reader {}
