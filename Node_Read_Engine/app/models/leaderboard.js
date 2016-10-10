//model file to build out nodes


var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var LeaderboardSchema   = new Schema({
	title: String,
	created: String,
    leaderboard_data: Array
});

module.exports = mongoose.model('leaderboards', LeaderboardSchema);