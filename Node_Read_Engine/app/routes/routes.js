

module.exports = function(app, passport) {

	var express          = require('express');            // call express
	var Logic            = require('../logic/logic');
	var Users            = require('../models/users');
	var Questions        = require('../models/questions');
	var Challenges       = require('../models/challenges');
	var Leaderboard      = require('../models/leaderboard');
	var router           = express.Router();              // get an instance of the express Router
	var startTime;

	// middleware to use for all requests
	router.use(function(req, res, next) {

	    startTime = Date.now();
	    console.log('Something is happening.');
	    // do logging
	    // perform authentication
	    // perform validations
	    // track analytics
	    //console.log('Request Type:', req.method);
	    //console.log('Request URL:', req.originalUrl);
	    //console.log('Headers sent :' , res.headersSent);
	    //console.log('Headers :' , req.headers);
	   
	    //make sure that all incoming requests contain this app key
	    if(req.headers['appkey'] !== undefined && req.headers['appkey'] == 'LldmtPm9rIqjyFZ1Kf8iW92D75CJGWKuOb2G5WUI'){
		    //if the user is coming in on /api/login
		    if(req.originalUrl == '/user' || req.originalUrl.substring(0, 10) == '/questions' || req.originalUrl.substring(0, 11) == '/challenges'){
		        //make sure we are posting data if we are coming in on the route /api/login
		        if(req.method == 'POST'){
		        	 //send the request on its way
		        	 next();
		        }else{
		        	res.send('requested dropped for not using the correct verb');
		        }
		        
		    }else{
		        next(); // make sure we go to the next routes and don't stop here
		    }
		}else{
			//drop the request
			res.send('requested dropped for not using a proper request');
		}
	    
	});


	//*************************************** Question Routes ***************************************

	//@TODO the random number portion of this function needs work before moving into production
	//For testing it is good 

	//x-www-form-urlencoded header
	//http://passportjs.org/guide/authenticate/
	//GET A GROUP OF QUESTION BY CATEGORY AND BY NUMBER
	//THIS COULD BE USED FOR CHALLENGE QUESTIONS OR REGULAR GAMEPLAY QUESTIONS
	//
	//verb:
	//  POST
	//
	//authentiation:
	//  authenticated user
	//
	//headers:
	//  appkey  : LldmtPm9rIqjyFZ1Kf8iW92D75CJGWKuOb2G5WUI
	//
	//x-www-form-ulrencoded
	//  email   : email@email.com
	//  key     : sessionkey 
    //
	//test email: agnosticdev@gmail.com
	//test key:   7UH4F45fFX5m43aygM4yi6FviLUa3c9ZQRU3xNDF
	router.route('/questions/:category/:questionLimit').post(passport.authenticate('local-login'), function(req, res) {
	 
		//get the date so we can get the seconds 
		var d = new Date();
		var s = d.getSeconds();
		//console.log('seconds ' + s);
		
		//generate a multiplier so we can multiply it against the random number
	    var multiplier = Math.floor(Math.random()* s);
	    //get the random number
	    var random = Math.floor(Math.random()* multiplier);

	    //console.log('Multiplier ' + multiplier);
	    //console.log('Random ' + random);

	    //get the questions and skip the random number
	    Questions.find({category: req.params.category}).limit(req.params.questionLimit).skip(random).execFind(function(err, questions) {
	        if (err)
	            res.send(err);

	        res.json(questions);

	        //log the request and the time it took to make the request
	        var duration = Date.now() - startTime;
	        duration = duration + 'ms';
	        Logic.saveRouterStats({ type: 'POST ' + req.params.questionLimit + ' questions of category type: ' + req.params.category, request_date: Date.now(), request_time: duration});

	    });
	});

	//*************************************** User Routes ***************************************
	
    //x-www-form-urlencoded header
	//http://passportjs.org/guide/authenticate/
	//GET A SINGLE USER
	//
	//verb:
	//  POST
	//
	//authentiation:
	//  authenticated user
	//
	//headers:
	//  appkey  : LldmtPm9rIqjyFZ1Kf8iW92D75CJGWKuOb2G5WUI
	//
	//x-www-form-ulrencoded
	//  email   : email@email.com
	//  key     : sessionkey 
	//
	//test email: agnosticdev@gmail.com
	//test key:   7UH4F45fFX5m43aygM4yi6FviLUa3c9ZQRU3xNDF
	router.route('/user').post(passport.authenticate('local-login'), function(req, res) {
		   // If this function gets called, authentication was successful.
           // req.user contains the authenticated user.
           console.log('user success');  

           //log the request and the time it took to make the request
	        var duration = Date.now() - startTime;
	        duration = duration + 'ms';
	        Logic.saveRouterStats({ type: 'get a single user email: ' + req.user.local.email, request_date: Date.now(), request_time: duration});
            
            res.json(req.user);
	});

	

	// *************************************** Challenge Routes ***************************************
	//READ A SINGLE CHALLENGE NODE
	//
	//verb:
	//  POST
	//
	//authentiation:
	//  authenticated user
	//
	//headers:
	//  appkey  : LldmtPm9rIqjyFZ1Kf8iW92D75CJGWKuOb2G5WUI
	//
	//x-www-form-ulrencoded
	//  email   : email@email.com
	//  key     : sessionkey 
	//
	//test email: agnosticdev@gmail.com
	//test key:   7UH4F45fFX5m43aygM4yi6FviLUa3c9ZQRU3xNDF
	router.route('/challenges/:nid').post(passport.authenticate('local-login'), function(req, res) {

	    //use the find 
	    Challenges.find({nid: req.params.nid}, function(err, challenge) {
	        if (err)
	            res.send(err);

	        res.json(challenge);

	        //log the request and the time it took to make the request
	        var duration = Date.now() - startTime;
	        duration = duration + 'ms';
	        Logic.saveRouterStats({ type: 'get a single challenge nid: ' + req.params.nid, request_date: Date.now(), request_time: duration});
	       
	    });

	});


	// *************************************** Leaderboard Routes ***************************************
	//GET THE ENTIRE LEADERBOARD.  
	//
	//verb:
	//  GET
	//
	//authentiation:
	//  no authentication
	//
	//headers:
	//  appkey  : LldmtPm9rIqjyFZ1Kf8iW92D75CJGWKuOb2G5WUI
	//
	//## READ THE ENTIRE LEADER BOARD
	router.route('/leaderboard').get(function(req, res) {
	    //this is the secret here
	    //use the find 
	    Leaderboard.find({title: 'Leaderboard'}, function(err, leaderboard) {
	        if (err)
	            res.send(err);

	        res.json(leaderboard);

	        //log the request and the time it took to make the request
	        var duration = Date.now() - startTime;
	        duration = duration + 'ms';
	        Logic.saveRouterStats({ type: 'get the leaderboard', request_date: Date.now(), request_time: duration});
	    });

	});

	// REGISTER OUR ROUTES -------------------------------
	// all of our routes will be prefixed with /api
	app.use('/api', router);
};