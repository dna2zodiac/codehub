// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package aes // crypto/aes

import (
	"crypto/cipher"
)

// The AES block size in bytes.
const BlockSize = 16

type KeySizeError int

func (k KeySizeError) Error() string {}

// NewCipher creates and returns a new cipher.Block.
// The key argument should be the AES key,
// either 16, 24, or 32 bytes to select
// AES-128, AES-192, or AES-256.
func NewCipher(key []byte) (cipher.Block, error) {}
