//
//  CustomTableCell.swift
//  XCTestExample
//
//  Created by Matt Eaton on 10/8/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import UIKit

class CustomTableCell: UITableViewCell {
    
    @IBOutlet weak var rowImage: UIImageView?
    @IBOutlet weak var titleLabel: UILabel?
    @IBOutlet weak var dateLabel: UILabel?
    
    override func awakeFromNib() {
        super.awakeFromNib()
    }
    
    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
    }
}
