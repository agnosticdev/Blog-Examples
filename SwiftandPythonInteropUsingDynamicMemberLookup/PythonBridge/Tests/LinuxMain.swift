import XCTest

import PythonBridgeTests

var tests = [XCTestCaseEntry]()
tests += PythonBridgeTests.allTests()
XCTMain(tests)