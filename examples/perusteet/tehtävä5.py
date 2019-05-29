kauppalista = []
print("Syötä tuotteet kauppalistaan rivi kerrallaan. Lopeta kirjoittamalla stop")

tuote = input()
while tuote != "stop":
    if not tuote in kauppalista:
        kauppalista.append(tuote)
    tuote = input()

kauppalista.sort()
for rivi in kauppalista:
    print(rivi)