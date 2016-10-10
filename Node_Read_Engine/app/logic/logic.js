// functions that help out our server file
// our server file acts like our controller in a MVC setup


// logic.js
// ========
var mongoose     = require('mongoose');
var Statistics       = require('../models/statistics');


module.exports = {

	saveRouterStats: function(object){
		var s = new Statistics(object);
		console.log(object);
		s.save(function (err) {
		  if (err) console.log(err);
		  // saved!
		});
	}, validateHeader: function(header){

		
	}



};