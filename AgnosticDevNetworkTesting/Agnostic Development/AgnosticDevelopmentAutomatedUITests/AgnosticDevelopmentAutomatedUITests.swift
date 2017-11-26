//
//  AgnosticDevelopmentAutomatedUITests.swift
//  AgnosticDevelopmentAutomatedUITests
//
//  Created by Matt Eaton on 11/6/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import XCTest
import Foundation

class AgnosticDevelopmentAutomatedUITests: XCTestCase {
    
    var app: XCUIApplication!
    var buttonIDs: [String] = []
    
    override func setUp() {
        super.setUp()
        NSLog("setUp")
        // Parse the comma separated TEST_ARGs variable
        if let BUTTON_ID_ARGS = ProcessInfo.processInfo.environment["BUTTON_ID_ARGS"] {
            buttonIDs = BUTTON_ID_ARGS.components(separatedBy: ",")
            NSLog("BUTTON_ID_ARGS: \(BUTTON_ID_ARGS)")
            NSLog("Launch Data BUTTON_ID_ARGS Count: \(buttonIDs.count)")
        } else {
            // If you do not get any test args, assert failure
            XCTAssert(false, "FAIL: No data found in BUTTON_ID_ARGS")
        }
        
        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false
        app = XCUIApplication()

    }
    
    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
    
    func testCommandLineData() {

        app.launch()
        NSLog("Passed in data: \(buttonIDs[0])")
        // Assert that we are displaying the button
        let unknownButton = app.tables[buttonIDs[0]]
        
        unknownButton.tap()
        XCTAssertTrue(true, "Reached the end with success")
    }
    
}
