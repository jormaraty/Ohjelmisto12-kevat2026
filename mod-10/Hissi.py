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


# -- pääohjelma alkaa --
# luodaan uusi hissi, joka liikkkuu kerrosten 1 ja 7 välillä
eka_hissi = Hissi(1, 7)

# siirrytään kerrokseen 5
eka_hissi.siirry_kerrokseen(5)

#xtra: hallutaan siirtyä kerrokseen 5, jossa jo olemme
eka_hissi.siirry_kerrokseen(5)

# palataan takaisin lähtökerrokseen
eka_hissi.siirry_kerrokseen(1)



