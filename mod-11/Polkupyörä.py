"""
Tässä on esimerkki olio-ohjelmoinnin periytymisestä.

Polkupyörä-luokalla on ominaisuudet polkupyörän merkki ja vaihteiden lukumäärä.
Tee luokalle alustaja, jossa voit asettaa nämä arvot.
Tee luokalle myös metodi tulosta(), joka tulostaa polkupyörän kaikki tiedot.

Tee myös luokka Sähköpyörä, joka periytyy Polkypyörä-luokasta.
Sähköpolkupyörä-luokalla on lisäksi ominaisuudet omistaja sekä toimintasäde sähköllä.
Hyödynnä aliluokassa (Sähköpolkupyörä) sen yliluokan (Polkupyörä) valmiita koodeja.

Tee pääohjelma, jossa luot polkypyörän ja tulostat sen kaikki ominaisuudet.
Tee lisäksi sähköpolupyörä ja tulosta sen kaikki ominaisuudet.
"""

class Polkupyörä:
    def __init__(self, merkki, vaihteiden_lkm):
        self.merkki = merkki
        self.vaihteiden_lkm = vaihteiden_lkm

    def tulosta(self):
        print("Polkypyörän tiedot:")
        print(f"Polkupyörän merkki: {self.merkki} ")
        print(f"Vaihteiden lukumäärä: {self.vaihteiden_lkm} ")
        return


class Sähköpyörä(Polkupyörä):
    def __init__(self, merkki, vaihteiden_lkm, omistaja, toimintasäde):
        # kutsutaan yliluokan (Polkupyörä) alustajaa
        super().__init__(merkki, vaihteiden_lkm)
        # lisätään omat (Sähköpolkupyörä) uudet ominaisuudet
        self.omistaja = omistaja
        self.toimintasäde = toimintasäde

    def tulosta(self):
        # 'ylikirjoitetaan' yliluokan metodi
        # hyödynnetään aluksi yliluokan valmista toimintoa
        super().tulosta()
        # tulostetaan lisäksi puuttuvat tiedot
        print(f"omistaja: {self.omistaja}" )
        print(f"toimintasäde: {self.toimintasäde}" )


# -- pääohjelma alkaa --
eka_pyörä = Polkupyörä("Helkama", "3")
eka_pyörä.tulosta()

toka_pyörä = Sähköpyörä("Tunturi", 4, "Mie", 40)
toka_pyörä.tulosta()



