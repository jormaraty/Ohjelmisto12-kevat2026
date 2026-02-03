import random   # kirjasto satunnaislukuja varten

# Funktio, joka ei tarvitse alkuarvoja eli parametreja toimiakseen.
# Funktio ei myöskään palauta mitään arvoa kutsujalle (pääohjelmalle).
# Huom: funktion nimeen kuuluu aina sulut (), vaikka ne olisivat tyhjät.
def heita():
    print("\n--- funktio aloittaa toiminnan ---")
    # arvotaan nopan silmäluku ja tulostetaan se
    arvottu = random.randint(1, 6)
    print(f"Arvoin nopan silmäluvuksi {arvottu}")

    # funktio lopettaa toiminnan ja toiminta siirtyy takaisin pääohjelmaan
    return

# -- pääohjelma --
# Ohjelman toiminta alkaa tästä
print("- Pääohjelma tässä, aloitan ohjelman toiminnan -")

print("Kutsun funktiota ja jään odottomaan, että se lopettaa toimintansa")
heita()         # funktion nimeen kuuluu sulut ()

# funktio on lopettanut toimintansa, kun tullaan tänne
print("\n-Pääohjelma tässä. Funktio lopetti äsken toimintansa. -")
print("Niin lopetan minäkin eli koko ohjelma loppuu. Moikka!")