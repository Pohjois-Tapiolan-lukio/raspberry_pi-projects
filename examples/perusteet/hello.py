print("Ohjelma tervehtii sinua ja laskee ikäsi!")
nimi = input("Mikä on sinun nimesi?\n"); # käyttäjältä saatu tieto tallennetaan muuttujaan
print("Terve "+nimi+".") # merkkijonot yhdistetään
ika = input("Kuinka vanha olet?\n") # ika on merkkijono
syntymavuosi = 2019 - int(ika)  # ika muuutetaan int tyyppiseksi
print("Olet syntynyt vuonna ",syntymavuosi,".") #int arvoinen muuttujan arvo liiteteen