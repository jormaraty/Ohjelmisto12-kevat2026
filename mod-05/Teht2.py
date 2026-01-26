# Tehdään tyhjä lista, johon käyttäjän antamat luvut tallennetaan.

# Kysytään käyttäjältä lukuja, kunnes hän antaa tyhjän merkkijonon.
# Ahaa, käyttäjän syöte luettava merkkijonona, muuten ei havaita lopetusmerkkiä.
# Huom: Tallennetaan arvot listaan kuitenkin numerona.

# lajitellaan listan alkiot käänteiseen suuruusjärjestykseen
# (suurimmasta pienimpään).

# Tulostetaan järjestetystä listasta 5 ekaa alkiota.

numerot = [1, 4, 6, 8, 11, 15, 56]

# tulostetaan 5 ekaa arvoa listasta
for arvo in numerot[:5]:
    print(arvo)

