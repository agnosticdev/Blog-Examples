//
//  Article.swift
//  Agnostic Development
//
//  Created by Matt Eaton on 4/23/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import Foundation

public class Article: NSObject {
    
    //
    // MARK: - Public Instance Properties
    //
    public var title: String?
    public var dateString: String?
    public var articleDescription: String?
    public var URLLink: String?
    
    //
    // MARK: - Private Instance Property
    //
    private let networkKeyMap: [String: String] = ["title": "title",
                                                   "dateString": "date",
                                                   "articleDescription": "description",
                                                   "URLLink": "URLLink"]
    
    override init() {
        super.init()
    }
    
    convenience init(jsonObject: [String: AnyObject]) {
        self.init()
        
        // Parse network objects based upon a network key-value mapping schema
        for (key, value) in networkKeyMap {
            if let networkObject = jsonObject[value] as? String {
                //self.setValue(networkObject, forKey: key)
                if key == "title" {
                    self.title = networkObject
                } else if key == "dateString" {
                    self.dateString = networkObject
                } else if key == "articleDescription" {
                    self.articleDescription = networkObject
                } else if key == "URLLink" {
                    self.URLLink = networkObject
                }
            }
        }
    }
}
