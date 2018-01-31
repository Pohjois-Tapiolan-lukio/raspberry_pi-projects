/* Asennus-ohje node.js raspberryyn
http://help.blynk.cc/how-to-connect-different-hardware-with-blynk/raspberry-pi/how-to-install-nodejs-library-on-linux

suorita tiedosto komennolla node.js index.js
*/
var Blynk = require('blynk-library');

var AUTH = 'sinun salainen token';

var blynk = new Blynk.Blynk(AUTH);

var v1 = new blynk.VirtualPin(1);
var v9 = new blynk.VirtualPin(9);

v1.on('write', function(param) {
  console.log('V1:', param[0]);
});

v9.on('read', function() {
  v9.write(new Date().getSeconds());
});
