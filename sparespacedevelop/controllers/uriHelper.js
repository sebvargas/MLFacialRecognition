module.export = {

registerHelper(uris, username) {
 
   // Instantiate the Shell object and invoke its execute method.
   var oShell = new ActiveXObject("Shell.Application");

   var commandtoRun = "sudo docker exec -it besfacecompose_web_1";
   //if (inputparms != "") {
   //   var commandParms = document.Form1.filename.value;
   //}
   //var commandParams = uris;
    // Invoke the execute method.
    console.log("here line 14");
    console.log(oShell.ShellExecute(commandtoRun, uris, username));
},


loginHelper(uris, username) {
   uris = uris.split("#*^/");
   

   // Instantiate the Shell object and invoke its execute method.
   var oShell = new ActiveXObject("Shell.Application");

   var commandtoRun = "docker exec -it besfacecompose_web_1";
   //if (inputparms != "") {
   //   var commandParms = document.Form1.filename.value;
   //}
   //var commandParams = uris;
   // Invoke the execute method.  
   oShell.ShellExecute(commandtoRun, uris, username);
}

}
