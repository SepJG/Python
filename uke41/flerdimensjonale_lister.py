import time # Til lenger ned
# Flerdimensjonale lister

# Først - skrive ut hver bokstav og dens unicodeverdi
# for char in 'abcdefghijk':
#     print(char, ord(char))
    


# Sånn mens vi snakker om unicode...
# for i in range(129293,129500):
#     print(i, chr(i))
#     time.sleep(0.1)



# La oss lage en liste av 
# liste = []
# for char in 'abcdefghijk':
#     print([char, ord(char)])
    # Men hva hvis vi lager en liste som inneholder disse?
#     liste.append([char, ord(char)])
# print(liste)
# 
# for i in range(len(liste)):
#     for j in range(len(liste[i]))
# # Hvordan endre ett av feltene?
# print(liste[1][1])
# liste[1][1] = 55
# print(liste[1][1])

# Hvordan går vi igjennom en todimensjonal liste?

# Vi kan gå igjennom indekser

# Vi kan gå igjennom med 'in' og hente ut begge elementene med en gang!


# Vi kan lage lister veldig raskt ved å bruke 'list comprehension'
#liste = [[x, ord(x)] for x in "abcdefghijk"]
# print(liste)
# Kan vi lage den todimensjonale lista over på samme måte?
# liste = [[char, ord(char)] for char in "abcdefghijk"]
# print(liste)


# Lage gangetabellen!
gange = [[rad*kol for kol in range(1,12)] for rad in range(1,11)]

# Dette tilsvarer
# gange = []
# for rad in range(1,11):
#     tmp = []
#     for kol in range(1,12):
#         tmp.append(rad*kol)
#     gange.append(tmp)
# 

for i in range(len(gange)):
    for j in range(len(gange[i])):
        print(gange[i][j],end="\t")
    print()

# for talliste in gange:
#     for tall in talliste:
#         print(tall,end="\t")
#     print()
