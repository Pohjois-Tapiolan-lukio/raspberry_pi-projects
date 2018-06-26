import json
import requests
import speech_recognition as sr
from google_speech import Speech



r=sr.Recognizer()

hostname=

def say(message,lang="en"):
    Speech(message, lang).play("")
def getText():
    with sr.Microphone() as source:
        print("Now listening:")
        audio = r.listen(source)
    return r.recognize_google(audio).lower()

while True:
    koodi=input("Lue koodi: ")
    res=requests.get("http://"+hostname+"/get?koodi="+koodi)
    print(res.text)
    o=json.loads(res.text)
    found=o["found"]
    print(found)
    if found=="true":
        say("This product is in the database")
        say("This is "+o["nimi"])
    else:
        say("This product is not in the database")
        say("What is this?")
        t=getText()
        print(t)
        ans=""
        while "yes" not in ans:

            say("is this "+t)
            ans=getText()
            print(ans)
            if "yes" in ans:
                say("Okay, this is "+t)
            else:
                say("What is it, then?")
                t=getText()
        res=requests.get("http://"+hostname+"+koodi+"&nimi="+t+"&hinta=0&lkm=0")
