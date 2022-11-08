# Sekvensielt søk i en sekvens
# Returnerer True hvis element er i sekvens, False ellers
def seq_search(sekvens, element):
    funnet = False              # Variabel som sier om verdien er funnet eller ikke
    for x in sekvens:
        if x == element:
            funnet = True
    return funnet

# Kan vi optimalisere koden over?

# Hva hvis vi ønsker å få indeks til elementet hvis det finnes?



A=[1,9,3,4,5,6,7,8,9,10]

print(seq_search(A, 3))
