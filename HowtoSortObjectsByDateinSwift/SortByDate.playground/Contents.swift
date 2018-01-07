//: Playground - noun: a place where people can play

import Cocoa

class customObject: NSObject {
    
    var title: String = ""
    var desc: String = ""
    var date: Date = Date()
    
    required init(title: String, desc: String, dateString: String) {
        // Set the title and description
        self.title = title
        self.desc = desc
        
        // Set the date formatter and optionally set the formatted date from string
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "MMMM d, yyyy"
        if let date = dateFormatter.date(from: dateString) {
            self.date = date
        }
    }
}
// Create 5 sample objects for testing, all with sporadic dates
var obj3 = customObject(title: "TLS 1.3 - Better, Stronger, Faster", desc: "Overview of TLS 1.3", dateString: "January 6, 2018")
var obj4 = customObject(title: "User Interface Testing with Swift and XCTest", desc: "Overview of UI Testing", dateString: "December 10, 2017")
var obj2 = customObject(title: "How to Use Python List Comprehensions", desc: "Overview of Python List Comprehensions", dateString: "December 2, 2017")
var obj1 = customObject(title: "Attending WWDC 2017 - Predictions Answered", desc: "Predictions Answered on WWDC 2017", dateString: "June 13, 2017")
var obj5 = customObject(title: "Swift Network Testing - Automate XCTest with Python", desc: "Automate XCTest with Python", dateString: "November 26, 2017")

// Display the dates and titles
print("Unsorted Date from obj1: \(obj1.date) with title: \(obj1.title)")
print("Unsorted Date from obj2: \(obj2.date) with title: \(obj2.title)")
print("Unsorted Date from obj3: \(obj3.date) with title: \(obj3.title)")
print("Unsorted Date from obj4: \(obj4.date) with title: \(obj4.title)")
print("Unsorted Date from obj5: \(obj5.date) with title: \(obj5.title)\n")

// Now, with 3 short lines of code is where the magic happens
// First the objects are wrapped up in a generic array
var customObjects = [obj1, obj2, obj3, obj4, obj5]
// Next, the .sorted(by:) method returns a collection that compares an element in the array against the next element and arranges the collection by date.
// The sorted collection is assigned back to the customObjects array for display
customObjects = customObjects.sorted(by: {
    $0.date.compare($1.date) == .orderedDescending
})
// The sorted customObjects collection is then printed out to display the objects sorted descending by date
for obj in customObjects {
    print("Sorted Date: \(obj.date) with title: \(obj.title)")
}


