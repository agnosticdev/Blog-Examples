//
//  AppDelegate.swift
//  MVVM Sample
//
//  Created by Matt Eaton on 10/28/16.
//  Copyright © 2016 AgnosticDev. All rights reserved.
//

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?
    let articleViewModel = ArticleViewModel()
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        
        // Build an initial set of data to be loaded into the ArticleData class
        var newArticles = [Article]()
        
        // Swift Thumbnail
        let swiftImage = UIImage(named: "swift")!
        let swiftImageData: Data = UIImagePNGRepresentation(swiftImage)!
        print ("Swift data \(swiftImageData)")
        
        // JavaScript Thumbnail
        let javaScriptImage = UIImage(named: "javascript")!
        let javaScriptImageData: Data = UIImagePNGRepresentation(javaScriptImage)!
        
        // Python Thumbnail
        let pythonImage = UIImage(named: "python")!
        let pythonImageData: Data = UIImagePNGRepresentation(pythonImage)!
        
        // ObjC Thumbnail
        let appleImage = UIImage(named: "apple")!
        let appleImageData: Data = UIImagePNGRepresentation(appleImage)!
        
        // Setup the date formatter for the Article Objects
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "dd-MM-yyyy"
        
        // Create new Article objects
        newArticles.append(Article(title: "Great Swift Article", date: dateFormatter.date(from:"18-10-2016")!, image: swiftImageData))
        newArticles.append(Article(title: "Excellent Objective-c", date: dateFormatter.date(from:"06-10-2016")!, image: appleImageData))
        newArticles.append(Article(title: "Awesome Python Article", date: dateFormatter.date(from:"14-10-2016")!, image: pythonImageData))
        newArticles.append(Article(title: "JavaScript Article", date: dateFormatter.date(from:"10-10-2016")!, image: javaScriptImageData))
        
        // Initialize the ArticleData object with the new array of Article objects and set as a class property
        let articleData = ArticleData(articles: newArticles)
        articleViewModel.articleData = articleData
        
        return true
    }

    func applicationWillResignActive(_ application: UIApplication) {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, and invalidate graphics rendering callbacks. Games should use this method to pause the game.
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
        // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        // Called as part of the transition from the background to the active state; here you can undo many of the changes made on entering the background.
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
    }

    func applicationWillTerminate(_ application: UIApplication) {
        // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
    }
}

