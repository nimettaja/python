lista = [1, 2, 3]
lopetus = "e"
pelaaja1 = input("Pelaajan 1 nimi: ")
pelaaja2 = input("Pelaajan 2 nimi: ")
pelaaja1pisteet = 0
pelaaja2pisteet = 0

while lopetus == "e":
	print("Hei, ", pelaaja1, " ja ", pelaaja2, "! Tervetuloa kivi, paperi, sakset -peliin!" )
	
	pelaaja1valinta = int(input(pelaaja1 + ", valitse kivi (1), paperi (2) tai sakset (3): "))
	pelaaja2valinta = int(input(pelaaja2 + ", valitse kivi (1), paperi (2) tai sakset (3): "))
	
	for piste in pelaaja1pisteet:
		#pelaajan 1 pisteytys
		if pelaaja1valinta == 1 and pelaaja2valinta == 3:
			print(pelaaja1, ":n pisteet +1.")
			print("Nyt", pelaaja1, ":n pisteet ovat: ", pelaaja1pisteet, ".")
			pelaaja1pisteet += 1
		elif pelaaja1valinta == 2 and pelaaja2valinta == 1:
			print(pelaaja1, ":n pisteet +1.")
			print("Nyt", pelaaja1, ":n pisteet ovat: ", pelaaja1pisteet, ".")
			pelaaja1pisteet += 1
		elif pelaaja1valinta == 3 and pelaaja2valinta == 2:
			print(pelaaja1, ":n pisteet +1.")
			print("Nyt", pelaaja1, ":n pisteet ovat: ", pelaaja1pisteet, ".")
			pelaaja1pisteet += 1
	for piste in pelaaja1pisteet:
		#pelaajan 2 pisteytys
		if pelaaja2valinta == 1 and pelaaja2valinta == 3:
			print(pelaaja2, ":n pisteet +1.")
			print("Nyt", pelaaja2, ":n pisteet ovat: ", pelaaja2pisteet, ".")
			pelaaja2pisteet += 1
		elif pelaaja2valinta == 2 and pelaaja1valinta == 1:
			print(pelaaja2, ":n pisteet +1.")
			print("Nyt", pelaaja2, ":n pisteet ovat: ", pelaaja2pisteet, ".")
			pelaaja2pisteet += 1
		elif pelaaja2valinta == 3 and pelaaja1valinta == 2:
			print(pelaaja2, ":n pisteet +1.")
			print("Nyt", pelaaja2, ":n pisteet ovat: ", pelaaja2pisteet, ".")
			pelaaja2pisteet += 1
		if pelaaja2pisteet == 3:
			print(pelaaja2, " voitti!")
		if pelaaja1pisteet == 3:
			print(pelaaja1, " voitti!")

	lopetus = input("Haluatko lopettaa? (k/e): ")
	if lopetus == "k":
		break
	elif lopetus == "e":
		lopetus = "e"
