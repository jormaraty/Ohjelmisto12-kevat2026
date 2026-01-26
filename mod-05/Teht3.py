# Tutkitaan käyttäjän antamasta kokonaislluvusta, että onko se alkuluku vai ei?

# onko alkuluku vai ei, alkuoletus: kyllä
on_alkuluku = True

# kysytään käyttäjältä tutkittava kokonaisluku
tutkittava = int( input("Anna tutkittava kokonaisluku: "))

# jakaja, jolla tutkitaan käyttäjän luvun jaollisuutta.
jakaja = 2

# Idea: tutkitaan, että onko käyttäjän antama luku jaollinen
# jollakin jakajan arvolla 2, 3, 4, 5, ... (kayttajan luku - 1).
# Jos löytyy jakajan arvo, jolla käyttäjän luku on jaollinen,
# niin muutetaan muuttujan on_jaollinen arvo (on_jaollinen = False).

# Jos löytyi yksikin jakajan arvo, jolla käyttäjän luku on jaollinen,
# niin muuttujan 'on_alkuluku' on muuttunut arvoon False.
# Tämä tarkoittaa ettei käyttäjän luku ole alkuluku.

# Jos muuttujan 'on_alkuluku' on säilynyt arvossa True kaikilla jakajan
# eri arvoilla, niin se tarkoittaa ettei käyttäjän antama luku ole
# jaollinen millään muulla kuin ykkösellä ja itsellään.
# Toisin sanoen käyttäjän antama luku ON alkuluku.


