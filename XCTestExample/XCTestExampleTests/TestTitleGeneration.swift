//
//  TestTitleGeneration.swift
//  XCTestExample
//
//  Created by Matt Eaton on 10/8/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import UIKit
import XCTest
@testable import XCTestExample

class TestTitleGeneration: XCTestCase {
    
    let master = MasterViewController()
    
    override func setUp() {
        super.setUp()
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }
    
    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
    
    func testRandomTitle() {

        // Declare two constant lengths for random string generation length
        let firstTestLength = 10
        let secondTestLength = 15
        
        // Get the first string
        let firstString = master.getRandomString(stringLength: firstTestLength)
        XCTAssertEqual(firstString.characters.count, firstTestLength, "First string characters should equal \(firstTestLength)")
        // Get the second string
        let secondString = master.getRandomString(stringLength: secondTestLength)
        XCTAssertEqual(secondString.characters.count, secondTestLength, "Second string characters should equal \(secondTestLength)")
        
    }
    
    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }
    
}
