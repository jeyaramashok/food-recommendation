
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , http = require('http')
  , path = require('path')
  , food = require('./routes/db')
  , restify = require('restify');

var app = express();

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));


http.createServer(app).listen(3000,function(){
    console.log('Express started');
})


// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}
app.configure(function () {
    app.use(express.bodyParser());
});



app.get('/food/:text', food.findByText);
app.get('/food', food.show)

/*
var server = restify.createServer();


server.listen(8080, function() {
    console.log('%s listening at %s', server.name, server.url);
});
   */