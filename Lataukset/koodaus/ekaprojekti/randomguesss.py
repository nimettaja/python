import random
import time

x = random.sample(range(1, 9), 1)
testi = [range(1, 10)]


kysymys = 0
while kysymys != "exit":
	userinput = input("Arvaa numero 1-9:n välillä: ")
	if userinput in [range(1, 10)]:
		print("Arvasit ", userinput)
		if userinput == x:
			print("Arvasit oikein!")
		elif userinput != x:
			print("Arvasit väärin.")
		elif userinput == "":
			print("Ei tyhjää!")
	kysymys = input("Halutako yrittää uudestaan? Paina enter yrittääksesi uudestaan ja kirjoita exit lopettaaksesi.")
	if kysymys == "exit":
		break