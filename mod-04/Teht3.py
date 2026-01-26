import math

pienin = math.inf       # ääretön
suurin = -math.inf

syote = input("Anna luku: ")

while syote != "":
    luku = int(syote)

    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    syote = input("Anna luku: ")

## onko käyttäjä antanut ainakin yhden numeron?
if pienin != math.inf:
    print(f"Pienin: {pienin}")
    print(f"Suurin: {suurin}")
else:
    print("Et antanut yhtään lukua")