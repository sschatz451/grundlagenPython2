# variable

x = True
while(x):
	aktion =  input("Welche Aktion willst du? (+|-|*|/): ")
	print ("Aktion", aktion, "wird ausgeführt...")

	eingabe1 = input("Bitte erste Zahl eingeben: ")
	print ("Zahl 1=", eingabe1)

	eingabe2 = input("Bitte zweite Zahl eingeben: ")
	print ("Zahl 2=", eingabe2)

	if (aktion == "+"):
		ausgabe = int(eingabe1) + int(eingabe2)
	if (aktion == "-"):
		ausgabe = int(eingabe1) - int(eingabe2)
	if (aktion == "*"):
		ausgabe = int(eingabe1) * int(eingabe2)
	if (aktion == "/"):
		if (eingabe2 == 0):
			print("Fehler, keine Division durch 0 möglich!")
		else:
			ausgabe = int(eingabe1) / int(eingabe2)
		
	print(eingabe1, aktion, eingabe2, " = ", ausgabe)
	z = True
	while(z):
		ende = input("\nNochmal rechnen? (Ja/Nein): ")
		if (ende == "Ja"):
			z = False
			x = True
		elif (ende == "Nein"):
			x = False
			z = False
		else:
			print("Fehler")
