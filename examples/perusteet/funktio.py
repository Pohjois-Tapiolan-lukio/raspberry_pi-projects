# Ohjelmassa on pääfunktio main() ja apufunktio tulosta(lukumaara, nimi)
# tulosta-funktiolla on kaksi parametria, joille on annettava arvo kun funktiota kutsutaan.

def main(): # Määritellään pääohjelma
    print("Ohjelma tervehtii sinua monta kertaa.")
    nimi = input("Mikä on nimesi?\n")
    lkm = input("Kuinka monesti tervehditään? Anna kokonaisluku 1-5.\n")
    lkm = int(lkm)
    tulosta(lkm, nimi) # funktion kutsu

def tulosta (lukumaara, nimi): # Määritellään apufunktio
    if lukumaara <= 0:
        print("Hei hei ", nimi,".")
    else:
        for laskuri in range(lukumaara):
            print("Terve "+nimi+".")

main() # kutsutaan suoritettevaksi pääohjelma joka kutsuu funktiota eli aliohjelmaa