# PythonBridge

Swift library that calls into a Python module to perform some computations or actions and then passes the data back to Swift for display, if needed.  An example here would be crunching some numbers on a website (Vapor) and then displaying the computed values in a web application.

**NOTE** The PythonBridge.swift file in this library was not originally written by me.  I refactored it for demostration purposes, but did not originally write it.  This file was an example file used to supported the [Dynamic Member Lookup](https://forums.swift.org/t/se-0195-introduce-user-defined-dynamic-member-lookup-types/8658) proposal originally and all credit for this file should be given to the Swift Community.  Having said that, if you are wanting to build your own Python Bridge using Python's C extensions and expose it to Swift, please get in contact with me.  I would love to help.


This library has been tested using Python 2.7 and Swift 4.2 on Ubuntu 16.04 and macOS 10.13.
