import random
'''

Funksjonen beskriv_set tar inn to LISTER a og b
Den skal gjøre om listene til set, og så
skrive ut ulike ting:
- alle unike verdier som er i begge listene til sammen
- alle verdier som KUN er i begge listene
- alle verdier som er i begge listene, men ikke i begge
- elementene som er i a, men ikke i b

'''

def beskriv_sett(a, b):
    
    # Gjøre om til sett

    print(f'Unike element i hele a og b tilsammen: {set_a.union(set_b)}')
    print(f'Unike element som er i både a og b: {set_a.intersection(set_b)}}')
    print(f'Unike element i som ikke er i begge lister: {set_a.symmetric_difference(set_b)}')
    print(f'Elementer i a som ikke også er i b: {set_a.difference(set_b)}')
    
a = [random.randrange(10) for i in range (0, 10)]
b = [random.randrange(10) for i in range (5, 15)]
print(f"a: {a}\nb: {b}")

beskriv_sett(a,b)

def foo():
    print(1)
    
print(12)


