const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const listing = new Schema({
	_host: { type: Schema.Types.ObjectId, ref: 'User', required: true },
	title: { type: String, required: true },
	price: { type: Number	, required: true },
	description: {type: String, required: true },
	dates: [Date],
	location: {type: String, required: true},
	images: [{type: String, required: true}],
	interested: [String],
	lat: {type: String},
	lng: {type: String},
	size: {type: String},
	features: {type: [String]},
	status: {type: Number, default: 1},
	reportCount: {type: Number, default: 0},
	reportMessages:{type:[String]},
},{ collection: 'sparespacelisting' });

module.exports = mongoose.model('Listing', listing);
