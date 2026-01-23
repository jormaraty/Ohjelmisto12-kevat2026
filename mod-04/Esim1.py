"""
Arvauspeli: kumpi arvaa ensin 3 kertaa oikein, pelaaja vai kone.
Pelaaja arvaa kruunu tai klaava. Kone saa aina jäljelle olevan vaihtoehdon
"""

# Otetaan käyttöön Pythonin satunnaislukujen kirjasto (random)
import random

# aluksi pelaajalla ja konella on oikeita vastauksia 0 kpl.
pelaaja = 0
kone = 0

print(f"Pääset pelaamaan konetta vastaan: kruunu vai klaava?")
print("Se joka saa ensin 3 oikein, voittaa.")

# pysytään while-toistossa, jos kummallakin on alle 3 oikein
while pelaaja < 3  and kone < 3:
    arvaus = int( input("Arvaa: 1=kruunu, 2=klaava: ") )
    # hyväksytään vain vastaus 1 tai 2
    while arvaus < 1  or  arvaus > 2:
        print("Arvaa 1 tai 2")
        arvaus = int(input("Arvaa: 1=kruunu, 2=klaava:"))

    # kone arpoo desimaaliluvun väliltä 0,000... -> 0,999...
    arvottu = random.random()

    # Päätetään että satunnaisluku alle 0,5 on kruunu, muuten klaava.
    # Tarkistetaan, että arvasiko pelaaja oikein vai ei, ja
    # päivitetään oikeiden vastausten lkm.
    if arvottu < 0.5:       # kruunu on oikein
        if arvaus == 1:
            # pelaaja arvasi oikein, lisätään pelaajan pisteitä yhdellä
            pelaaja += 1    # tai pelaaja = pelaaja + 1
        else:
            # pelaaja arvasi väärin, kone saa pisteen lisää
            kone += 1
    else:                   # klaava on oikein
        if arvaus == 2:
            # pelaaja arvasi oikein, lisätään pelaajan pisteitä yhdellä
            pelaaja += 1  # tai pelaaja = pelaaja + 1
        else:
            # pelaaja arvasi väärin, kone saa pisteen lisää
            kone += 1

    # tulostetaan tilanne
    print(f"Sinä - kone {pelaaja} - {kone}")

    # täältä siirrytään aina while-ehdon tarkistukseen


# tulostetaan lopputilanne
if pelaaja >= 3:         # pelaaja sai ensin 3 oikein
    print("Onneksi olkoon, VOITIT !!!")
else:
    print("Parempaa onnea ensi kerralla!")




