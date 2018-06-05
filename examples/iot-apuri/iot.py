#!/bin/python3
"""
IoT-apuri on kirjasto jolla saa helposti tehtyä ohjelmia,
jotka hyödyntävät Googlen Assistantia ääniohjaukseen,
ja Shiftr.io:ta tiedonsiirtoon.

Lisää README.md:ssä.
"""

import paho.mqtt.client as mqtt

DATA = {
    "subs": [],
    "connected": False
}

DEBUG = False

def setup(shiftr_name, shiftr_key, shiftr_pass):
    """
    Yhdistää shiftr.io palvelimelle ja käynnistää Google Assistantin.
    """

    def handle_connect(_client, _userdata, _flags, _code):
        """
        Kutsutaan kun client yhdistää shiftr.io:n palvelimelle.
        """
        print("Shiftr.io connected!")
        DATA["connected"] = True

    def handle_message(_client, _userdata, msg):
        """
        Kutsutaan kun client saa viestin shiftr.io:n palvelimilta.
        """
        call_subscriptions(msg.topic, msg.payload.decode("utf-8"))

    if shiftr_key == "shiftr-key":
        print("HUOM!  Muista korvata 'shiftr-key' omalla shiftr keylläsi!")
    if shiftr_pass == "shiftr-secret":
        print("HUOM!  Muista korvata 'shiftr-secret' omalla shiftr secretilläsi!")
    client = mqtt.Client(client_id=shiftr_name)
    client.on_connect = handle_connect
    client.on_message = handle_message
    client.username_pw_set(shiftr_key, password=shiftr_pass)
    client.connect("broker.shiftr.io", 1883, 60)
    client.loop_start()
    DATA["client"] = client
    while not DATA["connected"]:
        pass

def call_subscriptions(topic, message):
    """
    Kutsuu iot.subscribe-funktiolla alustettuja funktiota, riippuen topic:sta.
    """
    if DEBUG:
        print("New message: '" + message + "' (in topic: '" + topic + "')")
    for sub in DATA["subs"]:
        (func, topic_) = sub
        if topic == topic_:
            func(message)

def publish(topic, message):
    """
    Julkaise uusi viesti (message) annetulla aiheella (topic),
    jota muut laitteet voivat kuunnella subscribe-funktiolla.
    """
    if DEBUG:
        print("Publish: '" + message + "' (topic: '" + topic + "')")
    DATA["client"].publish(topic, message)

def subscribe(topic):
    """
    Kuuntele viestejä annetusta aiheesta (topic), ja
    kutsu annettu funktio kun shiftr.io:sta saadaan uusi viesti.
    """
    if not DATA["connected"]:
        print("HUOM!  iot-setup -funktio pitää kutsua ennen iot.subscribe -funktioita!")
        return lambda f: f

    def handler(func):
        """
        Lisää annettu funktio subscriptioneihin.
        """
        if DEBUG:
            print("Subscribe: " + topic)
        DATA["subs"].append((func, topic))
        DATA["client"].subscribe(topic)
    return handler
