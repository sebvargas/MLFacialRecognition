const userHelper = require('../controllers/userHelper');
const mapsHelper = require('../controllers/mapsHelper');
const listHelper = require('../controllers/listingHelper');
const msgHelper = require('../controllers/messageHelper');

module.exports = function (app) {
	app.route('/users')
		.post(userHelper.createUser);

	app.route('/user/:id')
		.get(userHelper.getUser)
		.put(userHelper.updateUser)

	app.route('/login')
		.post(userHelper.loginUser);

	app.route('/verify/:id')
		.get(userHelper.verifyUser);

	app.route('/resendV')
		.post(userHelper.resendV)

	app.route('/close/:id')
		.get(listHelper.closeListing)

	app.route('/cordinates')
		.get(mapsHelper.getAllCords)
		.post(mapsHelper.cordsToAddress);

	app.route('/listings')
		.get(listHelper.allListings)
		.post(listHelper.newListing);

	app.route('/listing/:id')
		.get(listHelper.listingDetails)
		.put(listHelper.updateListing)
		.delete(listHelper.deleteListing);

	// messages routes
	app.route('/message')
		.post(msgHelper.newMessage);

	app.route('/messages/:id')
		.get(msgHelper.getConversations);

	app.route('/message/:host/:renter')
		.get(msgHelper.allMessages)

	// these are for dev purposes to make it easier to test frontend
	app.route('/deleteListings')
		.delete(listHelper.clearAll);

	app.route('/deleteUsers')
		.delete(userHelper.clearAll);
	app.route('/report')
		.post(listHelper.reportListing);
};
