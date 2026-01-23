"""
Ohjelma kysyy käyttäjältä kokonaislukuja, kunnes käyttäjä antaa tyhjän merkkijonon.
Tyhjä merkkijono tarkoittaa merkkijonoa (""), jonka pituus on 0 eli
käyttäjä painaa pelkästään Enter-nappulaa.
Lopuksi ohjelma tulostaa kuinka monta kokonaislukua käyttäjä antoi sekä
tulostaa suurimman annetuista luvuista.
Käytä ratkaisussa while-toistorakennetta.
"""

# Ahaa, lopetusmerkkinä on "" eli tyhjä merkkijono. Se ei ole numero ->
# käyttäjän syöte on luettava sisään merkkijonona.

# alkuarvo:
# käyttäjien antamien kokonaislukujen lukumäärä on aluksi nolla.
lkm = 0

# kysytään käyttäjältä kokonaisluku yhden kerran,
# ennen kuin mennään while-toistoon
syote = input("Anna kokonaisluku, Enter lopettaa: ")

# while-toistossa ollaan, kunnes käyttäjä antaa tyhjän merkkijonon (Enter),
# eli toistetaan niin kauan, kun saatu syöte EI ole "".
while syote != "":
    # lisätään saatujen kokonaislukujen lukumäärää yhdellä
    lkm += 1        # sama kuin: lkm = lkm + 1
    # muutetaan käyttäjän antama syöte kokonaisluvuksi
    kayttajan_luku = int(syote)
    # jos käsiteltävä luku on eka (lkm == 1), niin se on suurin saatu luku
    if (lkm == 1):
        suurin = kayttajan_luku
    # jos kayttajan_luku on isompi kuin tämän hetken muuttujan 'suurin' arvo,
    # niin muuttujan 'suurin' uudeksi arvoksi tulee käyttäjältä saatu arvo
    if kayttajan_luku > suurin:
        suurin = kayttajan_luku

    # HUOM: muista kysyä käyttäjältä uusi arvo (muuten ollaan ikuisessa silmukassa)
    syote = input("Anna kokonaisluku, Enter lopettaa: ")
    # tästä siirrytään automaattisesti testaamaan while-ehtoa

# while-toisto on loppunut, kun tänne tullaan (käyttäjä on painanut pelkän Enter.
# Tulostetaan saadut tulokset
print(f"Annoit {lkm} kokonaislukua")
# tulostetaan suurin arvo vain, jos käyttäjä antoi vähintään yhden luvun
if lkm >= 1:
    print(f"Suurin arvoistasi oli: {suurin}")
print("Hyvää päivän jatkoa!")