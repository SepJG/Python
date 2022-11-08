# Lag en funksjon førsteBokstaver(s) som tar inn en streng og returnerer en liste med første tegn i hvert ord
# Eksempel:

# >>> setning = "Universal serial bus"
# >>> førsteBokstaver(setning)
# ["U", "s", "b"]

def førsteBokstaver(s):
    letters = []
    for word in s.split(" "):
        letters.append(word[0])
    return letters
print(førsteBokstaver("Olympic Games"))