//
//  Helper.swift
//  Agnostic Development
//
//  Created by Matt Eaton on 4/23/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//

import UIKit

struct Helper {
    
    //
    // MARK: - Help to get the logo for the navigation bar
    //
    static func getLogo() -> UIImageView {
        
        let logo = UIImage(named: "logo.png")
        let logoImageView = UIImageView(image: logo)
        logoImageView.contentMode = .scaleAspectFit
        return logoImageView
    }
}
