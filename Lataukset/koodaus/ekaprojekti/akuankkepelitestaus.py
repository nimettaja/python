import time
import string

lista = [
	"Aku Ankka", "Tupu", "Hupu", "Lupu", "Roope Ankka", "Iines Ankka", "Hannu Hanhi", "Milla Magia", "Kulta-Into Pii", "Kroisos Pennonen", "Karhukopla", "Mummo Ankka", "Pelle Peloton", "Riitta Hanhi", "Touho Ankka", "Leenu", "Liinu", "Tiinu", "Lipi Luikuri", "Kisumisu"
]
mikkilista =[
	"Mikki Hiiri", "Hessu Hopo", "Tohtori Staattinen"
]
pelaaja = input("Kirjoita nimesi: ")
print("Kuinka monta Aku-Ankka hahmoa muistat? Koeta kirjoittaa nimet sukunimineen.")
amount = 0
while len(lista) > 0:
	nimi = input("Hahmo: ")
	if nimi == "":
		break
	if nimi in lista:
		print("Oikein! Seuraava. (Tai paina enter lopettaaksesi)")
		amount += 1
		lista.remove (nimi)
	elif nimi in mikkilista:
		print("Tuo ei ole Aku-Ankka hahmo, se on Mikki Hiiri -tarinoiden hahmo.")
	else:
		print(nimi, "Ei ole Aku-Ankka hahmo.")
print("Muistit", amount, "Aku-Ankka -hahmoa. Kiitos kun pelasit,", pelaaja, "\n  Copyright 2016 (C) Teemu Rannikko")

valinta = input("Haluatko kirjoittaa nimesi pistetaulukkoon? (k/e) :")
if valinta == "k":
	pisteet = str("\n" + str(pelaaja) + ": " + str(amount) + " pistettä.")
	f = open("pistetaulukko.txt", "a")
	str(pisteet)
	f.write(pisteet)
	f.close()
elif valinta == "e":
	print("Valitsit ei. Tässä pistetaulukko.")

tiedosto = open("pistetaulukko.txt", "r")

for line in tiedosto:
	line = str(line)
	print(line)
	
tiedosto.close()