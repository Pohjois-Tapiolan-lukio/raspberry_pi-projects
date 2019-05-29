import mqtt.*;

MQTTClient client;

void setup() {
  client = new MQTTClient(this);
  client.connect("mqtt://shiftr-key:shiftr-secret@broker.shiftr.io", "processing");
  
  size(1280, 720);
  background(255,255,255);  
}

void draw() {
  
}

void keyPressed() {
  client.publish("/hello", "world");
}

void clientConnected() {
  println("client connected");

  client.subscribe("messages");
}

void messageReceived(String topic, byte[] payload) {
  String message = new String(payload);
  println("new message: " + topic + " - " + new String(payload));
  
  if (message.equals("k")){
    colorMode(RGB,100);
    stroke(0, 0, 255);
    strokeWeight(10);
    ellipse(width/2, height/2, height/4, height/4);
  }
  
  else if (message.equals("s")){
    background(255,255,255);
  }
}

void connectionLost() {
  println("connection lost");
}
