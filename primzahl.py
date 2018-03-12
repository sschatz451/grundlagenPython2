# Primzahl
# If Eingabe ist Primzahl
# Sebastian
def isPrime(n):

	if (n <= 1):
		return False

	for p in range(2,n):
		if (n % p == 0):
			return False
		else:
			return True

print("Willkommen beim Primzahltester")
z = input("Bitte Zahl eingeben: ")
z = int(z)
print("\n")
if ( isPrime(z)):
	print(z, "ist eine Primzahl.")
else:
	print(z, "ist keine Primzahl.")
