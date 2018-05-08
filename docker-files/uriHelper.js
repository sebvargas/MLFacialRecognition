var asyncblock = require('asyncblock');
const { execSync } = require('child_process');

module.exports = {
    registerHelper(username, uri) {
	console.log("in register helper, username:" + username);
	var tmp = execSync('docker exec cont1 python interface.py register ' + username + ' "' + uri + '"', (err, stdout, stderr) => {
	if (err) {
	    console.log('error: ' + err);
	    return;
	}
	    
	    console.log(tmp.toString());
    });
    
},


loginHelper(username, uris) {
   uris = uris.split("#*^/");

    console.log("in login  helper ");
    console.log(uris.length);
    //asyncblock(function (flow) {
    var tmp = execSync('docker exec cont1 python interface.py login "' + uris[0] + '" "' + uris[1] + '" "' + uris[2] + '"', (err, stdout, stderr) => {
	if (err) {
	    console.log('error: ' + err);
	    return;
	}
	console.log("here:" + stdout + ", username:" + username);
	console.log(stdout.replace(/(\r\n\t|\n|\r\t)/gm,"") == username);
	v= (stdout.replace(/(\r\n\t|\n|\r\t)/gm,"") == username);
	wait = true;
	console.log("got " + v);
	return v;
    });
    tmp = tmp.toString().replace(/(\r\n\t|\n|\r\t)/gm,"");
    var eql = tmp == username;
    console.log("got back from docker:"+tmp);
    console.log("returning:"+(eql));
    return (tmp == username);

//	result = flow.wait();
//	console.log(result);
	/*
    tmp.on('exit', function(v) {
	console.log(v);
	return v;
    });*/
//    });

    
}

}
