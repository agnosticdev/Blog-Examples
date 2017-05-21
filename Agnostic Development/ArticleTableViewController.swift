//
//  ArticleTableViewController.swift
//  Agnostic Development
//
//  Created by Matt Eaton on 4/23/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import UIKit

class ArticleTableViewController: UIViewController {
    
    //
    // MARK: - IBOutlets
    //
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var activityView: UIView!
    
    //
    // MARK: Properties
    //
    var articles: [Article] = []
    
    //
    // MARK: View Controller Methods
    //
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Remove padding introduced by the navigation controller
        self.automaticallyAdjustsScrollViewInsets = false
        
        // Set navigation bar logo
        self.navigationItem.titleView = Helper.getLogo()
        self.activityView.layer.cornerRadius = 5.0
        
        // Assign the network delegate to the ArticleTableViewController
        Network.shared.networkDelegate = self
        
        // Tableview setup
        tableView.rowHeight = UITableViewAutomaticDimension
        tableView.estimatedRowHeight = 140
        
        // Load over the network using the default completion block that makes use of weak self
        // Network.shared.loadNewArticlesWithDefaultCompletion()
        
        // Declare a completion closure as a variable and then pass it to the Network object to perform the completion task
        let networkArticlesCompletionHander: (Data?, URLResponse?, Error?) -> Void = {
            [unowned self] (data, response, error) in

            guard error == nil else {
                // Display error alert with usage of unowned self that an error is present
                DispatchQueue.main.async {
                    self.displayError(message: error.debugDescription)
                }
                return
            }
            
            guard let networkData = data, networkData.count > 0 else {
                // Display error alert with usage of unowned self that data was not returned
                DispatchQueue.main.async {
                    self.displayError(message: "There was an error parsing network data.")
                }
                return
            }
            
            do {
                if let networkArticles = try JSONSerialization.jsonObject(with: networkData, options: []) as? [[String: AnyObject]] {
                    var collectedArticles: [Article] = []
                    
                    // Create article objects out of a JSON object
                    for networkArticle in networkArticles {
                        let article = Article(jsonObject: networkArticle)
                        collectedArticles.append(article)
                    }
                    DispatchQueue.main.async {
                        // Usage of unowned self
                        self.articles = collectedArticles
                        self.activityView.alpha = 0.0
                        self.tableView.reloadData()
                    }
                }
            } catch let error as NSError {
                DispatchQueue.main.async {
                    // Usage of unowned self
                    self.displayError(message: error.debugDescription)
                }
            }
        }
        
        // Load over the network using custom defined closure as a completion block that makes use of unowned self
        Network.shared.loadNewArticlesWithAssignedCompletion(networkArticlesCompletionHander: networkArticlesCompletionHander)
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let destination = segue.destination as? ArticleDetailViewController,
            let indexPath = tableView.indexPathForSelectedRow {
            destination.selectedArticle = articles[indexPath.row]
        }
    }
    
    //
    // MARK: - Public Methods
    //
    public func displayError(message: String) {
        let alertViewController = UIAlertController(title: "Network Error",
                                                    message: message,
                                                    preferredStyle: .alert)
        
        let dismiss = UIAlertAction(title: "OK",
                                    style: .default,
                                    handler: nil)
        alertViewController.addAction(dismiss)
        
        present(alertViewController, animated: true)
    }
}

extension ArticleTableViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return articles.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "ArticleCell", for: indexPath) as! ArticleTableCell
        cell.selectionStyle = UITableViewCellSelectionStyle.none
        
        let article = articles[indexPath.row]
        
        cell.articleTitle?.text = article.title ?? ""
        cell.articleDate?.text = article.dateString ?? ""
        cell.articleDesc?.text = article.articleDescription ?? ""
        
        return cell
    }
}

extension ArticleTableViewController: NetworkProtocol {
    
    func networkReceivedError(error: String) {
        self.activityView.alpha = 0.0
        self.displayError(message: error)
    }
    
    func articlesFinishedLoading(articles: [Article]) {
        self.activityView.alpha = 0.0
        self.articles = articles
        self.tableView.reloadData()
    }
}

