# variable
'''
a = 10
b = 20

summe = a + b

print("Die Summe von", a, " + ", b, "=", summe)
'''
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

'''
zahl = input("Welche Zahl wählst du?")
zahl = int(zahl)
zahl2 = int("23")

zahlA = "123"
zahlB = "456"

print(zahlA+zahlB)

ZahlC = 987
text = str(zahLC)
'''