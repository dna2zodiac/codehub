// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package url parses URLs and implements query escaping.
package url

// See RFC 3986. This package generally follows RFC 3986, except where
// it deviates for compatibility reasons. When sending changes, first
// search old issues for history on decisions. Unit tests should also
// contain references to issue numbers with details.

import (
	"errors"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

// Error reports an error and the operation and URL that caused it.
type Error struct {
	Op  string
	URL string
	Err error
}

func (e *Error) Unwrap() error {}
func (e *Error) Error() string {}

func (e *Error) Timeout() bool {}

func (e *Error) Temporary() bool {}

type EscapeError string

func (e EscapeError) Error() string {}

type InvalidHostError string

func (e InvalidHostError) Error() string {}

// QueryUnescape does the inverse transformation of QueryEscape,
// converting each 3-byte encoded substring of the form "%AB" into the
// hex-decoded byte 0xAB.
// It returns an error if any % is not followed by two hexadecimal
// digits.
func QueryUnescape(s string) (string, error) {}

// PathUnescape does the inverse transformation of PathEscape,
// converting each 3-byte encoded substring of the form "%AB" into the
// hex-decoded byte 0xAB. It returns an error if any % is not followed
// by two hexadecimal digits.
//
// PathUnescape is identical to QueryUnescape except that it does not
// unescape '+' to ' ' (space).
func PathUnescape(s string) (string, error) {}

// QueryEscape escapes the string so it can be safely placed
// inside a URL query.
func QueryEscape(s string) string {}

// PathEscape escapes the string so it can be safely placed inside a URL path segment,
// replacing special characters (including /) with %XX sequences as needed.
func PathEscape(s string) string {}

// A URL represents a parsed URL (technically, a URI reference).
//
// The general form represented is:
//
//	[scheme:][//[userinfo@]host][/]path[?query][#fragment]
//
// URLs that do not start with a slash after the scheme are interpreted as:
//
//	scheme:opaque[?query][#fragment]
//
// Note that the Path field is stored in decoded form: /%47%6f%2f becomes /Go/.
// A consequence is that it is impossible to tell which slashes in the Path were
// slashes in the raw URL and which were %2f. This distinction is rarely important,
// but when it is, the code should use RawPath, an optional field which only gets
// set if the default encoding is different from Path.
//
// URL's String method uses the EscapedPath method to obtain the path. See the
// EscapedPath method for more details.
type URL struct {
	Scheme     string
	Opaque     string    // encoded opaque data
	User       *Userinfo // username and password information
	Host       string    // host or host:port
	Path       string    // path (relative paths may omit leading slash)
	RawPath    string    // encoded path hint (see EscapedPath method)
	ForceQuery bool      // append a query ('?') even if RawQuery is empty
	RawQuery   string    // encoded query values, without '?'
	Fragment   string    // fragment for references, without '#'
}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("http://bing.com/search?q=dotnet")
	if err != nil {
		log.Fatal(err)
	}
	u.Scheme = "https"
	u.Host = "google.com"
	q := u.Query()
	q.Set("q", "golang")
	u.RawQuery = q.Encode()
	fmt.Println(u)
}
*/
/* Roundtrip
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	// Parse + String preserve the original encoding.
	u, err := url.Parse("https://example.com/foo%2fbar")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(u.Path)
	fmt.Println(u.RawPath)
	fmt.Println(u.String())
}
*/

// User returns a Userinfo containing the provided username
// and no password set.
func User(username string) *Userinfo {}

// UserPassword returns a Userinfo containing the provided username
// and password.
//
// This functionality should only be used with legacy web sites.
// RFC 2396 warns that interpreting Userinfo this way
// ``is NOT RECOMMENDED, because the passing of authentication
// information in clear text (such as URI) has proven to be a
// security risk in almost every case where it has been used.''
func UserPassword(username, password string) *Userinfo {}

// The Userinfo type is an immutable encapsulation of username and
// password details for a URL. An existing Userinfo value is guaranteed
// to have a username set (potentially empty, as allowed by RFC 2396),
// and optionally a password.
type Userinfo struct {
	username    string
	password    string
	passwordSet bool
}

// Username returns the username.
func (u *Userinfo) Username() string {}

// Password returns the password in case it is set, and whether it is set.
func (u *Userinfo) Password() (string, bool) {}

// String returns the encoded userinfo information in the standard form
// of "username[:password]".
func (u *Userinfo) String() string {}

// Parse parses rawurl into a URL structure.
//
// The rawurl may be relative (a path, without a host) or absolute
// (starting with a scheme). Trying to parse a hostname and path
// without a scheme is invalid but may not necessarily return an
// error, due to parsing ambiguities.
func Parse(rawurl string) (*URL, error) {}

// ParseRequestURI parses rawurl into a URL structure. It assumes that
// rawurl was received in an HTTP request, so the rawurl is interpreted
// only as an absolute URI or an absolute path.
// The string rawurl is assumed not to have a #fragment suffix.
// (Web browsers strip #fragment before sending the URL to a web server.)
func ParseRequestURI(rawurl string) (*URL, error) {}

// EscapedPath returns the escaped form of u.Path.
// In general there are multiple possible escaped forms of any path.
// EscapedPath returns u.RawPath when it is a valid escaping of u.Path.
// Otherwise EscapedPath ignores u.RawPath and computes an escaped
// form on its own.
// The String and RequestURI methods use EscapedPath to construct
// their results.
// In general, code should call EscapedPath instead of
// reading u.RawPath directly.
func (u *URL) EscapedPath() string {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("http://example.com/path with spaces")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(u.EscapedPath())
}
*/

// String reassembles the URL into a valid URL string.
// The general form of the result is one of:
//
//	scheme:opaque?query#fragment
//	scheme://userinfo@host/path?query#fragment
//
// If u.Opaque is non-empty, String uses the first form;
// otherwise it uses the second form.
// Any non-ASCII characters in host are escaped.
// To obtain the path, String uses u.EscapedPath().
//
// In the second form, the following rules apply:
//	- if u.Scheme is empty, scheme: is omitted.
//	- if u.User is nil, userinfo@ is omitted.
//	- if u.Host is empty, host/ is omitted.
//	- if u.Scheme and u.Host are empty and u.User is nil,
//	   the entire scheme://userinfo@host/ is omitted.
//	- if u.Host is non-empty and u.Path begins with a /,
//	   the form host/path does not add its own /.
//	- if u.RawQuery is empty, ?query is omitted.
//	- if u.Fragment is empty, #fragment is omitted.
func (u *URL) String() string {}
/*
package main

import (
	"fmt"
	"net/url"
)

func main() {
	u := &url.URL{
		Scheme:   "https",
		User:     url.UserPassword("me", "pass"),
		Host:     "example.com",
		Path:     "foo/bar",
		RawQuery: "x=1&y=2",
		Fragment: "anchor",
	}
	fmt.Println(u.String())
	u.Opaque = "opaque"
	fmt.Println(u.String())
}
*/

// Values maps a string key to a list of values.
// It is typically used for query parameters and form values.
// Unlike in the http.Header map, the keys in a Values map
// are case-sensitive.
type Values map[string][]string
/*
package main

import (
	"fmt"
	"net/url"
)

func main() {
	v := url.Values{}
	v.Set("name", "Ava")
	v.Add("friend", "Jess")
	v.Add("friend", "Sarah")
	v.Add("friend", "Zoe")
	// v.Encode() == "name=Ava&friend=Jess&friend=Sarah&friend=Zoe"
	fmt.Println(v.Get("name"))
	fmt.Println(v.Get("friend"))
	fmt.Println(v["friend"])
}
*/

// Get gets the first value associated with the given key.
// If there are no values associated with the key, Get returns
// the empty string. To access multiple values, use the map
// directly.
func (v Values) Get(key string) string {}

// Set sets the key to value. It replaces any existing
// values.
func (v Values) Set(key, value string) {}

// Add adds the value to key. It appends to any existing
// values associated with key.
func (v Values) Add(key, value string) {}

// Del deletes the values associated with key.
func (v Values) Del(key string) {}

// ParseQuery parses the URL-encoded query string and returns
// a map listing the values specified for each key.
// ParseQuery always returns a non-nil map containing all the
// valid query parameters found; err describes the first decoding error
// encountered, if any.
//
// Query is expected to be a list of key=value settings separated by
// ampersands or semicolons. A setting without an equals sign is
// interpreted as a key set to an empty value.
func ParseQuery(query string) (Values, error) {}
/*
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/url"
	"strings"
)

func main() {
	m, err := url.ParseQuery(`x=1&y=2&y=3;z`)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(toJSON(m))
}

func toJSON(m interface{}) string {
	js, err := json.Marshal(m)
	if err != nil {
		log.Fatal(err)
	}
	return strings.ReplaceAll(string(js), ",", ", ")
}
*/

// Encode encodes the values into ``URL encoded'' form
// ("bar=baz&foo=quux") sorted by key.
func (v Values) Encode() string {}

// IsAbs reports whether the URL is absolute.
// Absolute means that it has a non-empty scheme.
func (u *URL) IsAbs() bool {}
/*
package main

import (
	"fmt"
	"net/url"
)

func main() {
	u := url.URL{Host: "example.com", Path: "foo"}
	fmt.Println(u.IsAbs())
	u.Scheme = "http"
	fmt.Println(u.IsAbs())
}
*/

// Parse parses a URL in the context of the receiver. The provided URL
// may be relative or absolute. Parse returns nil, err on parse
// failure, otherwise its return value is the same as ResolveReference.
func (u *URL) Parse(ref string) (*URL, error) {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("https://example.org")
	if err != nil {
		log.Fatal(err)
	}
	rel, err := u.Parse("/foo")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(rel)
	_, err = u.Parse(":foo")
	if _, ok := err.(*url.Error); !ok {
		log.Fatal(err)
	}
}
*/

// ResolveReference resolves a URI reference to an absolute URI from
// an absolute base URI u, per RFC 3986 Section 5.2. The URI reference
// may be relative or absolute. ResolveReference always returns a new
// URL instance, even if the returned URL is identical to either the
// base or reference. If ref is an absolute URL, then ResolveReference
// ignores base and returns a copy of ref.
func (u *URL) ResolveReference(ref *URL) *URL {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("../../..//search?q=dotnet")
	if err != nil {
		log.Fatal(err)
	}
	base, err := url.Parse("http://example.com/directory/")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(base.ResolveReference(u))
}
*/

// Query parses RawQuery and returns the corresponding values.
// It silently discards malformed value pairs.
// To check errors use ParseQuery.
func (u *URL) Query() Values {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("https://example.org/?a=1&a=2&b=&=3&&&&")
	if err != nil {
		log.Fatal(err)
	}
	q := u.Query()
	fmt.Println(q["a"])
	fmt.Println(q.Get("b"))
	fmt.Println(q.Get(""))
}
*/

// RequestURI returns the encoded path?query or opaque?query
// string that would be used in an HTTP request for u.
func (u *URL) RequestURI() string {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("https://example.org/path?foo=bar")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(u.RequestURI())
}
*/

// Hostname returns u.Host, stripping any valid port number if present.
//
// If the result is enclosed in square brackets, as literal IPv6 addresses are,
// the square brackets are removed from the result.
func (u *URL) Hostname() string {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("https://example.org:8000/path")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(u.Hostname())
	u, err = url.Parse("https://[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:17000")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(u.Hostname())
}
*/

// Port returns the port part of u.Host, without the leading colon.
//
// If u.Host doesn't contain a valid numeric port, Port returns an empty string.
func (u *URL) Port() string {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, err := url.Parse("https://example.org")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(u.Port())
	u, err = url.Parse("https://example.org:8080")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(u.Port())
}
*/

// Marshaling interface implementations.
// Would like to implement MarshalText/UnmarshalText but that will change the JSON representation of URLs.

func (u *URL) MarshalBinary() (text []byte, err error) {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u, _ := url.Parse("https://example.org")
	b, err := u.MarshalBinary()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s\n", b)
}
*/

func (u *URL) UnmarshalBinary(text []byte) error {}
/*
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	u := &url.URL{}
	err := u.UnmarshalBinary([]byte("https://example.org/foo"))
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s\n", u)
}
*/
