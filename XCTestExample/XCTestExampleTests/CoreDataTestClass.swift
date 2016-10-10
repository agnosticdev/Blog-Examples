//
//  CoreDataTestClass.swift
//  XCTestExample
//
//  Created by Matt Eaton on 10/8/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import XCTest
import CoreData

class CoreDataTestClass: XCTestCase {
    
    // Create a local NSManagedObjectContext
    var managedObjectContext: NSManagedObjectContext? = nil
    
    // In iOS 10 and Swift 3 this is all I need to create my core data stack
    lazy var persistentContainer: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "XCTestExample")
        container.loadPersistentStores(completionHandler: { (storeDescription, error) in
            if let error = error as NSError? {
                fatalError("Unresolved error \(error), \(error.userInfo)")
            }
        })
        return container
    }()
    
    override func tearDown() {
        super.tearDown()
        managedObjectContext = nil
    }
    
    override func setUp() {
        super.setUp()
        // Set the NSManagedObjectContext with the view Context
        managedObjectContext = self.persistentContainer.viewContext
    }
    
    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }
    
    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }
}
