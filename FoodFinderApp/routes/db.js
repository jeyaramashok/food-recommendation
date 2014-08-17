/*
 * Connection to mongodb
 */
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/pollo_tropical_menu');
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));

var schema = new mongoose.Schema(
		{
			type:String,
			description:String,
			image:String,
			name:String,
			restaurant:String
		});
var items = mongoose.model('items',schema);

exports.findByText = function (req, res) {
    var text = req.params.text;
    console.log(text);
    console.log('Retrieving Items');
    var regex = new RegExp(text,'i');
    items.find({name: regex}, function (err, foodItems) {
                console.log(foodItems);
                res.json(foodItems);
    });
};

exports.show = function(req, res){
    res.json(200, {message: "My Simple Json"});

};