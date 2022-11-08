#Vi har en 2D-liste som ser slik ut:
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]#og vi ønsker å printe den slik: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Hvilke av følgende snutter vil gjøre det?

# Riktig
B = []
for foo in A:
    for bar in foo:
        B.append(bar)
print(B)

# Feil fordi range forventer tall som input, men får lister
# B = []
# for foo in range(A):
#     for bar in range(A[0]):
#         B.append(bar)
# print(B)

# Feil
# Den ytre løkka vil kjøre 3 ganger med foo = 0, 1 og 2.
# Den indre løkka vil kjøre et antall ganger ut ifra hva foo er, så først 0, så 1 (med bar = 0) og så 2 (med bar = 0 og 1).
# Verdien den appender vil også være feil. Den endelige listen vil være [0, 0, 1]
# B = []
# for foo in range(len(A)):
#     for bar in range(foo):
#         B.append(bar)
# print(B)

# # Riktig
B = []
for foo in range(len(A)):
    for bar in range(len(A[0])):
        B.append(A[foo][bar])
print(B)
