import random

def heitä():
    # arvotaan 2 satunnaista kokonaislukua (int)
    eka, toka = random.randint(1,6), random.randint(1,6)

    # palautetaan 1 kpl monikkoja, joka sisältää 2 arvoa
    return (eka, toka)

# Tapa 1: otetaan funktion palauttama monikko (tuple) talteen monikkona
vastaus_monikko = heitä()
# puretaan monikon sisältämät 2 arvoa.
print(f"Nopista tuli {vastaus_monikko[0]} ja {vastaus_monikko[1]}")

# Tapa 2: sijoitetaan funktion palauttaman monikon 2 arvoa suoraan 2 eri muuttujaan.
noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

