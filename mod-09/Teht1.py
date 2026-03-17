"""
Tässä on ratkaisu tehtävään 1.
Ethän kopioi suoraan, vaan katso tarvittaessa vinkkejä.
"""

class Auto:

    # luokan konstruktori eli alustaja.
    # Oliota luodessa voidaan antaa arvot vain rekkarille ja huippunopeudelle.
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # uuden auton tämän hetkinen nopeus ja kuljattu matka asetetaan aina nollaksi.
        self.nopeus = 0     # tämän hetken nopeus
        self.matka = 0      # matkamittarin lukema (km)


# - pääohjelma alkaa -

# luodaan uusi Auto-tyyppinen olio, jonka nimeksi tulee 'auto1'
auto1 = Auto("ABC-123", 142)

# tulostetaan luodun auton kaikki ominaisuudet ja niiden arvot
print("Auton kaikki tiedot:")
print(f"rekisteritunnus: {auto1.rekisteritunnus}")
print(f"huippunopeus: {auto1.huippunopeus} km/h")
print(f"nykyinen nopeus: {auto1.nopeus} km/h")
print(f"matkamittarin lukema: {auto1.matka} km")