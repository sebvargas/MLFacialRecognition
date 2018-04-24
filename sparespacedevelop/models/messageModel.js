const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const message = new Schema({
	host: { type: Schema.Types.ObjectId, ref: 'User', required: true },
	renter: { type: Schema.Types.ObjectId, ref: 'User', required: true },
	author : {type: Schema.Types.ObjectId, ref: 'User', required: true },
	text: {type: String, required: true}
},{ timestamps: true },{ collection: 'sparespacechat' });

module.exports = mongoose.model('Message', message);
