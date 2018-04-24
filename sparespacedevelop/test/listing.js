const Listing = require('../models/listingModel');
const User = require('../models/userModel');
// Require the dev-dependencies
const chai = require('chai');
const chaiHttp = require('chai-http');
const server = require('../index');

const should = chai.should();

chai.use(chaiHttp);

describe('Listings', () => {
	beforeEach((done) => {
		Listing.remove({}, (err) => {
			done();
		});
	});

	describe('/GET listings', () => {
		it('it should GET all the listings', (done) => {
			chai
				.request(server)
				.get('/listings')
				.end((err, res) => {
					res.should.have.status(200);
					res.body.should.be.a('array');
					res.body.length.should.be.eql(0);
				done();
				});
		});
	});

    describe('/POST new listing', () => {
		it('it should  POST a new listing', (done) => {
            const user = new User ({
				fullname: 'Devin Roche',
				password: 'fart',
				contact: {
					email: 'foo@email.com',
					phone: '123-456-7890',
				},
				userType: 'host'
			});
            const listing = {
				_host: user.id,
                title: 'fart',
                price: '$10',
                description: 'super cool space'
			};
			chai
				.request(server)
				.post('/listings')
				.send(listing)
				.end((err, res) => {
					res.should.have.status(200);
					res.body.should.be.a('object');
					res.body.should.have.property('_host');
					res.body.should.have.property('title');
					res.body.should.have.property('price');
					res.body.should.have.property('description');
					res.body.should.have.property('images');
				done();
				});
		});
    });
    
    describe('/GET users listing', () => {
		it('it should  GET a specific listing', (done) => {
            const user = new User ({
				fullname: 'Devin Roche',
				password: 'fart',
				contact: {
					email: 'foo@email.com',
					phone: '123-456-7890',
				},
				userType: 'host'
			});
            const listing = new Listing({
				_host: user.id,
                title: 'fart',
                price: '$100',
                description: 'super cool space'
            });
            user.save((err, user) =>{
                listing.save((err, listing) => {
                    chai
                        .request(server)
                        .get(`/listing/${listing.id}`)
                        .send(listing)
                        .end((err, res) => {
                            res.should.have.status(200);
                            res.body.should.be.a('object');
                            res.body.should.have.property('title');
                            res.body.should.have.property('price');
							res.body.should.have.property('description');
							res.body.should.have.property('images');
                        done();
                    });
                })
            })
		});
	});
	
});

