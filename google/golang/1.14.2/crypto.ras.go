// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package rsa implements RSA encryption as specified in PKCS#1.
//
// RSA is a single, fundamental operation that is used in this package to
// implement either public-key encryption or public-key signatures.
//
// The original specification for encryption and signatures with RSA is PKCS#1
// and the terms "RSA encryption" and "RSA signatures" by default refer to
// PKCS#1 version 1.5. However, that specification has flaws and new designs
// should use version two, usually called by just OAEP and PSS, where
// possible.
//
// Two sets of interfaces are included in this package. When a more abstract
// interface isn't necessary, there are functions for encrypting/decrypting
// with v1.5/OAEP and signing/verifying with v1.5/PSS. If one needs to abstract
// over the public-key primitive, the PrivateKey struct implements the
// Decrypter and Signer interfaces from the crypto package.
//
// The RSA operations in this package are not implemented using constant-time algorithms.
package rsa // crypto/rsa

import (
	"crypto"
	"errors"
	"hash"
	"io"
	"math/big"
)

// A PublicKey represents the public part of an RSA key.
type PublicKey struct {
	N *big.Int // modulus
	E int      // public exponent
}

// Size returns the modulus size in bytes. Raw signatures and ciphertexts
// for or by this public key will have the same size.
func (pub *PublicKey) Size() int {}

// OAEPOptions is an interface for passing options to OAEP decryption using the
// crypto.Decrypter interface.
type OAEPOptions struct {
	// Hash is the hash function that will be used when generating the mask.
	Hash crypto.Hash
	// Label is an arbitrary byte string that must be equal to the value
	// used when encrypting.
	Label []byte
}

var (
	errPublicModulus       = errors.New("crypto/rsa: missing public modulus")
	errPublicExponentSmall = errors.New("crypto/rsa: public exponent too small")
	errPublicExponentLarge = errors.New("crypto/rsa: public exponent too large")
)

// A PrivateKey represents an RSA key
type PrivateKey struct {
	PublicKey            // public part.
	D         *big.Int   // private exponent
	Primes    []*big.Int // prime factors of N, has >= 2 elements.

	// Precomputed contains precomputed values that speed up private
	// operations, if available.
	Precomputed PrecomputedValues
}

// Public returns the public key corresponding to priv.
func (priv *PrivateKey) Public() crypto.PublicKey {}

// Sign signs digest with priv, reading randomness from rand. If opts is a
// *PSSOptions then the PSS algorithm will be used, otherwise PKCS#1 v1.5 will
// be used.
//
// This method implements crypto.Signer, which is an interface to support keys
// where the private part is kept in, for example, a hardware module. Common
// uses should use the Sign* functions in this package directly.
func (priv *PrivateKey) Sign(rand io.Reader, digest []byte, opts crypto.SignerOpts) ([]byte, error) {}

// Decrypt decrypts ciphertext with priv. If opts is nil or of type
// *PKCS1v15DecryptOptions then PKCS#1 v1.5 decryption is performed. Otherwise
// opts must have type *OAEPOptions and OAEP decryption is done.
func (priv *PrivateKey) Decrypt(rand io.Reader, ciphertext []byte, opts crypto.DecrypterOpts) (plaintext []byte, err error) {}

type PrecomputedValues struct {
	Dp, Dq *big.Int // D mod (P-1) (or mod Q-1)
	Qinv   *big.Int // Q^-1 mod P

	// CRTValues is used for the 3rd and subsequent primes. Due to a
	// historical accident, the CRT for the first two primes is handled
	// differently in PKCS#1 and interoperability is sufficiently
	// important that we mirror this.
	CRTValues []CRTValue
}

// CRTValue contains the precomputed Chinese remainder theorem values.
type CRTValue struct {
	Exp   *big.Int // D mod (prime-1).
	Coeff *big.Int // R·Coeff ≡ 1 mod Prime.
	R     *big.Int // product of primes prior to this (inc p and q).
}

// Validate performs basic sanity checks on the key.
// It returns nil if the key is valid, or else an error describing a problem.
func (priv *PrivateKey) Validate() error {}

// GenerateKey generates an RSA keypair of the given bit size using the
// random source random (for example, crypto/rand.Reader).
func GenerateKey(random io.Reader, bits int) (*PrivateKey, error) {}

// GenerateMultiPrimeKey generates a multi-prime RSA keypair of the given bit
// size and the given random source, as suggested in [1]. Although the public
// keys are compatible (actually, indistinguishable) from the 2-prime case,
// the private keys are not. Thus it may not be possible to export multi-prime
// private keys in certain formats or to subsequently import them into other
// code.
//
// Table 1 in [2] suggests maximum numbers of primes for a given size.
//
// [1] US patent 4405829 (1972, expired)
// [2] http://www.cacr.math.uwaterloo.ca/techreports/2006/cacr2006-16.pdf
func GenerateMultiPrimeKey(random io.Reader, nprimes int, bits int) (*PrivateKey, error) {}

// ErrMessageTooLong is returned when attempting to encrypt a message which is
// too large for the size of the public key.
var ErrMessageTooLong = errors.New("crypto/rsa: message too long for RSA public key size")

// EncryptOAEP encrypts the given message with RSA-OAEP.
//
// OAEP is parameterised by a hash function that is used as a random oracle.
// Encryption and decryption of a given message must use the same hash function
// and sha256.New() is a reasonable choice.
//
// The random parameter is used as a source of entropy to ensure that
// encrypting the same message twice doesn't result in the same ciphertext.
//
// The label parameter may contain arbitrary data that will not be encrypted,
// but which gives important context to the message. For example, if a given
// public key is used to decrypt two types of messages then distinct label
// values could be used to ensure that a ciphertext for one purpose cannot be
// used for another by an attacker. If not required it can be empty.
//
// The message must be no longer than the length of the public modulus minus
// twice the hash length, minus a further 2.
func EncryptOAEP(hash hash.Hash, random io.Reader, pub *PublicKey, msg []byte, label []byte) ([]byte, error) {}
/*
secretMessage := []byte("send reinforcements, we're going to advance")
label := []byte("orders")

// crypto/rand.Reader is a good source of entropy for randomizing the
// encryption function.
rng := rand.Reader

ciphertext, err := EncryptOAEP(sha256.New(), rng, &test2048Key.PublicKey, secretMessage, label)
if err != nil {
    fmt.Fprintf(os.Stderr, "Error from encryption: %s\n", err)
    return
}

// Since encryption is a randomized function, ciphertext will be
// different each time.
fmt.Printf("Ciphertext: %x\n", ciphertext)
*/

// ErrDecryption represents a failure to decrypt a message.
// It is deliberately vague to avoid adaptive attacks.
var ErrDecryption = errors.New("crypto/rsa: decryption error")

// ErrVerification represents a failure to verify a signature.
// It is deliberately vague to avoid adaptive attacks.
var ErrVerification = errors.New("crypto/rsa: verification error")

// Precompute performs some calculations that speed up private key operations
// in the future.
func (priv *PrivateKey) Precompute() {}

// DecryptOAEP decrypts ciphertext using RSA-OAEP.
//
// OAEP is parameterised by a hash function that is used as a random oracle.
// Encryption and decryption of a given message must use the same hash function
// and sha256.New() is a reasonable choice.
//
// The random parameter, if not nil, is used to blind the private-key operation
// and avoid timing side-channel attacks. Blinding is purely internal to this
// function – the random data need not match that used when encrypting.
//
// The label parameter must match the value given when encrypting. See
// EncryptOAEP for details.
func DecryptOAEP(hash hash.Hash, random io.Reader, priv *PrivateKey, ciphertext []byte, label []byte) ([]byte, error) {}
/*
ciphertext, _ := hex.DecodeString("4d1ee10e8f286390258c51a5e80802844c3e6358ad6690b7285218a7c7ed7fc3a4c7b950fbd04d4b0239cc060dcc7065ca6f84c1756deb71ca5685cadbb82be025e16449b905c568a19c088a1abfad54bf7ecc67a7df39943ec511091a34c0f2348d04e058fcff4d55644de3cd1d580791d4524b92f3e91695582e6e340a1c50b6c6d78e80b4e42c5b4d45e479b492de42bbd39cc642ebb80226bb5200020d501b24a37bcc2ec7f34e596b4fd6b063de4858dbf5a4e3dd18e262eda0ec2d19dbd8e890d672b63d368768360b20c0b6b8592a438fa275e5fa7f60bef0dd39673fd3989cc54d2cb80c08fcd19dacbc265ee1c6014616b0e04ea0328c2a04e73460")
label := []byte("orders")

// crypto/rand.Reader is a good source of entropy for blinding the RSA
// operation.
rng := rand.Reader

plaintext, err := DecryptOAEP(sha256.New(), rng, test2048Key, ciphertext, label)
if err != nil {
    fmt.Fprintf(os.Stderr, "Error from decryption: %s\n", err)
    return
}

fmt.Printf("Plaintext: %s\n", string(plaintext))

// Remember that encryption only provides confidentiality. The
// ciphertext should be signed before authenticity is assumed and, even
// then, consider that messages might be reordered.
*/


// This file implements the PSS signature scheme [1].
//
// [1] https://www.emc.com/collateral/white-papers/h11300-pkcs-1v2-2-rsa-cryptography-standard-wp.pdf

const (
	// PSSSaltLengthAuto causes the salt in a PSS signature to be as large
	// as possible when signing, and to be auto-detected when verifying.
	PSSSaltLengthAuto = 0
	// PSSSaltLengthEqualsHash causes the salt length to equal the length
	// of the hash used in the signature.
	PSSSaltLengthEqualsHash = -1
)

// PSSOptions contains options for creating and verifying PSS signatures.
type PSSOptions struct {
	// SaltLength controls the length of the salt used in the PSS
	// signature. It can either be a number of bytes, or one of the special
	// PSSSaltLength constants.
	SaltLength int

	// Hash, if not zero, overrides the hash function passed to SignPSS.
	// This is the only way to specify the hash function when using the
	// crypto.Signer interface.
	Hash crypto.Hash
}

// SignPSS calculates the signature of hashed using RSASSA-PSS [1].
// Note that hashed must be the result of hashing the input message using the
// given hash function. The opts argument may be nil, in which case sensible
// defaults are used.
func SignPSS(rand io.Reader, priv *PrivateKey, hash crypto.Hash, hashed []byte, opts *PSSOptions) ([]byte, error) {}

// VerifyPSS verifies a PSS signature.
// hashed is the result of hashing the input message using the given hash
// function and sig is the signature. A valid signature is indicated by
// returning a nil error. The opts argument may be nil, in which case sensible
// defaults are used.
func VerifyPSS(pub *PublicKey, hash crypto.Hash, hashed []byte, sig []byte, opts *PSSOptions) error {}

// This file implements encryption and decryption using PKCS#1 v1.5 padding.

// PKCS1v15DecrypterOpts is for passing options to PKCS#1 v1.5 decryption using
// the crypto.Decrypter interface.
type PKCS1v15DecryptOptions struct {
	// SessionKeyLen is the length of the session key that is being
	// decrypted. If not zero, then a padding error during decryption will
	// cause a random plaintext of this length to be returned rather than
	// an error. These alternatives happen in constant time.
	SessionKeyLen int
}

// EncryptPKCS1v15 encrypts the given message with RSA and the padding
// scheme from PKCS#1 v1.5.  The message must be no longer than the
// length of the public modulus minus 11 bytes.
//
// The rand parameter is used as a source of entropy to ensure that
// encrypting the same message twice doesn't result in the same
// ciphertext.
//
// WARNING: use of this function to encrypt plaintexts other than
// session keys is dangerous. Use RSA OAEP in new protocols.
func EncryptPKCS1v15(rand io.Reader, pub *PublicKey, msg []byte) ([]byte, error) {}

// DecryptPKCS1v15 decrypts a plaintext using RSA and the padding scheme from PKCS#1 v1.5.
// If rand != nil, it uses RSA blinding to avoid timing side-channel attacks.
//
// Note that whether this function returns an error or not discloses secret
// information. If an attacker can cause this function to run repeatedly and
// learn whether each instance returned an error then they can decrypt and
// forge signatures as if they had the private key. See
// DecryptPKCS1v15SessionKey for a way of solving this problem.
func DecryptPKCS1v15(rand io.Reader, priv *PrivateKey, ciphertext []byte) ([]byte, error) {}

// DecryptPKCS1v15SessionKey decrypts a session key using RSA and the padding scheme from PKCS#1 v1.5.
// If rand != nil, it uses RSA blinding to avoid timing side-channel attacks.
// It returns an error if the ciphertext is the wrong length or if the
// ciphertext is greater than the public modulus. Otherwise, no error is
// returned. If the padding is valid, the resulting plaintext message is copied
// into key. Otherwise, key is unchanged. These alternatives occur in constant
// time. It is intended that the user of this function generate a random
// session key beforehand and continue the protocol with the resulting value.
// This will remove any possibility that an attacker can learn any information
// about the plaintext.
// See ``Chosen Ciphertext Attacks Against Protocols Based on the RSA
// Encryption Standard PKCS #1'', Daniel Bleichenbacher, Advances in Cryptology
// (Crypto '98).
//
// Note that if the session key is too small then it may be possible for an
// attacker to brute-force it. If they can do that then they can learn whether
// a random value was used (because it'll be different for the same ciphertext)
// and thus whether the padding was correct. This defeats the point of this
// function. Using at least a 16-byte key will protect against this attack.
func DecryptPKCS1v15SessionKey(rand io.Reader, priv *PrivateKey, ciphertext []byte, key []byte) error {}
/*
// crypto/rand.Reader is a good source of entropy for blinding the RSA
// operation.
rng := rand.Reader

// The hybrid scheme should use at least a 16-byte symmetric key. Here
// we read the random key that will be used if the RSA decryption isn't
// well-formed.
key := make([]byte, 32)
if _, err := io.ReadFull(rng, key); err != nil {
    panic("RNG failure")
}

rsaCiphertext, _ := hex.DecodeString("aabbccddeeff")

if err := DecryptPKCS1v15SessionKey(rng, rsaPrivateKey, rsaCiphertext, key); err != nil {
    // Any errors that result will be “public” – meaning that they
    // can be determined without any secret information. (For
    // instance, if the length of key is impossible given the RSA
    // public key.)
    fmt.Fprintf(os.Stderr, "Error from RSA decryption: %s\n", err)
    return
}

// Given the resulting key, a symmetric scheme can be used to decrypt a
// larger ciphertext.
block, err := aes.NewCipher(key)
if err != nil {
    panic("aes.NewCipher failed: " + err.Error())
}

// Since the key is random, using a fixed nonce is acceptable as the
// (key, nonce) pair will still be unique, as required.
var zeroNonce [12]byte
aead, err := cipher.NewGCM(block)
if err != nil {
    panic("cipher.NewGCM failed: " + err.Error())
}
ciphertext, _ := hex.DecodeString("00112233445566")
plaintext, err := aead.Open(nil, zeroNonce[:], ciphertext, nil)
if err != nil {
    // The RSA ciphertext was badly formed; the decryption will
    // fail here because the AES-GCM key will be incorrect.
    fmt.Fprintf(os.Stderr, "Error decrypting: %s\n", err)
    return
}

fmt.Printf("Plaintext: %s\n", string(plaintext))
*/

// SignPKCS1v15 calculates the signature of hashed using
// RSASSA-PKCS1-V1_5-SIGN from RSA PKCS#1 v1.5.  Note that hashed must
// be the result of hashing the input message using the given hash
// function. If hash is zero, hashed is signed directly. This isn't
// advisable except for interoperability.
//
// If rand is not nil then RSA blinding will be used to avoid timing
// side-channel attacks.
//
// This function is deterministic. Thus, if the set of possible
// messages is small, an attacker may be able to build a map from
// messages to signatures and identify the signed messages. As ever,
// signatures provide authenticity, not confidentiality.
func SignPKCS1v15(rand io.Reader, priv *PrivateKey, hash crypto.Hash, hashed []byte) ([]byte, error) {}
/*
// crypto/rand.Reader is a good source of entropy for blinding the RSA
// operation.
rng := rand.Reader

message := []byte("message to be signed")

// Only small messages can be signed directly; thus the hash of a
// message, rather than the message itself, is signed. This requires
// that the hash function be collision resistant. SHA-256 is the
// least-strong hash function that should be used for this at the time
// of writing (2016).
hashed := sha256.Sum256(message)

signature, err := SignPKCS1v15(rng, rsaPrivateKey, crypto.SHA256, hashed[:])
if err != nil {
    fmt.Fprintf(os.Stderr, "Error from signing: %s\n", err)
    return
}

fmt.Printf("Signature: %x\n", signature)
*/

// VerifyPKCS1v15 verifies an RSA PKCS#1 v1.5 signature.
// hashed is the result of hashing the input message using the given hash
// function and sig is the signature. A valid signature is indicated by
// returning a nil error. If hash is zero then hashed is used directly. This
// isn't advisable except for interoperability.
func VerifyPKCS1v15(pub *PublicKey, hash crypto.Hash, hashed []byte, sig []byte) error {}
/*
message := []byte("message to be signed")
signature, _ := hex.DecodeString("ad2766728615cc7a746cc553916380ca7bfa4f8983b990913bc69eb0556539a350ff0f8fe65ddfd3ebe91fe1c299c2fac135bc8c61e26be44ee259f2f80c1530")

// Only small messages can be signed directly; thus the hash of a
// message, rather than the message itself, is signed. This requires
// that the hash function be collision resistant. SHA-256 is the
// least-strong hash function that should be used for this at the time
// of writing (2016).
hashed := sha256.Sum256(message)

err := VerifyPKCS1v15(&rsaPrivateKey.PublicKey, crypto.SHA256, hashed[:], signature)
if err != nil {
    fmt.Fprintf(os.Stderr, "Error from verification: %s\n", err)
    return
}

// signature is a valid signature of message from the public key.
*/
