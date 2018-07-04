#
# https://www.openssl.org/source/
# 
# 2018-Jun-20 14:58:10 	openssl-1.1.1-pre8.tar.gz
# (Install for Unix (Linux and macOS))
# ./configure
# make
# make test
# make install 
#
# ./configure --with-pydebug && make -j
#
#

import socket
import ssl
import os
import threading
from test import support
import sys


def handle_error(prefix):
    exc_format = ' '.join(traceback.format_exception(*sys.exc_info()))
    if support.verbose:
        sys.stdout.write(prefix + exc_format)

class ThreadedEchoServer(threading.Thread):

    class ConnectionHandler(threading.Thread):

        """A mildly complicated class, because we want it to work both
        with and without the SSL wrapper around the socket connection, so
        that we can test the STARTTLS functionality."""

        def __init__(self, server, connsock, addr):
            self.server = server
            self.running = False
            self.sock = connsock
            self.addr = addr
            self.sock.setblocking(1)
            self.sslconn = None
            threading.Thread.__init__(self)
            self.daemon = True

        def wrap_conn(self):
            try:
                self.sslconn = self.server.context.wrap_socket(
                    self.sock, server_side=True)
                self.server.selected_npn_protocols.append(self.sslconn.selected_npn_protocol())
                self.server.selected_alpn_protocols.append(self.sslconn.selected_alpn_protocol())
            except (ConnectionResetError, BrokenPipeError) as e:
                # We treat ConnectionResetError as though it were an
                # SSLError - OpenSSL on Ubuntu abruptly closes the
                # connection when asked to use an unsupported protocol.
                #
                # BrokenPipeError is raised in TLS 1.3 mode, when OpenSSL
                # tries to send session tickets after handshake.
                # https://github.com/openssl/openssl/issues/6342
                self.server.conn_errors.append(str(e))
                if self.server.chatty:
                    handle_error("\n server:  bad connection attempt from " + repr(self.addr) + ":\n")
                self.running = False
                self.close()
                return False
            except (ssl.SSLError, OSError) as e:
                # OSError may occur with wrong protocols, e.g. both
                # sides use PROTOCOL_TLS_SERVER.
                #
                # XXX Various errors can have happened here, for example
                # a mismatching protocol version, an invalid certificate,
                # or a low-level bug. This should be made more discriminating.
                #
                # bpo-31323: Store the exception as string to prevent
                # a reference leak: server -> conn_errors -> exception
                # -> traceback -> self (ConnectionHandler) -> server
                self.server.conn_errors.append(str(e))
                if self.server.chatty:
                    handle_error("\n server:  bad connection attempt from " + repr(self.addr) + ":\n")
                self.running = False
                self.server.stop()
                self.close()
                return False
            else:
                self.server.shared_ciphers.append(self.sslconn.shared_ciphers())
                if self.server.context.verify_mode == ssl.CERT_REQUIRED:
                    cert = self.sslconn.getpeercert()
                    if support.verbose and self.server.chatty:
                        sys.stdout.write(" client cert is " + pprint.pformat(cert) + "\n")
                    cert_binary = self.sslconn.getpeercert(True)
                    if support.verbose and self.server.chatty:
                        sys.stdout.write(" cert binary is " + str(len(cert_binary)) + " bytes\n")
                cipher = self.sslconn.cipher()
                if support.verbose and self.server.chatty:
                    sys.stdout.write(" server: connection cipher is now " + str(cipher) + "\n")
                    sys.stdout.write(" server: selected protocol is now "
                            + str(self.sslconn.selected_npn_protocol()) + "\n")
                return True

        def read(self):
            if self.sslconn:
                return self.sslconn.read()
            else:
                return self.sock.recv(1024)

        def write(self, bytes):
            if self.sslconn:
                return self.sslconn.write(bytes)
            else:
                return self.sock.send(bytes)

        def close(self):
            if self.sslconn:
                self.sslconn.close()
            else:
                self.sock.close()

        def run(self):
            self.running = True
            if not self.server.starttls_server:
                if not self.wrap_conn():
                    return
            while self.running:
                try:
                    msg = self.read()
                    stripped = msg.strip()
                    if not stripped:
                        # eof, so quit this handler
                        self.running = False
                        try:
                            self.sock = self.sslconn.unwrap()
                        except OSError:
                            # Many tests shut the TCP connection down
                            # without an SSL shutdown. This causes
                            # unwrap() to raise OSError with errno=0!
                            pass
                        else:
                            self.sslconn = None
                        self.close()
                    elif stripped == b'over':
                        if support.verbose and self.server.connectionchatty:
                            sys.stdout.write(" server: client closed connection\n")
                        self.close()
                        return
                    elif (self.server.starttls_server and
                          stripped == b'STARTTLS'):
                        if support.verbose and self.server.connectionchatty:
                            sys.stdout.write(" server: read STARTTLS from client, sending OK...\n")
                        self.write(b"OK\n")
                        if not self.wrap_conn():
                            return
                    elif (self.server.starttls_server and self.sslconn
                          and stripped == b'ENDTLS'):
                        if support.verbose and self.server.connectionchatty:
                            sys.stdout.write(" server: read ENDTLS from client, sending OK...\n")
                        self.write(b"OK\n")
                        self.sock = self.sslconn.unwrap()
                        self.sslconn = None
                        if support.verbose and self.server.connectionchatty:
                            sys.stdout.write(" server: connection is now unencrypted...\n")
                    elif stripped == b'CB tls-unique':
                        if support.verbose and self.server.connectionchatty:
                            sys.stdout.write(" server: read CB tls-unique from client, sending our CB data...\n")
                        data = self.sslconn.get_channel_binding("tls-unique")
                        self.write(repr(data).encode("us-ascii") + b"\n")
                    else:
                        if (support.verbose and
                            self.server.connectionchatty):
                            ctype = (self.sslconn and "encrypted") or "unencrypted"
                            sys.stdout.write(" server: read %r (%s), sending back %r (%s)...\n"
                                             % (msg, ctype, msg.lower(), ctype))
                        self.write(msg.lower())
                except ConnectionResetError:
                    # XXX: OpenSSL 1.1.1 sometimes raises ConnectionResetError
                    # when connection is not shut down gracefully.
                    if self.server.chatty and support.verbose:
                        sys.stdout.write(
                            " Connection reset by peer: {}\n".format(
                                self.addr)
                        )
                    self.close()
                    self.running = False
                except OSError:
                    if self.server.chatty:
                        handle_error("Test server failure:\n")
                    self.close()
                    self.running = False

                    # normally, we'd just stop here, but for the test
                    # harness, we want to stop the server
                    self.server.stop()

    def __init__(self, certificate=None, ssl_version=None,
                 certreqs=None, cacerts=None,
                 chatty=True, connectionchatty=False, starttls_server=False,
                 npn_protocols=None, alpn_protocols=None,
                 ciphers=None, context=None):
        if context:
            self.context = context
        else:
            self.context = ssl.SSLContext(ssl_version
                                          if ssl_version is not None
                                          else ssl.PROTOCOL_TLS_SERVER)
            self.context.verify_mode = (certreqs if certreqs is not None
                                        else ssl.CERT_NONE)
            if cacerts:
                self.context.load_verify_locations(cacerts)
            if certificate:
                self.context.load_cert_chain(certificate)
            if npn_protocols:
                self.context.set_npn_protocols(npn_protocols)
            if alpn_protocols:
                self.context.set_alpn_protocols(alpn_protocols)
            if ciphers:
                self.context.set_ciphers(ciphers)
        self.chatty = chatty
        self.connectionchatty = connectionchatty
        self.starttls_server = starttls_server
        self.sock = socket.socket()
        self.port = support.bind_port(self.sock)
        self.flag = None
        self.active = False
        self.selected_npn_protocols = []
        self.selected_alpn_protocols = []
        self.shared_ciphers = []
        self.conn_errors = []
        threading.Thread.__init__(self)
        self.daemon = True

    def __enter__(self):
        self.start(threading.Event())
        self.flag.wait()
        return self

    def __exit__(self, *args):
        self.stop()
        self.join()

    def start(self, flag=None):
        self.flag = flag
        threading.Thread.start(self)

    def run(self):
        self.sock.settimeout(0.05)
        self.sock.listen()
        self.active = True
        if self.flag:
            # signal an event
            self.flag.set()
        while self.active:
            try:
                newconn, connaddr = self.sock.accept()
                if support.verbose and self.chatty:
                    sys.stdout.write(' server:  new connection from '
                                     + repr(connaddr) + '\n')
                handler = self.ConnectionHandler(self, newconn, connaddr)
                handler.start()
                handler.join()
            except socket.timeout:
                pass
            except KeyboardInterrupt:
                self.stop()
            except BaseException as e:
                if support.verbose and self.chatty:
                    sys.stdout.write(
                        ' connection handling failed: ' + repr(e) + '\n')

        self.sock.close()

    def stop(self):
        self.active = False


# Small Sample of using new features for ssl in Python 3.7

# Check if OpenSSL has built-in support for the TLS 1.3 protocol.
if ssl.HAS_TLSv1_3:
    print("{0} with support for TLS 1.3"
		  .format(ssl.OPENSSL_VERSION))

    # This example is based off of the unit test for bpo-32947
    # written by 
    # https://github.com/python/cpython/pull/5663/files
    CERTFILE = os.path.join(os.path.dirname(__file__), "keycert.pem")
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(CERTFILE)
    context.options |= (
        ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
    )
    
    with ThreadedEchoServer(context=context) as server:
        with context.wrap_socket(socket.socket()) as s:
            s.connect(('localhost', server.port))
            string = "TLS 1.3 Data"
            # Write data to the socket encoded as bytes 
            s.sendall(str.encode(string))
            # Block and read up to 512 bytes from the read buffer.
            data = s.recv(512)
            print("Decoded data: {0}".format(data.decode()))
            s.close()
            server.stop()

    thread_info = support.threading_setup()
    support.threading_cleanup(*thread_info)
