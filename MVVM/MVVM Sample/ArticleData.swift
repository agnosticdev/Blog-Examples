//
//  ArticleData.swift
//  MVVM Sample
//
//  Created by Matt Eaton on 10/28/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import Foundation

class ArticleData {
    
    // For sake of example this class is used to setup an array to hold articles in memory
    // Normally this would be some sort of persistent data storage object
    var articles = [Article]()
    
    func sortArticleDataAlpha() ->[Article] {
        return self.articles.sorted(by: { $0.title < $1.title })
    }
    
    func sortArticleDataByDate() ->[Article] {
        return self.articles.sorted(by: { $0.date < $1.date })
    }
    
    init (articles: [Article]) {
        self.articles = articles
    }
}
