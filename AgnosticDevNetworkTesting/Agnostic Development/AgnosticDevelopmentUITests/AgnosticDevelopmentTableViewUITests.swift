//
//  AgnosticDevelopmentUITests.swift
//  AgnosticDevelopmentUITests
//
//  Created by Matt Eaton on 10/11/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import XCTest
import Foundation

class AgnosticDevelopmentTableViewUITests: XCTestCase {
    
    var app: XCUIApplication!
        
    override func setUp() {
        super.setUp()
        
        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false
        app = XCUIApplication()
        
    }
    
    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
    
    func testTableInteraction() {
        app.launch()

        // Assert that we are displaying the tableview
        let articleTableView = app.tables["table--articleTableView"]
        
        XCTAssertTrue(articleTableView.exists, "The article tableview exists")
        
        // Get an array of cells
        let tableCells = articleTableView.cells
        print("Count of table cells \(tableCells.count)")
        
        if tableCells.count > 0 {
            let count: Int = (tableCells.count - 1)
            
            let promise = expectation(description: "Wait for table cells")
            
            for i in stride(from: 0, to: count , by: 1) {
                // Grab the first cell and verify that it exists and tap it
                let tableCell = tableCells.element(boundBy: i)
                XCTAssertTrue(tableCell.exists, "The \(i) cell is in place on the table")
                // Does this actually take us to the next screen
                tableCell.tap()
                
                if i == (count - 1) {
                    promise.fulfill()
                }
                // Back
                app.navigationBars.buttons.element(boundBy: 0).tap()
            }
            waitForExpectations(timeout: 20, handler: nil)
            XCTAssertTrue(true, "Finished validating the table cells")
            
        } else {
            XCTAssert(false, "Was not able to find any table cells")
        }
    }
}
