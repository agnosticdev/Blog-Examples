//
//  ArticleProtocol.swift
//  MVVM Sample
//
//  Created by Matt Eaton on 10/29/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

protocol ArticleProtocol: class {
    // Signaling function that hands the ArticleViewController new data
    func resetTableData(articleData: [Article])
}
