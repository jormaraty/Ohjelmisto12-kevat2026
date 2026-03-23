"""
Tässä tiedostossa luodaan uusi Talo-luokan olio, edellisen tehtävän Hissi-luokan lisäksi.

Nyt Talo- ja Hissi-luokan välille syntyy pysyvä suhde.
Talo-luokan yhtenä ominaisuutena on lista, joka sisältää hissejä.

Nyt assosiaatio on yksisuuntainen, kuten yleensäkin on.
Talo tietää omat hissinsä, mutta hissi ei tiedä talosta jossa se sijaitsee.

Huomaa myös olio-ohjelmoinnin idea: talon ei tarvitse tietää mitään logiikasta,
jolla hissit toimivat. Talo vain hyödyntää hissien toimintoja eli metodeja.

Sopimus: käyttäjä tuntee hissit numeroilla 1, 2 ja 3.
Huomaa, että se poikkeaa listan 'hissit' indekseistä, jossa hissit ovat.
"""

class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        # asetetaan luotavan Hissi-tyyppisen olion alin ja ylin kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        # Huom: uusi hissi on aluksi aina alimmassa kerroksessa
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, tavoite_kerros):
        # metodi siirtää hissin haluttuun kerrokseen.

        # täytyykö siirtyä alaspäin vai ylöspäin?
        if self.nykyinen_kerros < tavoite_kerros:
            # siirrytään ylöspäin yksi kerros kerrallaan
            while self.nykyinen_kerros < tavoite_kerros:
                # kutsutaan olion toista metodia, joka nostaa hissin kerroksen ylöspäin
                self.kerros_ylös()
            # xtra: ilmoitetaan, että ollaan perillä
            print(f"- Olemme halutussa {tavoite_kerros}. kerroksessa -")

        elif self.nykyinen_kerros > tavoite_kerros:
            # alaspäin täytyy mennä
            while self.nykyinen_kerros > tavoite_kerros:
                self.kerros_alas()
            # xtra: ilmoitetaan, että ollaan perillä
            print(f"- Olemme halutussa {tavoite_kerros}. kerroksessa -")
        else:
            # Olemme tällä hetkellä halutussa kerroksessa
            print(f"-- Olemme jo valmiiksi halutussa {tavoite_kerros}. kerroksessa. -")

        return      # metodin loppu

    def kerros_ylös(self):
        # siirrytään 1 kerros ylöspäin ja ilmoitetaan uuden kerroksen tieto
        self.nykyinen_kerros += 1
        print(f"olemme nyt {self.nykyinen_kerros}. kerroksessa")
        return

    def kerros_alas(self):
        # siirrytään 1 kerros alaspäin ja ilmoitetaan uuden kerroksen tieto
        self.nykyinen_kerros -= 1
        print(f"olemme nyt {self.nykyinen_kerros}. kerroksessa")
        return


class Talo:
    # luokan alustaja saa tiedon talon hissien lukumäärästä ja
    # minkä kerroksien välillä ne kulkevat
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        # luodaan tyhjä lista talon hissejä varten
        self.hissit = []
        # luodaan talon hissit
        self.luo_hissit(hissien_lkm)

    def luo_hissit(self, lkm):
        # luodaan tarvittava määrä hissejä ja sijoitetaan listaan 'hissit',
        # joka on Talo-luokan ominaisuus.
        for i in range(lkm):
            uusi_hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(uusi_hissi)
        return      # metodin loppu

    def aja_hissiä(self, hissin_nro, kohdekerros):
        liikkuva_hissi = self.hissit[hissin_nro - 1]
        liikkuva_hissi.siirry_kerrokseen(kohdekerros)
        return

    def tulosta_tiedot(self):
        # xtra: metodi tulostaa kaikkien hissien kerrokset
        print("\nHissien sijainnit:")
        for i in range(len(self.hissit)):
            print(f"Hissi {i+1}: kerroksessa {self.hissit[i].nykyinen_kerros}")


# -- pääohjelma alkaa --

# luodaan talo, jolla on 3 hissiä. Ne kulkevat kerroksissa 1-10.
testitalo = Talo(1, 10, 3)

testitalo.aja_hissiä(1, 3)
testitalo.aja_hissiä(3, 10)

testitalo.tulosta_tiedot()





