"""
    Tässä tunnilla ollut asia siistimpänä versiona.
    Käytetään Python-kielen valmista geopy-kirjastoa ->
    projektiin on asennettava geopy-kirjasto (ks. tehtävän anto).

    Eihän ope osaa ratkaista tätäkään tehtävää, kuten tehtävässä haluttiin.
    Tämä ohjelma kysyy vain yhden lentokentän ICAO-koodin ja laskee sen etäisyyden Helsinki-Vantaan
    lentoasemasta kilometreinä.

    geopy.distance.distance käyttää oletuksena tarkkaa WGS-84 maan
    mallinnusta (geodesic). Myös GPS käyttää samaa.
    Koordinaatit annetaan asteina muodossa (latitude, longitude)
    Esim. Helsinki-Vantaan lentoaseman (lat,lon) = (60.3172, 24.963301)

"""

from geopy import distance      # etäisyyden laskentaan
import mysql.connector          # tietokantayhteys

# Funktio laskee kahden paikan välisen etäisyyden.
# Paikan gps-koordinaatit annetaan tuplena muodossa (lat, lon).
def laske_etaisyys(gps1, gps2):
    vastaus = distance.distance(gps1, gps2).km
    return vastaus

# Funktio palauttaa lentoaseman sijainnin tuplena (lat,lon).
# Parametrina annetaan lentoaseman icao-koodi.
def lentoaseman_sijainti(icao_koodi):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_koodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    # fetcone palauttaa korkeintaan 1 kpl tuloksia, se tulee tuple-tietorakenteena.
    tulos = kursori.fetchone()
    vastaus = (tulos[0], tulos[1])
    return vastaus

# pääohjelma
# luodaan aluksi yhteys tietokantaan, huom: muuta käyttäjätunnukset oikeiksi.
yhteys = mysql.connector.connect(
    host='127.0.0.1',           # tai 'localhost'. Viittaa sinun omaan koneeseen.
    port= 3306,
    database='flight_game',     # tähän sinun tietokannan nimi
    user='root',                # vaihda tähän sinun oma käyttäjätunnus
    password='root',            # käyttäjän oikea salasana
    autocommit=True
    )

print("Ohjelma laskee lentokenttäsi etäisyyden Helsinki_Vantaasta.")
gps1 = (60.3172, 24.963301)         # Helsinki-Vantaan gps-koordinaatit asteina.

icao_koodi = input("Anna lentokenttäsi ICAO-koodi: ")
# funktio palauttaa lentoaseman gps-koordinaatit tuplena (lat, lon)
gps2 = lentoaseman_sijainti(icao_koodi)
print(f"debug: lentoasemasi gps-koordinaatit: {gps2}")

# funktio palauttaa 2 lentokentän välisen etäisyyden kilomatreina
etaisyys = laske_etaisyys(gps1, gps2)
# tulostetaan lentokenttien välinen etäisyys kokonaisina kilometreinä (desimaaleja 0 kpl)
print(f"Lentokenttäsi etäisyys Helsinki-Vantaasta on {etaisyys:.0f} km. ")


