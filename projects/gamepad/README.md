# Gamepad
Arduino-osuuden tähän projektiin löydät [täältä](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad)

## Yhteenveto
Tässä projektissa opetetetaan Arduinon ja tietokoneen (Raspberry Pi:n) välisen
sarjaliikenteen perusteet.

Tämä kansio sisältää vain sarjaliikenteen kuuntelijan ja sen dokumentaation.

## Tarvittavat osat
- Raspberry Pi ja virtalähde (tai muu GNU/Linux-tietokone)
- Internet yhteys
- Näppäimistö, hiiri ja näyttö
- [Arduino-osuus](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad)

## Ohjeet
Kannattaa aloittaa rakentamalla [Arduino-osuus](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad) ensin!

### Valmistelu ja testaus
Voimme kuunnella Raspberry Pi:lla sarjaliikennettä hyvinkin helposti.

Kytke Arduino USB-johdolla Raspberryyn

Aja terminaalissa komento
<a name "merkkilaite"></a>
```shell
ls -go /dev/serial/by-id/
```
Komento antaa jotain tämän näköistä, josta voi lukea merkkilaitteen
nimen `ttyACM0`
```
total 0
lrwxrwxrwx 1 13 Jul 23 09:26 usb-Arduino__www.arduino.cc__0043_5563231303935110D1A0-if00 -> ../../ttyACM0
```
> Tämä saattaa muuttua, jos kytket Arduinon uudestaan, mutta luultavasti ei

Korvaa seuraavan komennon loppuosa merkkilaitteen nimellä (`ttyACM0`),
ja aja komento. Tulosteessa näet reaaliajassa Arduinon syötteen
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
> Tässä tarvitset Arduino-merkkilaitetiedoston [sijaintia](#merkkilaite)!
> Esimerkkinä toimii `/dev/ttyACM0`

```python
laite = "/dev/ttyACM0"
```

Lisätään tämä koodi estämään Arduinoa resetoitumasta yhteyden
sulkemisen jälkeen
> Tästä koodinpätkästä ei tarvitse huolehtia.
>
> Sen voi jopa jättää pois
```python
with open(laite) as f:
    import termios
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)
```

Luodaan `serial`-olio ja annetaan sille parametrit
- laite on merkkilaitteen absoluuttinen sijainti
- baudrate=9600 asettaa serialin merkkitaajuuden 9600:ksi
> **Tärkeää**: baudrate täytyy olla sama kuin Arduino-koodin
> `Serial.begin`-kutsun parametri `setup`-rutiinissa

- `timeout=1` asettaa 1 sekunnin aikarajan lukemisen kestolle.
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

Suljetaan `serial`-olio
```python
ser.close()
```

Suorita ohjelma Python3:lla.
Tulosteen pitäisi olla tämän näköistä riippuen koodauksesta:
```
b'488,1\r\n'
```
> Tulosteesta saattaa puuttua merkkejä, joka johtuu `readline`-kutsun
> ajanhetkestä. Jos ohjelma tulostaa `b''`, niin suorita ohjelmaa uudestaan.
>
> Jos ohjelma ei millään tulosta mitään muuta, kuin `b''`:
> - yhdistä Arduino uudestaan
> - varmista että Arduino kommunikoi laitteen kanssa [tämän komennon](#catcommand)
> avulla
> - kokeile testiohjelmaa [silmukka.py](silmukka.py)

#### Silmukka
Jotta voimme jatkuvasti lukea sarjaliikennettä, tarvitaan silmukka.

Silmukan ympärille lisäämme `try`-lausekkeen nappaamaan `[CTRL-C]`:n
```python
try:
    while True:
        # tassa luetaan data
except KeyboardInterrupt:
    # tassa suljetaan serial
    print(" Ohjelma suljetaan")
```

Nyt ohjelma näyttää [tältä](silmukka.py)
> **Tärkeää**: While-loopissa ei kuulu olla nukkumisaikaa (`time.sleep`)
> ollenkaan, että `readline` saisi aina tuoreimman datan

#### Datan <i>dekoodaus</i>
> Jos teit oman [koodikielen](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad#koodi),
> lue ohjeet [<i>Säännöllisten lausekkeiden</i> käytölle](#regex)

##### <a name="python-dekoodaus"></a> Dekoodaus Python-koodilla
Tuodaan ohjelmaan `re`-paketti
```python
import re
```

Luodaan valmiiksi säännölinen lauseke -olio
> Tämä nostaa suoritustehoa, kun säännöllistä lauseketta ei tarvitse
> rakentaa joka iteraatio

Tehdään _Säännöllisen lausekkeen olio_

```python
dataRe = re.compile(r"^(\d{1,4}),(\d{1,4}),([01])$")
```

Lauseen analyysi:
- `^`, rivin alku
- `\d`, numero [0-9]
- `{1,4}`, 1-4 kertaa
- `(\d{1,4})`, ensimmäinen ja toinen ryhmä
- `','`, ,-merkki
- `[01]`, merkki 0 tai 1
- `([01])`, kolmas ryhmä
- `$`, rivin loppu

Tämä säännöllinen lauseke ottaa rivistä
```
489,514,0
```
arvot `489`, `514`, `0`

Pythonissa data ryhmitellään `findall`-metodilla
```python
data = "489,514,0"
groups = dataRe.findall(data)
```

> Ihmettelet varmasti, miksei käytetä `str.split`-metodia. Syy on hyvin
> yksinkertainen:
>
> Jos vastaantuleva merkkijono on tämän näköinen
>
> `,231321,,,,9000,,,`
>
> sen `split(',')`-kutsu palauttaisi listan
>
> `['', '231321', '', '', '', '9000', '', '', '']`
>
> Nyt pitäisi validoida lista, joka olisi tuskallista.
> Listan validoinnin sijasta voidaan sekä validoida, että
> napata arvot merkkijonsta samaan aikaan Pythonin _säännöllisten
> lausekkeiden_ avulla
>
> Tässä olisi listan validoinnin esimerkkikoodi (älä käytä missään nimessä!)
```python
lista = data.split(',')

def validate(lista):
    if len(lista) != 3:
        return False
    for i in range(3):
        arvo = lista[i]
        try:
            if not int(arvo) in range(0,(1023,2)[i > 2]):
                return False
        except ValueError:
            return False
    return True
```
> Kuten nähdään, datan validointi on tuskaa ilman _säännöllisiä lausekkeita_

Jos data on virheellistä, esimerkiksi
```python
data = "0,512,9"
data = "12345,512,0"
data = ",231321,,,,9000,,,"
```
niin `dataRe`-olion `findall`-funktio palauttaa
```python
[]
```
josta on tosi helppoa testata, onko data validia `if`-lausekkeen
avulla.

Nyt yhdistetään datan dekoodaus ohjelmaan
```python
try:
    while True:
        rivi = ser.readline().decode('ascii').strip('\r\n')
        groups = dataRe.findall(rivi)
        if not groups: # jos groups on []
            print("Rikkinaista dataa {}".format(rivi))
            continue
        print(groups)
except KeyboardInterrupt:
    ser.close()
    print(" Ohjelma suljetaan")
```
> `readline`-funktio palauttaa `bytes`-olion. Arduinon sarjaliikenne
> on 'ascii'-enkoodattua, joten se pitää dekoodata 'ascii':sta
> `str`-olioksi. Sitten siitä poistetaan `Serial.println`-funktion
> lisäämä rivinvaihto

Ohjelma näyttää tällä hetkellä [tältä](prosessointi.py)

### Python <i>uinput</i>
Jos halutaan ohjelman tuottavan peliohjain-tapahtumia (tai mitä tahansa muita)
tarvitsemme input-merkkilaitteen.

Uinput on _kernel moduuli_, jolla voi emuloida input-laitteita.

`python-uinput` <https://github.com/tuomasjjrasanen/python-uinput> on
Python-paketti, joka käärii uinput-käsittelyfunktiot Pythoniin.

#### Python-uinput asennus
> Asenna Raspberry Pi:lle `git`, jos se ei ole vielä asennettuna
> `sudo apt-get install git`

```shell
git clone https://github.com/tuomasjjrasanen/python-uinput.git
cd python-uinput
python3 setup.py build
sudo python3 setup.py install
```

#### Uinput-moduulin lataus
Uinput kernel moduuli aktivoidaan komennolla
```shell
sudo modprobe uinput
```
> Tämä täytyy tehdä uudelleen, joka kerta kun käynnistät
> Raspberryn uudelleen

Moduuli on aktiivinen jos näet tuloksen komentoon
```shell
lsmod |grep uinput
```

#### Uinput Pythonissa
Tuodaan paketti ohjelmaan
```python
import uinput
```

Luodaan `uinput`-laite `with`-lausekkeella
> Ohjelmassa tämä tulee `try`-lausekkeen ympärille
```python
with uinput.Device([uinput.ABS_X]) as gamepad:
    # try ...
    gamepad.emit(uinput.ABS_X, 12345)
    # except ...
```

##### Tapahtumien nimet
Tapahtumien nimet, kuten `ABS_X`, `BTN_SOUTH` löytyy sivuilta

<https://www.kernel.org/doc/Documentation/input/gamepad.txt>
<https://www.kernel.org/doc/html/v4.14/input/gamepad.html>

> Jos haluat emuloida oikeaa gamepadia, eli mitä esim. Xbox-ohjain lähettää
> saat apua sivulta
> <https://askubuntu.com/questions/114895/how-can-a-gamepad-control-the-mouse>

Nyt voidaan lisätä akseleita ja nappeja uinput-laitteeseen
```python
with uinput.Device([uinput.ABS_X, uinput.ABX_Y, uinput.BTN_SOUTH]) as gamepad:
```
Laitetaan `Device`-luokan initialisointiargumenteiksi lista akseleista ja
napeista, joita ohjelma emuloi

Muutetaan `groups`-listan ensimmäisen alkion alkiot kokonaisluvuiksi
> Rivi tulee vasta `if ...: ... continue`-osan jälkeen,
> koska muuten groups[0] palauttaa `IndexError: list index out of range`
```python
groups = [int(arvo) for arvo in groups[0]]
```

Käytetään uuden `groups`-listan alkioita tapahtumien arvoina
```python
gamepad.emit(uinput.ABS_X, groups[0])
gamepad.emit(uinput.ABS_Y, groups[1])
gamepad.emit(uinput.BTN_SOUTH, groups[2])
```

Useimmat ohjelmat ja pelit lukevat absoluuttiset tapahtumat kokonaislukuina
[-32768,32767] välillä, joten Arduinon analogisia arvoja pitää skaalata ja
siirtää oikein: `32767 - 65535 * arvo//1023`

Joystickin nappi on aktivoitunut kun digitaalinen arvo on 0, joten sen arvosta
pitää ottaa komplementti: `1 - arvo`

Python-koodi näyttää [tältä](ohjelma.py)
> Huomaa, että koodi pitää suorittaa pääkäyttäjänä, koska uinput:iin
> kirjoittaminen vaatii pääkäyttäjän oikeudet

### Ohjelman käyttö ja tapahtumien lukeminen
Aktivoidaan uinput-kernelmoduuli
```shell
sudo modprobe uinput
```

Käynnistetään ohjelma
```shell
sudo ./ohjelma.py
```
> Virhe
> `FileNotFoundError: [Errno 2] No such file or directory: '/dev/ttyACM0'`
> tarkoittaa, että Arduino ei ole kytketty
>
> Virhe
> `OSError: [Errno 19] Failed to open the uinput device: No such device`
> tarkoittaa, että uinput ei ole aktivoitu. Voit aktivoida sen
> `sudo modprobe uinput`
>
> Virhe
> `PermissionError: [Errno 13] Failed to open the uinput device: Permission denied`
> tarkoittaa, että käyttäjälläsi ei ole oikeutta kirjoittaa uinput-laitteeseen.
> Aja ohjelma pääkäyttäjänä komennolla `sudo python3 ohjelma.py`

Voit monitoroida input-tapahtumia ohjelmalla `evtest` toisesta terminaalista

Näillä sivuilla voit testata miten joystickisi ja nappisi toimivat
- <http://html5gamepad.com/>, näyttää gamepad input-tapahtumat
- <https://itch.io/games/html5/input-gamepad>, lista HTML5 pelejä, jotka
toimivat gamepadilla

<br/>
<br/>

---
### <a name="regex"></a> Dekoodataan oma data
> Tätä ei ole pakko lukea, paitsi jos teit oman [koodikielen](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad#koodi)

Datan dekoodaamiseen käytetään [<i>Säännöllisiä lausekkeita</i>](https://fi.wikipedia.org/wiki/S%C3%A4%C3%A4nn%C3%B6llinen_lauseke)
Säännölliset lausekkeet käsittelevät merkkijonoja.
> Dekoodaus ei tässä tarkoita esimerkiksi
> heksadesimaalista desimaaliin muutosta.
> Sellaista dekoodausta ei tehdä säännöllisillä lausekkeilla

Säännöllisten lausekkeiden avulla voidaan _groupata_ osumia,
_vahvistaa_ datan _eheys_ tai _korvata_ osumia tekstillä.

#### Materiaali
Lue Aallon wikistä sivut 16-20 [Säännöllisistä lausekkeista](https://wiki.aalto.fi/download/attachments/63548818/luento9.pdf?version=1&modificationDate=1332923875000&api=v2)
> Kalvolla on muitakin hyödyllisiä aiheita, joita kannattaa lukea

Lue Linux.fi artikkelista [kaarisulkujen käytöstä](https://www.linux.fi/wiki/S%C3%A4%C3%A4nn%C3%B6llinen_lauseke#Sulut:_.28_ja_.29)
ja [hakasulkujen käytöstä](https://www.linux.fi/wiki/S%C3%A4%C3%A4nn%C3%B6llinen_lauseke#Merkkiluokat:_.5B.5D)
> **Huomaa**: kaarisulut yleisissä säännöllisissä lausekkeissa ovat
> eri asia, kuin Pythonin säännöllisissä lausekkeissa, joissa ne (kaarisulut)
> ryhmittelevät datasta tärkeät osat
>
> Pythonissa kaarisulkuja vastaa `(?:regex tähän)` esim
> `^(?:[0-9]+\s)+$` osuu kaikkiin merkkijonoihin, joissa on välilyönnillä
> erotettuja lukuja

Käy interaktiivinen [harjoitus](https://regexone.com/) läpi

Pythonin Säännöllisissä lausekkeissa apua löydät täältä
<https://docs.python.org/3/howto/regex.html>

Kun olet luonut koodaustasi vastaavan säännöllisen lausekkeen, laita se
ohjelmaan
```python
dataRe = re.compile(r"tanne regex")
```
