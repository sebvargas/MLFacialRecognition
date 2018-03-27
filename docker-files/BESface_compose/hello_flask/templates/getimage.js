function putImage()
{
  var canvas1 = document.getElementById("canvas");        
  if (canvas1.getContext) {
     var ctx = canvas1.getContext("2d");                
var image = canvas.toDataURL("img/png").replace("img/png", "image/octet-stream");  // here is the most important part because if you dont replace you will get a DOM 18 exception.
  }
  var imageElement = document.getElementById("canvas");  
  window.location.href=image; // it will save locally
  imageElement.src = myImage;                           

}

var assert = require('assert');
describe('Array', function() {
  describe('#indexOf()', function() {
    it('should return -1 when the value is not present', function() {
      assert.equal(-1, [1,2,3].indexOf(4));
    });
  });
});