# Funktio, joka tarvitsee alkuarvon eli parametrin toimiakseen.
# Huom: parametri 'tuumat' on myös funktion muuttuja.
# Huom: pääohjelma ei näe funktion muuttujia.
# Funktio ei palauta mitään arvoa kutsujalle.

def muunna(tuumat):
    kerroin = 2.54      # 1 tuuma = 2,54 cm

    print("\n--- Funktio tässä moi ---")
    print(f"Parametrini/muuttujani 'tuumat' arvo = {tuumat}")

    # lasketaan ja tulostetaan vastaus 2 desimaalin tarkkuudella
    tulos = kerroin * tuumat
    print(f"{tuumat} tuumaa = {tulos:.2f} cm.")

    # palataan takaisin kutsujalle (pääohjelmaan)
    return


# - pääohjelma -
print("- Pääohjelma tässä. Aloitetaan. -")

# muunnetaan käyttäjän vastaus desimaaliluvuksi (float)
syote = float( input("Kuinka paljon tuumia? ") )

# kutsutaan funktiota, annetaan kutsun yhteydessä pääohjelman muuttujan arvo.
# Huom: pääohjelman 'syote' kopioidaan muuttujan parametrin 'tuumat' arvoksi.
# Huom: pääohjelma ei näe funktion parametrin nimeä.
muunna(syote)

# funkktio on lopettanut toimintansa, kun tähän tullaan.
print("\n- Pääohjelma tässä taas, lopetellaan ohjelma. Moi! -")

