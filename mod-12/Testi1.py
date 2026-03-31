import requests
import json

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls

# muodostetaan nettiin lähetettävä pyyntö
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
print("Nettiin lähtevä pyyntö: " + pyyntö)

try:
    # lähetetään nettiin GET-pyyntö, saadaan takaisin json muotoinen data
    vastaus = requests.get(pyyntö).json()
    print(vastaus)

    # vastauksen muotoilua
    # print(json.dumps(vastaus, indent=2))

    # tulostetaan löytyneiden sarjojen nimet
    for a in vastaus:
        print(a["show"]["name"])

except requests.exceptions.RequestException as e:
    # käsitellään nettihaussa syntyneet poikkeukset
    print ("Hakua ei voitu suorittaa.")
except Exception as ex:
    # käsitellään kaikki muut poikkeukset
    print("Tapahtui odottamaton virhe:")
    print(ex)       # virheen selitys






