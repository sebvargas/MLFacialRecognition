<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <title>addContact.html</title>
 <link rel = "stylesheet"
  type = "text/css"
  href = "contact.css" />
</head>
<body>
 <?php
 //read data from form
 $username = filter_input(INPUT_POST, "username");
 $password = filter_input(INPUT_POST, "password");
 $image = filter_input(INPUT_POST, "image");

 //print form results to user
 print <<< HERE
 <h1>Thanks!</h1>
 <p>
  Your spam will be arriving shortly.
 </p>
 <p>
 username: $username <br />
 password: $password <br />
 $image
 </p>
HERE;
 //generate output for text file
 $output = <<< HERE
username: $username
password: $password

HERE;
 //open file for output
 $fp = fopen("contacts.txt", "a");
 //write to the file
 fwrite($fp, $output);
 fclose($fp);
 ?>
</body>
</html>