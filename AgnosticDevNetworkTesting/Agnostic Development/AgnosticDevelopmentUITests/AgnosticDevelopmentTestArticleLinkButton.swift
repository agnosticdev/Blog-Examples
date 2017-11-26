//
//  AgnosticDevelopmentTestArticleLinkButton.swift
//  AgnosticDevelopmentUITests
//
//  Created by Matt Eaton on 10/23/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import XCTest

class AgnosticDevelopmentTestArticleLinkButton: XCTestCase {
    
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
    
    func testArticleButton() {
        app.launch()
        
        // Assert that we are displaying the tableview
        let articleTableView = app.tables["table--articleTableView"]
        
        XCTAssertTrue(articleTableView.exists, "The article tableview exists")
        
        // Get an array of cells
        let tableCells = articleTableView.cells
        print("Count of table cells \(tableCells.count)")
        
        if tableCells.count > 0 {
            // Grab the first cell and verify that it exists and tap it
            let cellZero = tableCells.element(boundBy: 0)
            XCTAssertTrue(cellZero.exists, "The first cell is in place on the table")
            // Does this actually take us to the next screen
            cellZero.tap()
            // This verifies that our article title label exists
            let articleButton = app.buttons["button--articleLinkButton"]
            XCTAssertTrue(articleButton.exists, "Validating article button")
            // Attempt to open the article button in safari
            articleButton.tap()
            // If we make it here we can assume that the article was opened successfully
            XCTAssertTrue(true, "Opening the article was successful")
            
        } else {
            XCTAssert(false, "Was not able to find any table cells")
        }
    }
    
}
