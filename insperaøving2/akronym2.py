# Lag en funksjon akronym(s) som tar inn en setning og returnerer akronymet (det vil si en streng med første bokstaven i hvert ord). 
# Alle bokstavene i akronymet skal ha stor bokstav. 
# Du kan bruke funksjonen førsteBokstaver(s) fra forrige oppgave (selv om du ikke har gjort den).
# Eksempel:

# >>> setning = "Universal serial bus"
# >>> akronym(setning)
# "USB"

def førsteBokstaver(s):
    letters = []
    for word in s.split(" "):
        letters.append(word[0])
    return letters

def akronym(s):
    return "".join(førsteBokstaver(s)).upper()
print(akronym("olympic games"))