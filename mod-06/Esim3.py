"""
Funktio saa alkuarvon eli parametrin.
Funktio myös palauttaa arvon kutsujalle.
Funktio ei tulosta mitään.
"""

def muunna(tuumat):
    kerroin = 2.54

    # lasketaan tulos
    tulos = kerroin * tuumat

    # palautetaan saatu tulos kutsujalle, se tehdään return lauseen avulla.
    return tulos


# - pääohjelma -

# kysytään käyttäjltä tarvittava tieto
syote = float( input("Kuinka paljon tuumia? ") )

# kutsutaan funktiota, annetaan kutsun yhteydessä sen tarvitsema alkuarvo eli parametri.
# HUOM: nyt funktio palauttaa arvon.
# * Muista ottaa se talteen! *
# Nyt funktiolta saatu vastaus sijoitetaan muuttujaan 'vastaus'.

vastaus = muunna(syote)

# tulostetaan funktiolta saaatu vastaus
print(f"Funktio vastaili jotta {syote} tuumaa on {vastaus} cm.")