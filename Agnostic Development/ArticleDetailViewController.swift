//
//  ArticleDetailViewController.swift
//  Agnostic Development
//
//  Created by Matt Eaton on 4/23/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import UIKit

class ArticleDetailViewController: UIViewController {
    
    //
    // MARK: - IBOutlets
    //
    @IBOutlet weak var articleTitle: UILabel!
    @IBOutlet weak var articleDate: UILabel!
    @IBOutlet weak var articleDesc: UILabel!
    @IBOutlet weak var articleLink: UIButton!
    
    //
    // MARK: Constants
    //
    var selectedArticle: Article?
    
    //
    // MARK: View Controller Methods
    //
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set navigation bar logo
        self.navigationItem.titleView = Helper.getLogo()
        
        self.setup()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    //
    // MARK: Instance Methods
    //
    func setup() {
        if let passedInArticle = selectedArticle {
            self.articleTitle.text = passedInArticle.title
            self.articleDate.text = passedInArticle.dateString
            self.articleDesc.text = passedInArticle.articleDescription
            self.articleDesc.sizeToFit()
        }
    }
    
    //
    // MARK: IBOutlets
    //
    @IBAction func viewLink(sender: UIButton) {
        
        guard let articleLink = selectedArticle?.link else {
            return
        }
        
        if let url = URL(string: articleLink) {
            UIApplication.shared.open(url, options: [:])
        }
    }
}
