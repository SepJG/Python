import random

land = ["Norge", "Sverige", "Spania", "USA", "Finland", "Island", "Danmark", "Tyskland", "Frankrike"]

hovedsteder = ["Oslo", "Stockholm", "Madrid", "Washington, DC", "Helsinki", "Reykjavik", "København", "Berlin", "Paris"]

def skriv(land, hovedsteder):
    for i in range(len(land)):
        print(f"Hovedsteden in {land[i]} er {hovedsteder[i]}.")

def nytt_land(land, hovedsteder):
    tmpland = input("Land: ")
    tmpstad = input("Stad: ")
    land.append(tmpland)
    hovedsteder.append(tmpstad)
    return land, hovedsteder

def spm(land, hovedsteder):
    print(random.choice(enumerate(land)))

'''
    i = random.randint(0,len(land))
    svar = input(f"Hva er hovedstaden i {land[i]}")
    if svar == hovedsteder[i]:
        print("jippi")
    else:
        print("nah")
'''
#skriv(land, hovedsteder)
#land, hovedsteder = nytt_land(land, hovedsteder)
#skriv(land, hovedsteder)
spm(land, hovedsteder)