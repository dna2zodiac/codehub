// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package quotedprintable implements quoted-printable encoding as specified by
// RFC 2045.
package quotedprintable

import (
	"bufio"
	"io"
)

// Reader is a quoted-printable decoder.
type Reader struct {
	br   *bufio.Reader
	rerr error  // last read error
	line []byte // to be consumed before more of br
}

// NewReader returns a quoted-printable reader, decoding from r.
func NewReader(r io.Reader) *Reader {}
/*
package main

import (
	"fmt"
	"io/ioutil"
	"mime/quotedprintable"
	"strings"
)

func main() {
	for _, s := range []string{
		`=48=65=6C=6C=6F=2C=20=47=6F=70=68=65=72=73=21`,
		`invalid escape: <b style="font-size: 200%">hello</b>`,
		"Hello, Gophers! This symbol will be unescaped: =3D and this will be written in =\r\none line.",
	} {
		b, err := ioutil.ReadAll(quotedprintable.NewReader(strings.NewReader(s)))
		fmt.Printf("%s %v\n", b, err)
	}
}
*/

// Read reads and decodes quoted-printable data from the underlying reader.
func (r *Reader) Read(p []byte) (n int, err error) {}

// A Writer is a quoted-printable writer that implements io.WriteCloser.
type Writer struct {
	// Binary mode treats the writer's input as pure binary and processes end of
	// line bytes as binary data.
	Binary bool

	w    io.Writer
	i    int
	line [78]byte
	cr   bool
}

// NewWriter returns a new Writer that writes to w.
func NewWriter(w io.Writer) *Writer {}
/*
package main

import (
	"mime/quotedprintable"
	"os"
)

func main() {
	w := quotedprintable.NewWriter(os.Stdout)
	w.Write([]byte("These symbols will be escaped: = \t"))
	w.Close()

}
*/

// Write encodes p using quoted-printable encoding and writes it to the
// underlying io.Writer. It limits line length to 76 characters. The encoded
// bytes are not necessarily flushed until the Writer is closed.
func (w *Writer) Write(p []byte) (n int, err error) {}

// Close closes the Writer, flushing any unwritten data to the underlying
// io.Writer, but does not close the underlying io.Writer.
func (w *Writer) Close() error {}
