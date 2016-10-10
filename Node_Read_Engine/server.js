// server.js

// BASE SETUP
// =============================================================================

// call the packages we need
var express          = require('express');              // call express
var app              = express();                       // define our app using express
var port             = process.env.PORT || 8181;        // set our port
var bodyParser       = require('body-parser');
var mongoose         = require('mongoose');
var passport         = require('passport');
var flash            = require('connect-flash');
var session          = require('express-session');
var cookieParser     = require('cookie-parser');
var morgan           = require('morgan');
var configDB         = require('./app/config/database.js');



// configuration ===============================================================
mongoose.connect(configDB.url); // connect to our database


require('./app/config/passport')(passport); // pass passport for configuration

// configure app to use bodyParser()
// this will let us get the data from a POST

app.use(morgan('dev')); // log every request to the console
app.use(cookieParser()); // read cookies (needed for auth)
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// required for passport
app.use(session({ 
         secret: 'HVCyKhngHz6lfPROwKvjqm6mPuchP3U7WE8KO3Pp', 
         resave: true,
         saveUninitialized: true,
         cookie: {
            secure: true,
            maxAge: new Date(Date.now() + 3600000)
         }
})); // session secret
app.use(passport.initialize());
app.use(passport.session()); // persistent login sessions
app.use(flash()); // use connect-flash for flash messages stored in session

// ROUTES FOR OUR API
// =============================================================================

require('./app/routes/routes')(app, passport); // pass our application into our routes



// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);


