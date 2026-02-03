"""
Lista parametrina: tämä on eri asia kuin jos parametrina on esim. int.

Perustietotyypit (int, float, string, boolean):
- pääohjelman muuttujan arvo kopioidaan funktion parametrin arvoksi.

Lista:
- pääohjelma saa viittauksen (osoitteen) omaan listaansa
- jos funktio saa parametrina listan:
   - listaa ei kopioida
   - funktio saa viittaukseen SAMAAN listaan kuin pääohjelma.
Tästä seuraa:
   - kaikki funktion tekemät muutokset listaan näkyvät myös pääohjelmalle,
     siis vaikka funktio ei palauttaisi mitään.
"""

# Funktio saa parametrina listan kokonaislukuja,
# funktio lajittelee listan alkiot ja lisäksi tuplaa niiden arvon.
def tuplaus(lista):
    print("\n-- Funktio tässä moi, käsittelen hieman listaani nimeltä 'lista'.")
    # lajitellaan listan alkiot nousevaan suuruusjärjestykseen
    lista.sort()
    # tuplataan listan jokaisen alkion arvo, len palauttaa listan pituuden.
    # esim. jos listan pituus on 5 -> i saa arvot 0, 1, 2, 3, ja 4.
    for i in range (len(lista)):
        lista[i] *= 2     # lista[i] = 2 * lista[i]

    return


print("- Pääohjelma tässä, aloitellaan -")

kokonaisluvut = [8, 3, 22, 15, 17]

print("\nListani 'kokonaisluvut' arvot ovat:")
print(kokonaisluvut)

print("Kutsun funktiota tuplaus")
tuplaus(kokonaisluvut)

print("\nPääohjelmassa jälleen. Listani 'kokonaisluvut' arvot ovat:")
print(kokonaisluvut)