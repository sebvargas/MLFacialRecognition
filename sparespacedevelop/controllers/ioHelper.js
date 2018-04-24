module.exports = function(io) {
	io.on('connection', (client) => {
		client.on('new space', () => {
			io.emit('refresh listings', { for: 'everyone' });
		});

		client.on('peer-msg', ()=> {
			client.broadcast.emit('update msg');
		})
	})
}