# kysytään käyttäjän hyttiluokka
vastaus = input("Mikä on hyttiluokkasi? ")

# xtra: muutetaan käyttäjän syötteen kaikki merkit isoiksi,
# sijoitetaan muokattu merkkijono uuteen muuttujaan
hyttiluokka = vastaus.upper()

# tulostetaan selitysteksti hyttiluokan mukaan
if hyttiluokka == "LUX":
    print("parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella.")
# TODO: tee puuttuvat hyttiluokkien tulostukset
else:
    print("Virheellinen hyttiluokka")
