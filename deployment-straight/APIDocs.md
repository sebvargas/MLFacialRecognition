Front End:

To use our API once it has been installed, make sure you have these two HTML elements on your webpage

`<video id="video" width="640" height="480" style="border: 1px solid black;" autoplay></video>`
`<canvas id="canvas" width="640" height="480"  style="border: 1px solid black;"></canvas>`

These can be put anywhere you want on your website or how you see it is fit for your users to view the camera.
The important part is that they are video and canvas elements as well as their id's must be video and canvas.
This applies to both log in as well as sign up.

Also, in the form where you ask for the user's name and password for the sign up, include these hidden fields in the form
`<input type="hidden" id="imageUrl" name="imageUrl" value="" />`


For example:
<form method="post" action="/register" autocomplete="on">
    Username:<input type="text" name="username" id="username" required><br>
    <input type="hidden" id="imageUrl" name="imageUrl" value="" />
    <input id="snap" type="submit" id="snap" value="Log in">
</form>

Back End:

To implement our back end API, call our backend functions in their appropriate places from where you host
your registration

For example,
call `backend.login(POST_IMAGE)` where you call `POST_IMAGE = str(request.form['imageURL'])`
