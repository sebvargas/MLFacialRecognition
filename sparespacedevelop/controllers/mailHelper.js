const nodemailer = require('nodemailer');
const hbs = require('nodemailer-express-handlebars');
require('dotenv').config()

const smtpTransport = nodemailer.createTransport({
	service: 'gmail',
	host: 'smtp.gmail.com',
	port: 465,
	secure: true,
	auth: {
		user: process.env.EMAIL,
		pass: process.env.PASS,
	},
});

const options = {
	viewEngine: {
		extname: '.hbs',
		layoutsDir: 'views/',
	},
	viewPath: 'views/',
	extName: '.hbs'
};

smtpTransport.use('compile', hbs(options));

module.exports = {
	verifyEmail(user) {
		const mailOptions = {
			to: user.email,
			subject: 'Verify your account',
			template: 'verify',
			context: {
				user: user
			}
		}

		smtpTransport.sendMail(mailOptions, (error, response) => {
			console.log(error)
			return error, response
		});
	},
	expressInterest(renter, host, listing) {
		const mailOptions = {
			replyTo: renter.email,
			to: host.email,
			subject: 'Lets talk storage!',
			template: 'interest',
			context: {
				l: listing,
				h: host
			}
		}

		smtpTransport.sendMail(mailOptions, (error, response) => {
			return error, response
		});
	},
	newMessage(reciever) {
		const mailOptions = {
			to: reciever.email,
			subject: 'You recieved a new message!',
			template: 'message',
			context: {
				user: reciever,
			}
		}

		smtpTransport.sendMail(mailOptions, (error, response) => {
			return error, response
		});
	}
};
