// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

/*
Package mail implements parsing of mail messages.

For the most part, this package follows the syntax as specified by RFC 5322 and
extended by RFC 6532.
Notable divergences:
	* Obsolete address formats are not parsed, including addresses with
	  embedded route information.
	* The full range of spacing (the CFWS syntax element) is not supported,
	  such as breaking addresses across lines.
	* No unicode normalization is performed.
	* The special characters ()[]:;@\, are allowed to appear unquoted in names.
*/
package mail

import (
	"errors"
	"io"
	"mime"
	"time"
)

// A Message represents a parsed mail message.
type Message struct {
	Header Header
	Body   io.Reader
}

// ReadMessage reads a message from r.
// The headers are parsed, and the body of the message will be available
// for reading from msg.Body.
func ReadMessage(r io.Reader) (msg *Message, err error) {}
/*
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/mail"
	"strings"
)

func main() {
	msg := `Date: Mon, 23 Jun 2015 11:40:36 -0400
From: Gopher <from@example.com>
To: Another Gopher <to@example.com>
Subject: Gophers at Gophercon

Message body
`

	r := strings.NewReader(msg)
	m, err := mail.ReadMessage(r)
	if err != nil {
		log.Fatal(err)
	}

	header := m.Header
	fmt.Println("Date:", header.Get("Date"))
	fmt.Println("From:", header.Get("From"))
	fmt.Println("To:", header.Get("To"))
	fmt.Println("Subject:", header.Get("Subject"))

	body, err := ioutil.ReadAll(m.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", body)

}
*/

// ParseDate parses an RFC 5322 date string.
func ParseDate(date string) (time.Time, error) {}

// A Header represents the key-value pairs in a mail message header.
type Header map[string][]string

// Get gets the first value associated with the given key.
// It is case insensitive; CanonicalMIMEHeaderKey is used
// to canonicalize the provided key.
// If there are no values associated with the key, Get returns "".
// To access multiple values of a key, or to use non-canonical keys,
// access the map directly.
func (h Header) Get(key string) string {}

var ErrHeaderNotPresent = errors.New("mail: header not in message")

// Date parses the Date header field.
func (h Header) Date() (time.Time, error) {}

// AddressList parses the named header field as a list of addresses.
func (h Header) AddressList(key string) ([]*Address, error) {}

// Address represents a single mail address.
// An address such as "Barry Gibbs <bg@example.com>" is represented
// as Address{Name: "Barry Gibbs", Address: "bg@example.com"}.
type Address struct {
	Name    string // Proper name; may be empty.
	Address string // user@domain
}

// ParseAddress parses a single RFC 5322 address, e.g. "Barry Gibbs <bg@example.com>"
func ParseAddress(address string) (*Address, error) {}
/*
package main

import (
	"fmt"
	"log"
	"net/mail"
)

func main() {
	e, err := mail.ParseAddress("Alice <alice@example.com>")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(e.Name, e.Address)

}
*/

// ParseAddressList parses the given string as a list of addresses.
func ParseAddressList(list string) ([]*Address, error) {}
/*
package main

import (
	"fmt"
	"log"
	"net/mail"
)

func main() {
	const list = "Alice <alice@example.com>, Bob <bob@example.com>, Eve <eve@example.com>"
	emails, err := mail.ParseAddressList(list)
	if err != nil {
		log.Fatal(err)
	}

	for _, v := range emails {
		fmt.Println(v.Name, v.Address)
	}

}
*/

// An AddressParser is an RFC 5322 address parser.
type AddressParser struct {
	// WordDecoder optionally specifies a decoder for RFC 2047 encoded-words.
	WordDecoder *mime.WordDecoder
}

// Parse parses a single RFC 5322 address of the
// form "Gogh Fir <gf@example.com>" or "foo@example.com".
func (p *AddressParser) Parse(address string) (*Address, error) {}

// ParseList parses the given string as a list of comma-separated addresses
// of the form "Gogh Fir <gf@example.com>" or "foo@example.com".
func (p *AddressParser) ParseList(list string) ([]*Address, error) {}

// String formats the address as a valid RFC 5322 address.
// If the address's name contains non-ASCII characters
// the name will be rendered according to RFC 2047.
func (a *Address) String() string {}
