#python harjoitus tasan jakajat

numero = int(input("Kirjoita numero: "))
numero = numero + 1

x = range(1, numero)
numero = numero - 1
print("Numeron ", numero, "jakajat ovat:")
for i in x:
	if numero % i == 0:
		print(i)