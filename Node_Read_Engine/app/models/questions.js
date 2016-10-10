//model file to build out nodes


var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var QuestionSchema   = new Schema({
    uid: String,
    title: String,
    type: String,
    nid: String,
    category: String,
    question: String,
    points: String,
    answers: Array
});

module.exports = mongoose.model('questions', QuestionSchema);
