lista = []
luku = input("Syötä lukuja. Lopeta kirjoittamalla stop\n")

while luku != "stop":
    lista.append(luku)
    luku = input()

lista.sort(reverse = True)

for i in lista:
    print(i)

summa = 0
for i in lista:
    summa += int(i)
keskiarvo = summa / len(lista)
print("Keskiarvo on ", keskiarvo)

suurin = 0
for i in lista:
    if int(i) > suurin:
        suurin = int(i)
print("Suurin luku on ", suurin)