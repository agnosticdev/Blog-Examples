//
//  Article.swift
//  MVVM Sample
//
//  Created by Matt Eaton on 10/28/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import Foundation

// Simple Article Model Object
class Article {
    
    var title: String
    var date: Date
    var image: Data
    
    init(title: String, date: Date, image: Data) {
        
        self.title = title
        self.date = date
        self.image = image
    }
}
