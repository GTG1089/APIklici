import requests

url = "https://restcountries.com/v3.1/all?fields=name"
url2="https://restcountries.com/v3.1/all?fields=name,borders,languages,population,continents,timezones"
odgovor = requests.get(url2)
drzave = odgovor.json()
#print(odgovor)
# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!
"""old=0
oldi=""
for i in drzave:
    if "borders" in i:
        ai=i["name"]
        a=len(i["borders"])
        old=a
        oldi=ai

        print(ai, a)
        if a>old: 
            old=a
            oldi=ai
        else:
            pass"""
old=0
oldi=""
for i in drzave:
    if "borders" in i:
        a = len(i["borders"])
        if a > old:
            old = a
            oldi = i["name"]

print("Država z največ mejami:", oldi, old)
        
# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"
old=0
oldi=""
for i in drzave:
    if "languages" in i:
        a = len(i["languages"])
        if a > old:
            old = a
            oldi = i["name"]

print("Države z največ jeziki:", oldi, old)
# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0

# 4: Poišči državo z največ časovnimi pasovi (timezones)
# Namig: Vsaka država ima vsaj en timezone

# 5: Izpiši vse države, ki imajo v imenu presledek
# Namig: Uporabi ["name"]["common"] za ime države

# 6: Izpiši število držav, ki imajo za uradni jezik angleščino

# 7: V katerem časovnem pasu (timezone) je največ držav?
# Namig: Ena država ima lahko več timezone-ov

# 8: Katera črka se največkrat pojavi kot prva črka v imenu države?
# Namig: Za ime uporabi ["name"]["common"].lower()

# 9: Katera država ima najdaljše ime?

# 10: Izračunaj še eno statistiko po želji.