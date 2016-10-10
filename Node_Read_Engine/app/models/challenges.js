//model file to build out users


var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var ChallengeSchema   = new Schema({
    nid: String,
    title: String,
    type: String,
    challenging_user: Array,
    user_being_challenged: Array,
    score: String,
    category: String,
    challenge_complete: String,
    challege_created: String,
    challenge_closed: String
});

module.exports = mongoose.model('challenges', ChallengeSchema);
