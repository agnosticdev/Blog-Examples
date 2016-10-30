//
//  ViewController.swift
//  MVVM Sample
//
//  Created by Matt Eaton on 10/28/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource, ArticleProtocol {
    
    // The filterSwitch and tableView declared as weak IBOutlets
    @IBOutlet weak var filterSwitch: UISegmentedControl?
    @IBOutlet weak var tableView: UITableView?
    
    // View Controller's local variables
    weak var viewModel: ArticleViewModel?
    var localArticles: [Article]?
    var appDelegate = UIApplication.shared.delegate as! AppDelegate

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        // Take the strong reference from the AppDelegate and assign it to the view controllers weak reference of the same object
        viewModel = appDelegate.articleViewModel
        viewModel?.articleDelegate = self
        
        // Trigger the initial load of data as sorted by alpha
        triggerSegmentationSwitch(sender: filterSwitch!)
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: UISegmentedControl Callback
    //
    // Callback for the UISegmentedControl to reload the table data sorted using a specific filter
    //
    @IBAction func triggerSegmentationSwitch(sender: UISegmentedControl) {
        
        let index = sender.selectedSegmentIndex
        if index == 0 {
            viewModel?.getArticleData(withFlag: "alpha")
        } else {
            viewModel?.getArticleData(withFlag: "date")
        }
    }
    
    // MARK: ArticleProtocol
    //
    // Article Protocol callback function to get a message from ArticleViewModel that new data is available and ready to reload the view
    //
    func resetTableData(articleData: [Article]) {
        localArticles = articleData
        tableView!.reloadData()
    }
    
    // MARK: Tableview Functions
    //
    // Get the number of rows for the tableView
    //
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return localArticles!.count
    }
    
    //
    // Get the data from the loadArticles array based upon the row index and pluck an Article object out of the 
    // array and wrap it in the ArticleViewModel class using the convenience constructor.
    // Set the ArticleViewModel formatted properties to the custom ArticleCellTableViewCell
    //
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let articleCell: ArticleCellTableViewCell = tableView.dequeueReusableCell(withIdentifier: "ArticleCell") as! ArticleCellTableViewCell
        let articleVM = ArticleViewModel(article: (localArticles?[indexPath.row])!)
      
        // Set the article image, title, and date
        articleCell.articleImage?.image = UIImage(data:(articleVM?.image!)!, scale:1.0)
        articleCell.articleTitle?.text = articleVM?.titleText
        articleCell.articleDate?.text = articleVM?.dateFormattedString
    
        return articleCell
    }
    
    //
    // Selection of a row 
    //
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        // Display your awesome article here!
    }
}

