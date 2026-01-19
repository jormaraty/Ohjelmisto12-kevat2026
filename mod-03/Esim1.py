# kysytään käyttäjän ikä ja kysytään rahamäärää
ika = int(input("Anna ikäsi: "))
rahat = float(input("Paljonko on rahaa mukana: "))

# jos käyttäjä on täysi-ikäinen ja rahaa on
# vähintään 10€, niin pääsee bileisiin.
# Muuten toivotetaan hyvää kotimatkaa.
if ika >= 18  and rahat >= 10:
    print("Hyvää iltaa,")
    print("Tervetuloa bileisiin!!!")
else:
    print("Go home!")

print("Ohjelma loppuu")




