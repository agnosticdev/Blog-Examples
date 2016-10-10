//model file to build out users


var mongoose     = require('mongoose');
var bcrypt       = require('bcrypt-nodejs');
var Schema       = mongoose.Schema;

var UsersSchema   = new Schema({
    local: { 
        email : String,
        key: String, 
    },
    uid: String,
    name: String,
    created: String,
    member_for: String,
    status: Boolean,
    facebook: Boolean,
    twitter: Boolean,
    email: String,
    image: String,
    badge: String,
    score: String
});



// checking if key is valid
UsersSchema.methods.validPassword = function(key) {
    if(this.local.key == key){
        return true;
    }else{
        return false;
    }
};

module.exports = mongoose.model('users', UsersSchema);

