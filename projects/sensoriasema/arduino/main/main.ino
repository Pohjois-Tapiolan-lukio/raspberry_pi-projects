#include <SPI.h>
#include <WiFi101.h>
#include <MQTTClient.h>

#define TRIGGER 9
#define ECHO 10

#include "arduino_secrets.h"
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int status = WL_IDLE_STATUS;

WiFiClient wifi_client;
MQTTClient mqtt_client;

void handleMessage(String &topic, String &payload) {
  Serial.println("got a message");
  Serial.println(payload);
  if (payload == "0") {
    float distance = ultrasonic();
    Serial.println(distance);
    mqtt_client.publish("/data", (String) distance);
  }

}
float ultrasonic() {
  digitalWrite(TRIGGER, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER, LOW);

  float duration = pulseIn(ECHO, HIGH);

  return duration / 58.2;

}
void setup() {
  WiFi.setPins(8, 7, 4, 2);
  Serial.begin(9600);
  
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);
  
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

    status = WiFi.begin(ssid, pass);
    delay(10000);
  }

  Serial.println("You're connected to the network");
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  mqtt_client.begin("broker.shiftr.io", wifi_client);
  mqtt_client.onMessage(handleMessage);
  while (!mqtt_client.connect(SHIFTR_NAME, SHIFTR_USER, SHIFTR_PASS)) {
    Serial.println("Connecting to shiftr");
    delay(1000);
  }
  mqtt_client.subscribe("/measure");
  Serial.println("Connected to shiftr");
  return true;
}
