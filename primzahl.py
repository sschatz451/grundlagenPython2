# Primzahl
# If Eingabe ist Primzahl
# Sebastian
eingabe = input("Bitte Zahl eingeben: ")
counter = 0
x = True
if (zahl <= 1):
	print(zahl, "ist keine gültige eingabe.")
else:
	while(x):
		if (zahl % i == 0):
			counter = 1
		if (i == 1):
			x = False
			zahl = zahl+1

if (counter == 1):
	print(zahl, "ist keine Primzahl.")
else:
	print(zahl, "ist eine Primzahl.")
