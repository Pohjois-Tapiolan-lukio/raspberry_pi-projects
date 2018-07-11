/**
 * BasicHTTPClient.ino
 *
 *  Created on: 24.05.2015
 *
 */

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <Adafruit_NeoPixel.h>

#include <ESP8266HTTPClient.h>

#define USE_SERIAL Serial

/* Pins */
#define PIN D4
#define NUM_LEDS 10
#define BRIGHTNESS 255  // Values between 0 ... 255.
#define DEALAY_VAL 10

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

ESP8266WiFiMulti WiFiMulti;

void setup() {

    USE_SERIAL.begin(115200);
   // USE_SERIAL.setDebugOutput(true);

    USE_SERIAL.println();
    USE_SERIAL.println();
    USE_SERIAL.println();

    for(uint8_t t = 4; t > 0; t--) {
        USE_SERIAL.printf("[SETUP] WAIT %d...\n", t);
        USE_SERIAL.flush();
        delay(1000);
    }

    WiFiMulti.addAP("AndroidAP", "ipad14567");

    strip.begin();

}

void loop() {
    // wait for WiFi connection
    if((WiFiMulti.run() == WL_CONNECTED)) {

        HTTPClient http;

        USE_SERIAL.print("[HTTP] begin...\n");
        // configure traged server and url
        //http.begin("https://192.168.43.56/rgb", "7a 9c f4 db 40 d3 62 5a 6e 21 bc 5c cc 66 c8 3e a1 45 59 38"); //HTTPS
        http.begin("http://192.168.43.56:5000/processjson"); //HTTP

        USE_SERIAL.print("[HTTP] GET...\n");
        // start connection and send HTTP header
        int httpCode = http.GET();

        // httpCode will be negative on error
        if(httpCode > 0) {
            // HTTP header has been send and Server response header has been handled
            USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);

            // file found at server
            if(httpCode == HTTP_CODE_OK) {
                String payload = http.getString();
                USE_SERIAL.println(payload);
                int firstColon = payload.indexOf(":");
                int firstComma = payload.indexOf(",");
                String redVal = payload.substring(firstColon+3, firstComma-1);
                int red = redVal.toInt();

                int secondColon = payload.indexOf(":", firstColon+1);
                int secondComma = payload.indexOf(",", firstComma+1);
                String greenVal = payload.substring(secondColon+3, secondComma-1);
                int green = greenVal.toInt();

                int thirdColon = payload.indexOf(":", secondColon+1);
                int thirdComma = payload.indexOf("}", secondComma+1);
                String blueVal = payload.substring(thirdColon+3, thirdComma-2);
                int blue = blueVal.toInt();

                Serial.println(red);
                Serial.println(green);
                Serial.println(blue);
                /*
                String redValue  = payload.substring(12, 15);
                String greenValue = payload.substring(26, 29);
                String blueValue = payload.substring(38, 41);
                //USE_SERIAL.println(redValue);
                int red = redValue.toInt();
                int green = greenValue.toInt();
                int blue = blueValue.toInt();
                USE_SERIAL.println(redValue);
                USE_SERIAL.println(greenValue);
                USE_SERIAL.println(blueValue);
                */

                for (int i=0; i <= NUM_LEDS; i++){
                  strip.setPixelColor(i, strip.Color(red,green,blue));
                }
                strip.show();
                
                
                
            }
        } else {
            USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }

        http.end();
    }

    delay(1000);
}

