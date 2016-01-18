import sys
import os

vuosi = input("Vuosi: ")
os.system("cls" if os.name == "nt" else "clear")

try:
	val = int(vuosi)
except:
	sys.exit("Tuo ei ole numerosarja!")

tasa = int(vuosi) % 4
tasa1 = int(vuosi) % 100

tasa2 = ""

if tasa == 0:
	print("Vuosi ", vuosi, " on karkausvuosi.")
elif tasa1 == 0:
	tasa2 = int(vuosi) % 400
elif tasa2 == 0:
	print("Vuosi ", vuosi, " on karkausvuosi.") 
else:
	print("Vuosi ", vuosi, " ei ole karkausvuosi")