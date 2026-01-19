# Käytän lopussa myös Pythonin matematiikka-kirjastoa.
# Se otetaan koodiin import-lauseella.
# import-lauseet ovat ennen muuta koodia.

import math

# luetaan käyttäjältä kokonaislukuja 2 eri tavalla
ekaluku_str = input("Anna eka kokonaisluku: ")    # input palauttaa aina string
ekaluku = int(ekaluku_str)          # muutettiin merkkijono kokonaisluvuksi

# tehdään tyypinmuunnos kokonaisluvuksi heti lukemisen yhteydessä
tokaluku = int( input("Anna toinen kokonaisluku: ") )
kolmasluku = int(input("Anna vielä kolmas kokonaisluku: "))

summa = ekaluku + tokaluku + kolmasluku
ka = summa / 3          # keskiarvo

# normaali print vaatii, että numerot täytyy muuttaa tekstiksi,
# jos tulostuksessa on myös tekstiä.
# '\n' aiheuttaa ylimääräisen rivinvaihdon
print("\nAntamasi lukujen summa on: " + str(summa) + ", eiks vaan!")

# muotoiltu tulostus: huomaa f ennen lainausmerkkiä print(f"..."),
# muuttujan nimi laitetaan aaltosulkujen {...} sisään
print(f"lukujeni summa on {summa}, eikös vain?")

print(f"Lukujesi keskiarvo {ka}")

# muotoiltu tulostus: muuttujan arvoa voidaan myös muotoilla
# {muuttujan_nimi:muotoilukomennot}     # huomaa ':'
print(f"keskiarvo 3 desimaalilla {ka:.3f}")

print(f"\npiin arvo Pythonin mukaan: {math.pi}, aika monta desimaalia")
print(f"piin arvo 4 desimaalilla {math.pi:.4f}")