#include <SPI.h>
#include <WiFi101.h>
#include <MQTTClient.h>

#define Control 12

char ssid[] = "1234678";
char pass[] = "asdfasdf";
int status = WL_IDLE_STATUS;

WiFiClient wifi_client;
MQTTClient mqtt_client;

void handleMessage(String &topic, String &payload) {
  Serial.println("got a message");
  Serial.println(payload);

}
void setup() {
  WiFi.setPins(8, 7, 4, 2);
  Serial.begin(9600);

  
  connectShiftr();
}

void loop() {

  mqtt_client.loop();

  mqtt_client.connected() || connectShiftr();

  delay(1000);

  mqtt_client.publish("/measure", "0");
}

bool connectShiftr() {

  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);

    status = WiFi.begin(ssid, pass);
    delay(10000);
  }

  Serial.println("You're connected to the network");
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  mqtt_client.begin("broker.shiftr.io", wifi_client);
  mqtt_client.onMessage(handleMessage);
  while (!mqtt_client.connect("arduino-servo", "arduido-servo", "arduino-servo")) {
    Serial.println("Connecting to shiftr");
    delay(1000);
  }
  mqtt_client.subscribe("/measure");
  Serial.println("Connected to shiftr");
  return true;
}
