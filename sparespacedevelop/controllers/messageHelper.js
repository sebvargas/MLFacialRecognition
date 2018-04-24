const mongoose = require('mongoose');
const userModel = require('../models/messageModel')
const Message = mongoose.model('Message');
const User = mongoose.model('User');
const mailHelper = require('./mailHelper')

module.exports = {
	allMessages(req, res) {
		Message.find({'host': req.params.host ,'renter': req.params.renter }, 'createdAt author text')
			.populate('author', 'first')
			.exec((err, m) => {
				if (err) 
					return res.json(err);
            
				res.send(m);
			});
	},
	
	newMessage(req, res) {
		const reciever = req.body.author === req.body.host ? req.body.renter : req.body.host
		User.findById(reciever, (err, user) => {
			mailHelper.newMessage(user)
		})

		const newMessage = new Message(req.body);
		newMessage.save((err, m) => {
			if (err) 
				return res.json(err);

			res.send(m);
		});
	},
    
	getConversations(req, res) {
		const id = req.params.id;
		Message.aggregate([
			{$match: {$or: [{'host': mongoose.Types.ObjectId(id)},{'renter': mongoose.Types.ObjectId(id)}]}},
			{ $group: {'_id': {'host': '$host', 'renter': '$renter'}}},
			{ $lookup: { from: 'sparespaceusers', localField: '_id.host', foreignField: '_id', as: 'user1' } },
			{ $lookup: { from: 'sparespaceusers', localField: '_id.renter', foreignField: '_id', as: 'user2' } },
		], (err, result) => {
			if (err) 
				return res.json(err);
            
          
			const results = []
			result.forEach(elem => {
				const tmp = {}
				tmp['host_id'] = elem.user1[0]._id
				tmp['renter_id'] = elem.user2[0]._id
				tmp['host'] = elem.user1[0].first + ' ' + elem.user1[0].last
				tmp['renter'] = elem.user2[0].first + ' ' + elem.user2[0].last
				results.push(tmp)
			})

			res.send(results)
		});
	}
};