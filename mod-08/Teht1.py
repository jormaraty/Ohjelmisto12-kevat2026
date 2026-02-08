'''
    Tässä on vähän alkua tehtävään 1, ei hae kaikkia tietoja.
    Testattu 5.2.2026, että toimii PyCharm  seuraavalla konfiguraatiolla:
    - python interpreter: 3.14
    - mysql-connector-python: 9.5.0
'''

'''
Suositellaan että mikään sovellus ei käytä tietokannan 
pääkäyttäjän (root) tunnuksia.
Tosi vaarallista, jos pääkäyttäjän tunnukset leviävät ilkeille tahoille.
Tätä varten tietokantaan on luotu käyttäjätunnus 'peruskäyttäjä', 
jolla on oikeudet käyttää vain komentoja select, insert ja update.
Ohjeet tähän löytyvät Sql-materiaalin luku 1 / "PDF Työvälineet työtavat".
'''

# Alla oleva import tarvitaan aina, kun käytetään tietokantaa.
# Vaatii paketin lisäämisen projektiisi. Ks. ohjeet teoriasta (.
import mysql.connector

def hae_kentan_tiedot(icao):
    sql = f"SELECT name FROM airport where ident='{icao}'"
    print(sql)
    # kursorin avulla kommunikoidaan tietokannan kanssa
    kursori = yhteys.cursor()
    # suoritetaan sql-lause kursorin avulla
    kursori.execute(sql)
    # haetaan kursorilta kaikki tulosrivit
    tulos = kursori.fetchall()
    # saatiinko tulosrivejä?
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on: {rivi[0]}")
    else:
        print("ICAO-koodillasi ei löytynyt lentoasemaa.")
    return


# pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',           # tai 'localhost'. Viittaa sinun omaan koneeseen.
    port= 3306,
    database='flight_game',     # tähän sinun tietokannan nimi
    user='perususer',           # vaihda tähän sinun oma käyttäjätunnus
    password='salainen',        # käyttäjän oikea salasana
    autocommit=True
    )

icao_koodi = input("Anna kentän ICAO-koodi: ")
hae_kentan_tiedot(icao_koodi)