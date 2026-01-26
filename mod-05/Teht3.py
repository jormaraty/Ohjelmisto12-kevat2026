# Tutkitaan käyttäjän antamasta kokonaislluvusta, että onko se alkuluku vai ei?

# onko alkuluku vai ei, alkuoletus: kyllä
on_alkuluku = True

# kysytään käyttäjältä tutkittava kokonaisluku
tutkittava = int( input("Anna tutkittava kokonaisluku: "))

# jakaja, jolla tutkitaan käyttäjän luvun jaollisuutta.
jakaja = 2

# Idea: jos käyttäjän luku on jaollinen 2:lla.
# Seuraavaksi jaan 3:lla, 4, 5, ... (kayttajan luku - 1)
# Jos löytyy yksikin jakajan arvo, jolla käyttäjän luku on jaollinen,
# niin käyttäjän luku EI ole alkuluku. Merkitään on_alkuluku = False.
# Huom: toistorakenteen voi lopettaa heti, jos jakolasku menee tasan.

