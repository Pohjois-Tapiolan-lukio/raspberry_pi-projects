import paho.mqtt.client as mqtt # Tuodaan mqtt kirjasto

def on_connect(client, userdata, flags, rc): # Funktio, joka pyöriteään aina, kun yhdistetään palvelimeen.
    print("Yhdistettiin koodilla:", str(rc)) # Tulostetaan koodi jolla ollaan yhditetty palvelimeen.
    client.subscribe("viestit") # Tilataan viesti kanava (topic). Eli vastaanotetaan vain viestit, jotka tulevat tälle kanavalle.

def on_message(client, userdata, msg): # Funktio, joka pyöriteään aina, kun saadaa viesti.
    print(msg.payload.decode("utf-8")) # Tulostetaan viesti.


client = mqtt.Client(client_id = "Kuutelia") # Määritetään käyttäjä (client). Annetaan sille nimeksi "Kuuntelia".
client.on_connect = on_connect # Määritetään funktio, joka pyöritetään aina, kun yhdistetään palvelimeen.
client.on_message = on_message # Määritetään funktio, joka pyöritetään aina, kun saadaan viesti.
client.username_pw_set("52677e83", password = "91f241d7a9bd055b") # Määritetään Avain sekä Salasana.
client.connect("broker.shiftr.io", 1883, 60) # Yhdistää shiftr.io:n palvelimelle. (ip, port, timeout)
client.loop_forever() # Pyöritetään ohjelmaa loputtomiin (siihen asti että sen itse lopetamme).
