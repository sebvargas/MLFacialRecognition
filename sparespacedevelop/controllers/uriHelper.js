const { exec } = require('child_process');

module.exports = {

    registerHelper(username, uri) {
	console.log("in register helper, username:" + username);
	exec('docker exec cont1 python interface.py register ' + username + ' "' + uri + '"', (err, stdout, stderr) => {
	if (err) {
	    console.log('error: ' + err);
	    return;
	}
	console.log(stdout);
    });
    
},


loginHelper(username, uris) {
   uris = uris.split("#*^/");

    console.log("in login  helper ");
    console.log(uris.length);
    exec('docker exec cont1 python interface.py login "' + uris[0] + '" "' + uris[1] + '" "' + uris[2] + '"', (err, stdout, stderr) => {
	if (err) {
	    console.log('error: ' + err);
	    return;
	}
	console.log("here:" + stdout + ", username:" + username);
	console.log(stdout.replace(/(\r\n\t|\n|\r\t)/gm,"") == username);
	return (stdout.replace(/(\r\n\t|\n|\r\t)/gm,"") == username);
    });

    
}

}
