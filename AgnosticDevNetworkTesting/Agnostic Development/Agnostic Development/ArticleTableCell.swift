//
//  ArticleTableCell.swift
//  Agnostic Development
//
//  Created by Matt Eaton on 4/23/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import UIKit

class ArticleTableCell: UITableViewCell {
    
    //
    // MARK: - IBOutlets
    //
    @IBOutlet weak var articleTitle: UILabel?
    @IBOutlet weak var articleDate: UILabel?
    @IBOutlet weak var articleDesc: UILabel?
    
    override func awakeFromNib() {
        super.awakeFromNib()
    }
    
    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
        // Configure the view for the selected state
    }
    
}

