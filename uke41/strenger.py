# En streng består av tegn, som kan hentes
# ut som elementer i en liste:

streng = "Kapang"
print("Første tegn:", streng[0])

# Den kan også slices akkurat som lister:
print("Tre første tegn, baklengs:",streng[2::-1])

# Vi kan gå gjennom tegnene i for-løkker:
for tegn in streng:
    print(tegn)

# Vi kan bruke løkke med indeks:
for i in range(len(streng)):
    print(streng[i])

# Vi kan samkjøre det med list comprehension:
print([c for c in streng])

