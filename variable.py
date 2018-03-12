# variable

aktion =  input("Welche Aktion willst du? (+/-/*/:): ")
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
	ausgabe = int(eingabe1) / int(eingabe2)
	
print(eingabe1, aktion, eingabe2, " = ", ausgabe)
