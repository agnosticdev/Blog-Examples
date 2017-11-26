//
//  Network.swift
//  Agnostic Development
//
//  Created by Matt Eaton on 5/14/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import Foundation

class Network: NSObject {
    
    //
    // MARK: - Shared instance property
    //
    public static var shared = Network()
    
    //
    // MARK: - Public instance properties
    //
    public weak var networkDelegate: NetworkProtocol?
    
    //
    // MARK: - Private constants
    //
    private let url = "https://5fc3d7589074cd0c4bf5-79ef711e857aec8d77eb74e0027f6262.ssl.cf1.rackcdn.com/articles.json"
    private let urlConfiguration = URLSessionConfiguration.default
    
    //
    // MARK: - Public Instance Methods
    //
    
    // Load articles over the network with a default completion block provided by URLSession
    public func loadNewArticlesWithDefaultCompletion() {
        
        guard let articleURL = URL(string: url) else {
            return
        }
        
        var articleRequest = URLRequest(url: articleURL)
        articleRequest.httpMethod = "GET"
        
        let urlSession = URLSession(configuration: urlConfiguration)
        
        // Create a dataTask with a closure that defines the comletion handler
        // The closure in this case is defined as completionHandler: { (data, response, error) in  ... }
        let articleTask = urlSession.dataTask(with: articleRequest, completionHandler: { [weak self] (data, response, error) in
            
            // Ensure that an error is not present, otherwise, return the error
            guard error == nil else {
                // Usage of weak self to reference networkDelegate
                DispatchQueue.main.async {
                    self?.networkDelegate?.networkReceivedError(error: error.debugDescription)
                }
                return
            }
            
            // Ensure that the network data is available and that the byte count is greater that zero
            guard let networkData = data, networkData.count > 0 else {
                DispatchQueue.main.async {
                    self?.networkDelegate?.networkReceivedError(error: "There was an error parsing network data.")
                }
                return
            }
            
            // Perform the JSONSerialization into an array of Dictionaries
            // Next use the convenience constructor in Article to create an Article object out of each object in the JSON array
            do {
                if let networkArticles = try JSONSerialization.jsonObject(with: networkData, options: []) as? [[String: AnyObject]] {
                    var articles: [Article] = []
                    
                    // Create article objects out of a JSON object
                    for networkArticle in networkArticles {
                        let article = Article(jsonObject: networkArticle)
                        articles.append(article)
                    }
                    DispatchQueue.main.async {
                        self?.networkDelegate?.articlesFinishedLoading(articles: articles)
                    }
                }
            } catch let error as NSError {
                DispatchQueue.main.async {
                    self?.networkDelegate?.networkReceivedError(error: error.debugDescription)
                }
            }
            
        })
        articleTask.resume()
    }
    
    // Load articles over the network with a assigned completion as a passed in argument : networkArticlesCompletionHander
    // networkArticlesCompletionHander is a closure defined as a variable to handle all of the processing without using URLSessions out of the box completion handler
    public func loadNewArticlesWithAssignedCompletion(networkArticlesCompletionHander: @escaping(Data?, URLResponse?, Error?) -> Void) {
        
        guard let articleURL = URL(string: url) else {
            return
        }
        
        var articleRequest = URLRequest(url: articleURL)
        articleRequest.httpMethod = "GET"
        
        let urlSession = URLSession(configuration: urlConfiguration)
        
        let articleTask = urlSession.dataTask(with: articleRequest, completionHandler: networkArticlesCompletionHander)
        articleTask.resume()
    }
    
    public func runNetworkingRequests(networkRequest: URLRequest, networkSession: URLSession, completion: @escaping (_ : String) -> Void) {
        var results: String = ""
        let start = Date()

        // Actual network request
        let networkTask = networkSession.dataTask(with: networkRequest, completionHandler: { (data, response, error) in
            
            guard let url = response?.url else {
                return
            }
            if let _ = data {
                let elapsed_start = abs(start.timeIntervalSinceNow)
                results = "SUCCESS: Latency Elapsed: \(elapsed_start) for URL: \(url) |DONE|"
                DispatchQueue.main.async {
                    print(results)
                    completion(results)
                }
            } else {
                let elapsed_fail = abs(start.timeIntervalSinceNow)
                results = "FAIL: Latency Elapsed: \(elapsed_fail) for URL: \(url) |DONE|"
                DispatchQueue.main.async {
                    print(results)
                    completion(results)
                }
            }
        })
        networkTask.resume()
    }
}
