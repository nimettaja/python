import random

a = random.sample(range(1000), 100)
b = random.sample(range(1000), 100)
print("Näissä (sekalaisesti luoduissa) listoissa yhteistä on: ")
for i in a:
	if i in b:
		print(i)