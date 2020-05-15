// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package des // crypto/des

import (
	"crypto/cipher"
)

// The DES block size in bytes.
const BlockSize = 8

type KeySizeError int

func (k KeySizeError) Error() string {}

// NewCipher creates and returns a new cipher.Block.
func NewCipher(key []byte) (cipher.Block, error) {}

// NewTripleDESCipher creates and returns a new cipher.Block.
func NewTripleDESCipher(key []byte) (cipher.Block, error) {}
/*
package main

import (
	"crypto/des"
)

func main() {
	// NewTripleDESCipher can also be used when EDE2 is required by
	// duplicating the first 8 bytes of the 16-byte key.
	ede2Key := []byte("example key 1234")

	var tripleDESKey []byte
	tripleDESKey = append(tripleDESKey, ede2Key[:16]...)
	tripleDESKey = append(tripleDESKey, ede2Key[:8]...)

	_, err := des.NewTripleDESCipher(tripleDESKey)
	if err != nil {
		panic(err)
	}

	// See crypto/cipher for how to use a cipher.Block for encryption and
	// decryption.
}
*/
