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
> kuten mitä tekstieditoria käytät, vaan pääosin keskittyy asian ytimeen,
> sarjaliikenteeseen

Suosittelen aloittamaan rakentamalla Arduino-osuuden ensin!

#### Valmistelu ja testaus
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
Korvataan seuraavan komennon loppuosa, ja ajetaan komento.
Tulosteessa näet reaaliajassa Arduinon syötteen

```shell
cat /dev/[laitteen nimi]
```

#### Python sarjaliikennekuuntelija
Pythonissa on valmiiksi kirjastot _input/output_-kommunikaatiolle.

Aloitetaan tuomalla `io`-paketti ohjelmaan
```python
import io
```
Määritellään _merkkilaitteen_ sijainti
> Tässä tarvitset Arduino-merkkilaitetiedoston sijaintia!
> Esimerkkinä toimii `/dev/ttyACM0`

```python
laite = "/dev/ttyACM0"
```

Avataan laite `io`-kirjaston avulla `"r"` (read)-tilassa `with` avainsanan
avulla muuttujaan nimeltä `laiteObjekti`
> `with`-osion jälkeen laite automaattisesti suljetaan
```python
with io.open(laite, "r") as laiteObjekti:
```

Luetaan laitteesta rivi `readline`-methodin avulla
```python
rivi = laiteObjekti.readline()
```

Tulostetaan rivi
```python
print(rivi)
```
