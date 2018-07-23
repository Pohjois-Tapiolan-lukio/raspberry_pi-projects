# Gamepad
Arduino-osuuden tähän projektiin löydät [täältä](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad)!

## Yhteenveto
Tässä projektissa opetetetaan Arduinon ja tietokoneen (Raspberry Pi:n) välisen
sarjaliikenteen perusteet.

Tämä kansio sisältää vain sarjaliikenteen kuuntelijan ja sen dokumentaation.

## Tarvittavat osat
- Raspberry Pi (tai muu GNU/Linux-tietokone)
- Raspberry Pi:n virtalähde (vain Pi:ta varten)

## Ohjeet
> **Huomaa**: Nämä ohjeet eivät ole tarkasti tiettyä konfiguraatiota varten,
> kuten mitä tekstieditoria käytät, vaan keskittyy asian ytimeen

Kannattaa aloittaa rakentamalla [Arduino-osuus](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad) ensin!

### Valmistelu ja testaus
Voimme kuunnella Raspberry Pi:lla sarjaliikennettä hyvinkin helposti.

---
Aja terminaalissa komento
```shell
ls -go /dev/serial/by-id/
```
Komento antaa jotain tämän näköistä, josta voi lukea laitteen nimen `ttyACM0`
```
total 0
lrwxrwxrwx 1 13 Jul 23 09:26 usb-Arduino__www.arduino.cc__0043_5563231303935110D1A0-if00 -> ../../ttyACM0
```
> Tämä saattaa muuttua, jos kytket Arduinon uudestaan

Korvaa seuraavan komennon loppuosa, ja aja komento.
Tulosteessa näet reaaliajassa Arduinon syötteen
<a name="catcommand"></a>
```shell
cat /dev/[laitteen nimi]
```

### Python sarjaliikennekuuntelija
Kuuntelija tarvitsee paketin `pyserial`
```shell
sudo apt-get install python3-pip
sudo pip3 install pyserial
```

Tuodaan `pyserial` ohjelmaan
```python
import serial
```

Määritellään _merkkilaitteen_ sijainti
> Tässä tarvitset Arduino-merkkilaitetiedoston sijaintia!
> Esimerkkinä toimii `/dev/ttyACM0`.

```python
laite = "/dev/ttyACM0"
```

Lisätään tämä koodi estämään Arduinoa resetoitumasta yhteyden
sulkemisen jälkeen
```python
with open(laite) as f:
    import termios
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)
```

Luodaan `serial` objekti ja annetaan sille parametrit
- laite on merkkilaitteen absoluuttinen sijainti
- baudrate=9600 asettaa serialin merkkitaajuuden 9600:ksi
> **Tärkeää**: baudrate täytyy olla sama kuin Arduino-koodin
> `Serial.begin`-kutsun parametri

- timeout=1 asettaa 1 sekunnin aikarajan lukemisen kestolle.
Jos 1 sekunnin sisällä ei ole tullut merkkijonoa joka sisältää `\n`
(uudenrivin) -symbolin, niin `readline` funktio palauttaa
siihen mennessä tulleen datan. Timeout on hyödyllinen, koska ilman
sitä ohjelma olisi 'tukossa', jos `\n`-merkki jää tulematta.
```python
ser = serial.Serial(laite, baudrate=9600, timeout=1)
```

Luetaan ja tulostetaan rivi
```python
rivi = ser.readline()
print(rivi)
```

Suljetaan `serial` objekti
```python
ser.close()
```

Suorita ohjelma.
Tulosteen pitäisi olla tämän näköistä riippuen koodauksesta:
```
b'488,1\r\n'
```
> Tulosteesta saattaa puuttua merkkejä, joka johtuu `readline`-kutsun
> ajanhetkestä. Jos ohjelma tulostaa `b''`, niin suorita ohjelmaa uudestaan.
>
> Jos ohjelma ei millään tulosta mitään muuta:
> - kokeile testiohjelmaa [silmukka.py](silmukka.py)
> - yhdistä Arduino uudestaan
> - varmista että Arduino kommunikoi laitteen kanssa [tämän](#catcommand)
komennon avulla

#### Silmukka
Jotta voimme jatkuvasti lukea sarjaliikennettä, tarvitaan silmukka.

Silmukan ympärille lisäämme `try`-lausekkeen nappaamaan `[CTRL-C]`:n
```python
try:
    while True:
        # luetaan data
except KeyboardInterrupt:
    # suljetaan serial
    print(" Ohjelma suljetaan")
```

Nyt ohjelma näyttää [tältä](silmukka.py)

#### Datan <i>dekoodaus</i>
> Jos teit oman [koodikielen](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad#koodi),
> lue ohjeet [<i>Säännöllisten lausekkeiden</i> käytölle](#regex)

Tuodaan ohjelmaan `re`-paketti
```python
import re
```

Tehdään _Säännöllisen lausekkeen objekti_
`re.compile(r"`![](regex1.png)`")`

---
### <a name="regex"></a> Dekoodataan data
> Tätä ei ole pakko lukea, mutta jos teit oman [koodikielen](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad#koodi)
> Arduinolle, tämä on oleellista aineistoa

Datan dekoodaamiseen käytetään [<i>Säännöllisiä lausekkeita</i>](https://fi.wikipedia.org/wiki/S%C3%A4%C3%A4nn%C3%B6llinen_lauseke)
Säännölliset lausekkeet käsittelevät merkkijonoja.

Säännöllisten lausekkeiden avulla voidaan _groupata_ osumia,
_vahvistaa_ datan _eheys_ tai _korvata_ osumia tekstillä.

#### Materiaali

Lue Aallon wikistä sivut 16-20 [Säännöllisistä lausekkeista](https://wiki.aalto.fi/download/attachments/63548818/luento9.pdf?version=1&modificationDate=1332923875000&api=v2)
> Kalvolla on muitakin hyödyllisiä aiheita, joita kannattaa lukea

Lue Linux.fi artikkelista [kaarisulkujen käytöstä](https://www.linux.fi/wiki/S%C3%A4%C3%A4nn%C3%B6llinen_lauseke#Sulut:_.28_ja_.29)
ja [hakasulkujen käytöstä](https://www.linux.fi/wiki/S%C3%A4%C3%A4nn%C3%B6llinen_lauseke#Merkkiluokat:_.5B.5D)

Käy interaktiivinen [harjoitus](https://regexone.com/) läpi

Pythonin Säännöllisissä lausekkeissa hyötyä löydät täältä
<https://docs.python.org/3/howto/regex.html>
