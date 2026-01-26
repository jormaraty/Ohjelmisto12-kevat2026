# otetaan käyttöön satunnaislukujen kirjasto
import random

# kysytään noppien lukumäärä
lkm = int( input("Kuinka monta noppaa? ") )
# annetaan silmälukujen summalle alkuarvoksi nolla
summa = 0

# heitetään haluttu lukumäärä noppia,
# muuttuja nopan_nro on ns. kierroslaskuri
for nopan_nro in range(lkm):
    # heitetään noppaa yhden kerran
    silmaluku = random.randint(1, 6)
    # xtra: tulostetaan saatu silmäluku
    print(f"noppa {nopan_nro + 1}, tulos = {silmaluku}")
    # lisätään saatu silmäluku muuttujan summa arvoon
    summa += silmaluku  # summa = summa + silmaluku
# tulostetaan noppien silmälukujen summa
print(f"Silmälukujen summa = {summa}")




