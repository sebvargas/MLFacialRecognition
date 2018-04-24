const mongoose = require('mongoose');
const Listing = mongoose.model('Listing')
require('dotenv').config()

module.exports = {
	getAllCords(req, res) {
		Listing.find({}, 'lat lng title', (err, listing) => {
			if (err)
				return res.json(err);

			res.send(listing);
		});
	},

	cordsToAddress(req, res) {
		const googleMapsClient = require('@google/maps').createClient({
			key: process.env.GMAPS
		});

		googleMapsClient.geocode({
			address: req.body.address
		}, (err, response) => {
			if (err)
				return res.send(err)
			if (response.json.status === 'ZERO_RESULTS')
				res.send('bad')
			else
				res.send(response.json.results[0].geometry.location);


		});
	}
};
