# Ehdotus: Jaetaan koodi eri funktioihin.

def lisaa():
    # funktio lisää uuden lentokentän sanakirjaan
    print("Toiminto ei ihan vielä valmis...")

def hae():
    # funktio pyytää käyttäjältä icao-koodin, hakee sen avulla lentokentän tiedot.
    pass        # komento ei tee mitään, mutta jokin suorituslause vaaditaan..

def tulosta_valikko():
    # funktio tulostaa käyttäjälle eri vaihtoehdot
    print("\nValitse toiminto:")
    print("1 = Lisää uusi lentoasema")
    print("9 = Lopeta")


# -- pääohjelma --

# luodaan sankirja lentokentän tietoja varten
lentoasemat = {
    "EFHK" : "Helsinki-Vantaa"
}

toiminto = 0    # käyttäjän valitsema toiminnon nro

while toiminto != 9:
    tulosta_valikko()
    toiminto = int(input("Valitse toiminto: "))

    if toiminto == 1:
        # lisätään uusi lentoasema
        lisaa()
    # tässä välissä on muut toiminnot (elif -haarat)
    else:
        print("Tuntematon toiminto")

print("Lopetit ohjelman, hyvää päivänjatkoa!")
