'''
    Luvun jaollisuuden tutkiminen.
    Se tehdään jakojäännöksen (%) avulla.

    Esim. 15 % 5 = 0, eli 15 on jaollinen 5:llä.
    15/5 = 3 tasan, yhtään ei 'jää yli'.

    19 % 5 = 4, eli 18 ei ole jaollinen 5:llä.
    5 mahtuu kolme kokonaista kertaa lukuun 19.
    3 * 5 = 15 -> luvusta 19 'jää 4 yli'.
'''

# kysytään käyttältä kokonaisluku,
# tarkistetaan, että onko se jaollinen 3:lla.
luku = int( input("Annan kokonaisluku: ") )

# lasketaan ja tulostetaan nyt jakojäännöksen arvo, '\n' on rivinvaihto
jakojaannos = luku % 3
print(f"jakojäännös, kun lukusi jaetaan kolmella on {jakojaannos}")

# luvun jaollisuus tai jaottomuus voidaan tutkia helposti  if-ehdon avulla
if luku % 3 == 0:
    print(f"lukusi {luku} ON jaollinen kolmella.")

if luku % 3 != 0:
    print(f"lukusi {luku} EI ole jaollinen kolmella.")

# -------------

arvo = int(input("\nYritäpä nyt antaa kokonaisluku, joka on parillinen ja yli 10: "))

# alla oleva lauseke olisi varmaan helpompi hahmottaa sulkujen avulla
# if (arvo > 10) and (arvo % 2 == 0):
# ilman sulkujakin pitäisi kyllä toimia..
if arvo > 10  and  arvo % 2 == 0:
    print("Sinä osasit, wau!")
else:
    print("Tunari!")
