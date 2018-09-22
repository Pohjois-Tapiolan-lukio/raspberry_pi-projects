#include <SPI.h>
#include <WiFi101.h>
#include <MQTTClient.h>

#include "arduino_secrets.h"
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int status = WL_IDLE_STATUS;

WiFiClient wifi_client;
MQTTClient mqtt_client;

void handleMessage(String &topic, String &payload) {
  Serial.println("got a message");
  Serial.println(payload);
  
}

void setup() {
  //Configure pins for Adafruit ATWINC1500 Feather
  WiFi.setPins(8, 7, 4, 2);
  //Initialize serial and wait for port to open:
  Serial.begin(9600);

  connectShiftr();
}

void loop() {
  mqtt_client.loop();

  mqtt_client.connected() || connectShiftr();
}

bool connectShiftr() {

  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  // you're connected now, so print out the data:
  Serial.println("You're connected to the network");
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  mqtt_client.begin("broker.shiftr.io", wifi_client);
  mqtt_client.onMessage(handleMessage);
  while (!mqtt_client.connect(SHIFTR_NAME, SHIFTR_USER, SHIFTR_PASS)) {
    Serial.println("Connecting to shiftr");
    delay(1000);
  }
  mqtt_client.subscribe("/data");
  Serial.println("Connected to shiftr");
  return true;
}
