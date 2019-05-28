void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
delay(5000);
Serial.println("ping");
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() > 0){
    String value = Serial.readString();
    if (value == "pong"){
      Serial.println("ping");
      delay(500);
      }  
    }
}
