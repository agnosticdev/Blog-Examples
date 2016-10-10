//model file to build out users


var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var StatsSchema   = new Schema({
    type: String,
    request_date: Date,
    request_time: String
});

module.exports = mongoose.model('statistics', StatsSchema);