import random 

tall = random.randint(1,100)   # tilfedlig tall mellom 1 til 100 (inklusive)

gjett = -1     # for å sikre oss at vi får True første gang i while-løkka
while tall != gjett:          #saa lenge man gjetter feil
    gjett = int(input("Gjett tall mellom 1 og 100: "))
    if gjett > tall:
        print("Psst: Litt for stort!")
    elif gjett < tall:
        print("Psst: Litt for smaatt!")

print("RIKTIG!!!! Hvordan klarte du det????")
