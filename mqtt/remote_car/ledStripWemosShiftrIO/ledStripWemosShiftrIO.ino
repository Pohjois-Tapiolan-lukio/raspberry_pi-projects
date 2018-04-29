#include <Adafruit_NeoPixel.h>

/* WiFi Info */
#define WIFI_SSID "<Wifi name>"
#define WIFI_PASS "<Wifi passwd>"

/* Shiftr Info */
#define SHIFTR_NAME "<device name>"
#define SHIFTR_USER "<Key/User>"
#define SHIFTR_PASS "<Your passwd>"

/* Pins */
#define PIN D4
#define NUM_LEDS 10
#define BRIGHTNESS 255  // Values between 0 ... 255.
#define DEALAY_VAL 10

#include <ESP8266WiFi.h>
//#include <WiFi101.h> // Sisällytetään kirjasto WiFi-yhteyksiä varten
#include <MQTTClient.h> // Sisällytetään kirjasto MQTT-protokollaa varten

WiFiClient net; // WiFi-yhteyksiä ylläpitävä olio
MQTTClient client; // MQTT-protokollan yhteyksiä ylläpitävä olio

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  Serial.begin(9600); 

  //WiFi.setPins(8, 7, 4, 2); // Adafruit Feather M0 WiFi:ä varten tarvittu "uudelleenjärjestely"
  WiFi.begin(WIFI_SSID, WIFI_PASS); 

  client.begin("broker.shiftr.io", net); // Valmistellaan shiftr.io yhteys
  client.onMessage(messageReceived); // Kerrotaan MQTT:lle, että haluamme prosessoida meille lähetetyt viestit funktiossa messageReceived()

  connect(); // Yhdistetään WiFiin ja shiftr.io:hon. Kts. ohjelman viimeinen funktio lisätietoja varten
  client.subscribe("/testing_raspbians"); // Aloitetaan kuuntelemaan /leda, täältä saamme viestejä joissa on sensorien arvoja 
}

void messageReceived(String &topic, String &payload) {
  String message = payload; // 
  if (message == "red"){
    for (int i=0; i <= NUM_LEDS; i++){
      strip.setPixelColor(i, strip.Color(255,0,0));
      }
    strip.show();
    }
  else if (message == "green"){
    for (int i=0; i <= NUM_LEDS; i++){
      strip.setPixelColor(i, strip.Color(0,255,0));
      }
    strip.show();
    }
  else if (message == "blue"){
    for (int i=0; i <= NUM_LEDS; i++){
      strip.setPixelColor(i, strip.Color(0,0,255));
      }
    strip.show();
    }
  else if (message == "nolight"){
    for (int i=0; i <= NUM_LEDS; i++){
      strip.setPixelColor(i, strip.Color(0,0,0));
      }
    strip.show();
    }
  else if (message == "rainbow"){
    chase(strip.Color(255, 0, 0)); // Red
    chase(strip.Color(0, 255, 0)); // Green
    chase(strip.Color(0, 0, 255)); // Blue
    }
}

void loop() {
  client.loop(); // Päivitetään MQTT-yhteydet

  if (!client.connected()) { // Jos yhteys on katkennut... ("!" tarkoittaa "ei" eli tämän rivin voi lukea "jos ei ole niin, että client on connected")
    connect(); // Yhdistetään uudestaan!
  }
}

void connect() {
  Serial.print("Yhdistetaan WiFiin.."); // Printataan Serial-yhteyden kautta, että olemme yhdistämisvaiheessa
  while (WiFi.status() != WL_CONNECTED) { // Toistetaan seuraavaa niin pitkään kun WiFi ei ole yhdistetty (kun "status" ei ole "connected")
    Serial.print("."); // Printataan piste, jotta tiedämme ettei ohjelma jäätynyt
    delay(1000); // Odotetaan sekunti (1000 millisekuntia), sitten tarkistetaan yhteys uudestan
  }
  Serial.println(""); // Printataan hieman tyhjiä rivejä, jotta ulostulo olisi siistimpi

  Serial.print("Yhdistetaan shiftr.io:n..."); // Sama kuin aiemmin WiFi:n kanssa, mutta nyt shiftr.io:n kanssa
  while (!client.connect(SHIFTR_NAME, SHIFTR_USER, SHIFTR_PASS)) { // Yritetään yhdistää shiftr.io:hon
    Serial.print(".");
    delay(1000);
  }
  Serial.println(""); // Printataan taas hieman tyhjiä rivejä siisteyden vuoksi

  Serial.println("Valmista tuli!"); // Nyt on kaikki yhdistelyt valmiita, printataan vielä varmistus Serialiin
}
static void chase(uint32_t c) {
  for (uint16_t i = 0; i < strip.numPixels() + 4; i++) {
    strip.setPixelColor(i  , c); // Draw new pixel
    strip.setPixelColor(i - 4, 0); // Erase pixel a few steps back
    strip.show();
    delay(25);
  }
}
