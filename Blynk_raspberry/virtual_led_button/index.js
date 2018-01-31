/* Asennus-ohje node.js raspberryyn
http://help.blynk.cc/how-to-connect-different-hardware-with-blynk/raspberry-pi/how-to-install-nodejs-library-on-linux

Luo kansio projektillesi:
mkdir led_button

siirry kansioon:
cd led_button

Luo projektisi package.json tiedosto:
nmp init

lisaa  projektiin Blynk:
npm install blynk-library --save

Salli raspbin pinnien kaytto
npm install onoff --save


suorita tiedosto index.js  komennolla node.js index.js
*/
var Blynk = require('blynk-library');
var Gpio = require('onoff').Gpio;
var led = new Gpio(18, 'out');

var AUTH = 'syota tahan sinun salainen token';

var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);


v0.on('write', function(param) {
	if (param[0]=='1' ){
		led.writeSync(1);
		console.log('V0:', param[0]);	
   	}  else {
		led.writeSync(0)
		console.log('V0:', param[0]);
	}
});



