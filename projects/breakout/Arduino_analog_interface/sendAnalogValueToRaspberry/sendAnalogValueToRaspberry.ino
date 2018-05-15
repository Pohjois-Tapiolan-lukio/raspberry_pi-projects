void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(A0);
  Serial.print(sensorValue);
  // Delay 20ms, as the game runs every 10ms, to not clog up the serial conn
  delay(20);
  Serial.print("\n");
}
