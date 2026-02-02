import random

def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return (eka, toka)

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

vastaus_monikko = heitä()
print(f"Nopista tuli {vastaus_monikko[0]} ja {vastaus_monikko[1]}")