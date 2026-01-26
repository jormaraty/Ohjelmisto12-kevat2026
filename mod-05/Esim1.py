# Esimerkkejä Range-funktion käytöstä

# toistetaan moikkaus 5 kertaa,
# muuttuja i on ns. kierrosmuuttuja.
# Huom. muuttuja i saa arvot 0 - 4.
for i in range(5):
    print("Moi!")

# tulostetaan luvut 1 ... 15,
# Huom. alkuarvo 1 otetaan mukaan, loppuarvoa 16 EI.
for arvo in range(1, 16):
    print(arvo)

print("\nTulostetaan kolmella jaolliset luvut väliltä 3-30")
# 3 parametrin versio range-funktiosta, parametrit ovat
# alkuarvo, loppuarvo ja ns. askel (step).
# Askel määrää kuinka paljon kierrosmuuttujan arvoa kasvatetaan.
for alkio in range(3, 31, 3):
    print(alkio)
