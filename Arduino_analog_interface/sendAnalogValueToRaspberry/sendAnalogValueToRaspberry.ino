void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(A0);
   Serial.print(sensorValue);
   delay(10);
   Serial.print("\n");
}
