const mongoose = require('mongoose');
const listingModel = require('../models/listingModel')
const Listing = mongoose.model('Listing');

module.exports = {
	newListing(req, res) {
		req.body._host = mongoose.Types.ObjectId(req.body._host);
		req.body.dates[0] = new Date(req.body.dates[0])
		req.body.dates[1] = new Date(req.body.dates[1]);

		const newListing = new Listing(req.body);

		newListing.save((err, listing) => {
			if (err) 
				return res.json(err);
            
            
			res.send(listing);
		});
	},

	allListings(req, res) {
		Listing.find({status: 1})
			.populate('_host', '_id first')
			.exec((err, listing) => {
				if (err) 
					return res.json(err);
					
				res.send(listing);
			});
	},
    
	updateListing(req, res) {
		Listing.findOneAndUpdate({ _id: req.params.id }, req.body, {new: true}, (err, listing) => {
			if (err) 
				return res.json(err);
        

			res.json({ message: 'listing updated', listing });
		});
	},

	closeListing(req, res) {
		Listing.findByIdAndUpdate(req.params.id, { status: 0 }, { new: true }, (err, result) => {
			return res.json({status: 'closed', result: result})
		})
	},

	listingDetails(req, res) {
		Listing.findById(req.params.id)
			.populate('_host', '_id first')
			.exec((err, listing) => {
				if (err) 
					return res.json(err);

				res.send(listing);
			});
	},

	deleteListing(req, res) {
		Listing.remove({ _id: req.params.id }, (err, listing) => {
			if (err) 
				return res.json(err);
      

			res.json({listing});
		});
	},

	// Use for testing only: clear all listings from db
	clearAll(req, res){
		Listing.remove({}, (err, listing) => {
			if(err)
				return res.json(err)

			res.send(listing)
		})
	},
	reportListing(req,res) {
		Listing.findOne({ _id: req.body.id }, {reportCount:1,reportMessages:1}, (err, listing) => {
			if (err) 
				return res.json(err);
			var tempArr = listing.reportMessages;
			tempArr.push(req.body.message)
			Listing.findOneAndUpdate({_id:req.body.id},{reportCount:listing.reportCount+ 1,reportMessages:tempArr},(err2,listing2) => {
				if (err2) 
					return res.json(err2);
				res.json({ message: 'listing updated', listing2 });
				
			});
			
		});	
	}
};
