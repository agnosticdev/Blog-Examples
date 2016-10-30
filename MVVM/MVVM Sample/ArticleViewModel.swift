//
//  ViewModel.swift
//  MVVM Sample
//
//  Created by Matt Eaton on 10/28/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import Foundation

class ArticleViewModel {
    
    // Article Protocol
    weak var articleDelegate: ArticleProtocol?
    // Private Article Object
    private var article: Article?
    var articleData: ArticleData?
    
    // The title for this article
    var titleText: String? {
        // Force unwrap the title as it is an expected value
        return article!.title
    }
    
    // The formatted date for this article
    var dateFormattedString: String? {
        // Unwrap date optional to make sure there is a value
        if let dateVal = article?.date {
            let dateStringFormatter = DateFormatter()
            dateStringFormatter.dateFormat = "dd-MM-yyyy"
            return dateStringFormatter.string(from:dateVal)
        } else {
            // Could return a default value here
            // For sake of example return nil
            return nil
        }
    }
    
    // The image for this article
    var image: Data? {
        // Unwrap image optional to make sure there is a value
        if let imageData = article?.image {
            return imageData
        } else {
            // Could return a default image here
            // For sake of example return nil
            return nil
        }
    }
    
    // I have questions around the placement of this function
    // I am thinking there may be a better place for this function
    // This function calls out to the ArticleData object and gets a sorted array of the article data
    func getArticleData(withFlag: String) {
        
        // This function calls back to the View Controller not using KVO or RAC but a protocol instead
        if withFlag == "alpha" {
            articleDelegate?.resetTableData(articleData: articleData!.sortArticleDataAlpha())
        } else {
            articleDelegate?.resetTableData(articleData: articleData!.sortArticleDataByDate())
        }
    }
    
    // This initializer is a convenience initializer because I need to call the standard constructor in AppDelegate
    // to get a strong reference to this class and I need to call this convenience initializer when I want to wrap
    // an Article object in the properties of this class
    convenience init? (article: Article) {
        self.init()
        self.article = article
    }
}
