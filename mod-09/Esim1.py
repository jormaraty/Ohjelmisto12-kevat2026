"""
Koodaa Kissa-luokka.
Kissa luokalla on 2 ominaisuutta: nimi ja rotu.
Jos käyttäjä ei anna kissalle rodun nimeä, niin se arvoksi
"kotikissa".
Tee luokalle alustaja, jossa voidaan antaa luotavan olion
arvot.
Luo pääohjelmassa 2 kissaa: eka kissan rotuna on 'Ragdoll',
toiselle ei määritellä rotua. Keksi itse kissojen nimet.
Tulosta molempien kissojen kaikki ominaisuudet.
"""

class Kissa:

    def __init__(self, nimi, laji="kotikissa"):
        self.nimi = nimi
        # huom: parametrin nimi on eri luokan ominaisuus.
        self.rotu = laji

# pääohjelma alkaa

# luodaan kaksi kissa-tyyppistä oliota
kissa1 = Kissa("Miska", "Ragdoll")
kissa2 = Kissa("Minni")

# tulostetaan molempien kissojenkaikki arvot
print(f"Nimi: {kissa1.nimi} on {kissa1.rotu}")
print(f"{kissa2.nimi} on {kissa2.rotu}")

