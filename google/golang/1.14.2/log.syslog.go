// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package syslog provides a simple interface to the system log
// service. It can send messages to the syslog daemon using UNIX
// domain sockets, UDP or TCP.
//
// Only one call to Dial is necessary. On write failures,
// the syslog client will attempt to reconnect to the server
// and write again.
//
// The syslog package is frozen and is not accepting new features.
// Some external packages provide more functionality. See:
//
//   https://godoc.org/?q=syslog
package syslog

// BUG(brainman): This package is not implemented on Windows. As the
// syslog package is frozen, Windows users are encouraged to
// use a package outside of the standard library. For background,
// see https://golang.org/issue/1108.

// BUG(akumar): This package is not implemented on Plan 9.

import (
	"log"
	"sync"
)

// The Priority is a combination of the syslog facility and
// severity. For example, LOG_ALERT | LOG_FTP sends an alert severity
// message from the FTP facility. The default severity is LOG_EMERG;
// the default facility is LOG_KERN.
type Priority int

const (
	// Severity.

	// From /usr/include/sys/syslog.h.
	// These are the same on Linux, BSD, and OS X.
	LOG_EMERG Priority = iota
	LOG_ALERT
	LOG_CRIT
	LOG_ERR
	LOG_WARNING
	LOG_NOTICE
	LOG_INFO
	LOG_DEBUG
)

const (
	// Facility.

	// From /usr/include/sys/syslog.h.
	// These are the same up to LOG_FTP on Linux, BSD, and OS X.
	LOG_KERN Priority = iota << 3
	LOG_USER
	LOG_MAIL
	LOG_DAEMON
	LOG_AUTH
	LOG_SYSLOG
	LOG_LPR
	LOG_NEWS
	LOG_UUCP
	LOG_CRON
	LOG_AUTHPRIV
	LOG_FTP
	_ // unused
	_ // unused
	_ // unused
	_ // unused
	LOG_LOCAL0
	LOG_LOCAL1
	LOG_LOCAL2
	LOG_LOCAL3
	LOG_LOCAL4
	LOG_LOCAL5
	LOG_LOCAL6
	LOG_LOCAL7
)

// A Writer is a connection to a syslog server.
type Writer struct {
	priority Priority
	tag      string
	hostname string
	network  string
	raddr    string

	mu   sync.Mutex // guards conn
	conn serverConn
}

// New establishes a new connection to the system log daemon. Each
// write to the returned writer sends a log message with the given
// priority (a combination of the syslog facility and severity) and
// prefix tag. If tag is empty, the os.Args[0] is used.
func New(priority Priority, tag string) (*Writer, error) {}

// Dial establishes a connection to a log daemon by connecting to
// address raddr on the specified network. Each write to the returned
// writer sends a log message with the facility and severity
// (from priority) and tag. If tag is empty, the os.Args[0] is used.
// If network is empty, Dial will connect to the local syslog server.
// Otherwise, see the documentation for net.Dial for valid values
// of network and raddr.
func Dial(network, raddr string, priority Priority, tag string) (*Writer, error) {}
/*
package main

import (
	"fmt"
	"log"
	"log/syslog"
)

func main() {
	sysLog, err := syslog.Dial("tcp", "localhost:1234",
		syslog.LOG_WARNING|syslog.LOG_DAEMON, "demotag")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Fprintf(sysLog, "This is a daemon warning with demotag.")
	sysLog.Emerg("And this is a daemon emergency with demotag.")
}
*/

// Write sends a log message to the syslog daemon.
func (w *Writer) Write(b []byte) (int, error) {}

// Close closes a connection to the syslog daemon.
func (w *Writer) Close() error {}

// Emerg logs a message with severity LOG_EMERG, ignoring the severity
// passed to New.
func (w *Writer) Emerg(m string) error {}

// Alert logs a message with severity LOG_ALERT, ignoring the severity
// passed to New.
func (w *Writer) Alert(m string) error {}

// Crit logs a message with severity LOG_CRIT, ignoring the severity
// passed to New.
func (w *Writer) Crit(m string) error {}

// Err logs a message with severity LOG_ERR, ignoring the severity
// passed to New.
func (w *Writer) Err(m string) error {}

// Warning logs a message with severity LOG_WARNING, ignoring the
// severity passed to New.
func (w *Writer) Warning(m string) error {}

// Notice logs a message with severity LOG_NOTICE, ignoring the
// severity passed to New.
func (w *Writer) Notice(m string) error {}

// Info logs a message with severity LOG_INFO, ignoring the severity
// passed to New.
func (w *Writer) Info(m string) error {}

// Debug logs a message with severity LOG_DEBUG, ignoring the severity
// passed to New.
func (w *Writer) Debug(m string) error {}

// NewLogger creates a log.Logger whose output is written to the
// system log service with the specified priority, a combination of
// the syslog facility and severity. The logFlag argument is the flag
// set passed through to log.New to create the Logger.
func NewLogger(p Priority, logFlag int) (*log.Logger, error) {}
