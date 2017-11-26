//
//  AgnosticDevelopmentLatencyTest.swift
//  AgnosticDevelopmentLatencyTest
//
//  Created by Matt Eaton on 9/30/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import XCTest
@testable import Agnostic_Development

class AgnosticDevelopmentLatencyTest: XCTestCase {
    //
    // MARK: Public Constants
    //
    public let urlConfiguration: URLSessionConfiguration = URLSessionConfiguration.default
    //
    // MARK: Public Instance Properties
    //
    public var urls: [String] = []
    public var networkRequests: [URLRequest] = []
    public var networkSessions: [URLSession] = []
    public var results: [String] = []
    
    override func setUp() {
        super.setUp()
        
        // Parse the comma separated TEST_ARGs variable
        if let TEST_ARGS_URLS = ProcessInfo.processInfo.environment["URL_ARGS"] {
            urls = TEST_ARGS_URLS.components(separatedBy: ",")
            NSLog("Launch Data URL Count: \(urls.count)")
        } else {
            // If you do not get any test args, assert failure
            XCTAssert(false, "FAIL: No data found in TEST_ARGS_URLS")
        }
        
        // Put setup code here. This method is called before the invocation of each test method in the class.
        for networkURL in urls {
            guard let networkURLObj = URL(string: networkURL) else {
                return
            }
            var networkRequest = URLRequest(url: networkURLObj)
            networkRequest.httpMethod = "GET"
            networkRequests.append(networkRequest)
            
            let networkSession = URLSession(configuration: urlConfiguration)
            networkSessions.append(networkSession)
        }
    }
    
    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
        
    }
    
    func testFirstNetworkRequestLatency() {
        
        guard let url = networkRequests[0].url,
            networkRequests.count > 0 else {
            return
        }
        let expectation = XCTestExpectation(description: "Download from: \(url)")
        Network.shared.runNetworkingRequests(networkRequest: networkRequests[0], networkSession: networkSessions[0]) {
            (result: String) in
            if result.range(of:"FAIL") != nil {
                XCTAssert(false, "URLDebug: A failing message was found on the first execution of the request. \(result)")
            } else {
                XCTAssert(true, "URLDebug: The first execution was run successfully. \(result)")
            }
            expectation.fulfill()
        }
        
        wait(for: [expectation], timeout: 15.0)
    }
    
    func testSecondNetworkRequestLatency() {
        
        guard let url = networkRequests[1].url,
            networkRequests.count > 0 else {
            return
        }
        
        let expectation = XCTestExpectation(description: "Download from: \(url)")
        Network.shared.runNetworkingRequests(networkRequest: networkRequests[1], networkSession: networkSessions[1]) {
            (result: String) in
            if result.range(of:"FAIL") != nil {
                XCTAssert(false, "URLDebug: A failing message was found on the second execution of the request. \(result)")
            } else {
                XCTAssert(true, "URLDebug: The second execution was run successfully. \(result)")
            }
            expectation.fulfill()
        }
        wait(for: [expectation], timeout: 15.0)
    }
    
    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }
}
