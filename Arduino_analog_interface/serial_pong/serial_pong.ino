#define PING_INTERVAL 2
unsigned long time;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);
  ping();
}

void ping() {
  Serial.write("ping\n");
  time = millis();
}

void loop() {
  // Read Serial
  String input = "";
  while (Serial.available()) {
    input += Serial.readString();
  }
  
  // Send another ping if we get a pong
  if (input.indexOf("pong") != -1) {
    ping();
  }

  // If it has been PING_INTERVAL seconds, send another ping
  if (millis() - time > PING_INTERVAL * 1000) {
    Serial.write("Trying again: ");
    ping();
  }
}
