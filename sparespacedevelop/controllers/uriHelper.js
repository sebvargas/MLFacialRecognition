const { exec } = require('child_process');

module.exports = {

    registerHelper(username, uri) {
    
	exec('docker exec flamboyant_swanson python interface.py register ' + username + ' "' + uri + '"', (err, stdout, stderr) => {
	if (err) {
	    console.log('error: ' + err);
	    return
	}
	console.log(stdout);
    });
    
},


loginHelper(username, uris) {
   uris = uris.split("#*^/");

    console.log("in login helper");
    console.log(uris.length);
    console.log(uris[0]);
    exec('docker exec flamboyant_swanson python interface.py login "' + uris[0] + '" "' + uris[1] + '" "' + uris[2] + '"', (err, stdout, stderr) => {
	if (err) {
	    console.log('error: ' + err);
	    return
	}
	console.log(stdout);
    });
}

}
