import paho.mqtt.client as mqtt # Tuodaan mqtt kirjasto

nimi = input("\nNimesi:\n") # Kysyy nimen ja tallettaa sen muuttujaan.
viesti = input("\nViesti:\n") # Kysyy viestin ja tallettaa sen muuttujaan.
client = mqtt.Client(client_id = nimi) # Määritetään käyttäjäksi (Client) nimi muuttja.
client.username_pw_set("52677e83", password="91f241d7a9bd055b") # Määritetään Avain sekä Salasana.
client.connect("broker.shiftr.io", 1883, 3) # Yhdistää shiftr.io:n palvelimelle. (ip, port, timeout)
client.loop_start()
client.publish("viestit", payload = (nimi + " : " + viesti)) # Lähetetään viesti.
print("Viesti lähetetty") # Tulostetaan "Viesti lähetetty"
