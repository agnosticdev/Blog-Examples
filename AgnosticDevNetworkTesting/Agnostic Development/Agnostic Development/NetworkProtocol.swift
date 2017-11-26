//
//  NetworkProtocol.swift
//  Agnostic Development
//
//  Created by Matt Eaton on 5/20/17.
//  Copyright © 2017 AgnosticDev. All rights reserved.
//


public protocol NetworkProtocol: class {
    
    //
    // MARK: - Notify the user interface once the network is finished loading
    //
    func networkReceivedError(error: String)
    func articlesFinishedLoading(articles: [Article])
}
