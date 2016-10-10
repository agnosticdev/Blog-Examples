//
//  TestEventCreation.swift
//  XCTestExample
//
//  Created by Matt Eaton on 10/8/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import XCTest
import CoreData
@testable import XCTestExample

class TestEventCreation: CoreDataTestClass {
    
    var newEvent:Event?
    
    override func setUp() {
        super.setUp()
        let newEventEntity = NSEntityDescription.entity(forEntityName: "Event", in: managedObjectContext!)
        newEvent = Event(entity: newEventEntity!, insertInto: managedObjectContext)
    }
    
    override func tearDown() {
        super.tearDown()
    }
    
    func testNewEvent() {
        XCTAssertNotNil(self.newEvent, "Cannot create a new event!")
    }
    
    override func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }
    
}
