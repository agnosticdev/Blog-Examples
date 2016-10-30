//
//  ArticleCellTableViewCell.swift
//  MVVM Sample
//
//  Created by Matt Eaton on 10/28/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import UIKit

class ArticleCellTableViewCell: UITableViewCell {
    
    // Custom UITableCell 
    
    @IBOutlet weak var articleImage: UIImageView?
    @IBOutlet weak var articleTitle: UILabel?
    @IBOutlet weak var articleDate: UILabel?

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
        // Configure the view for the selected state
    }

}
