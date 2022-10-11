'''
Uke 41: under
I dag:
- slutt lister
- 2d-lister
- strengoperasjoner som likner på lister

'''


# # Man kan endre på listen selv med slicing:
# liste = [0,1,2,3,4,5]

# liste[0:3] = ['slett'] # Skriver over tre element med ett!
# print(liste)
# liste[3:] = [] # Skriver over _etter_ tredje element med en tom liste
# print(liste)
# 
# liste.insert(2,333) # Sett inn noe på en spesifikk plass
# print(liste)
# 
# 
# # in
liste = [0,12,2,3,122,12]
# if 2 in liste: # motsatt: legg inn not foran True
#     print(True)
#     
# # funksjoner som index, sort, reverse, remove
# print(liste.index(3)) # Hvilket nummer er første treff på 3

# Erstatte første treff på en verdi med noe annet
# print(liste)
# print(liste.index(12, liste.index(12)))
# liste.insert(liste.index(2), 144)
# print(liste)

# man kan søke i delstrenger med
# index(hva, start, slutt)
# print(liste.index(12, liste.index(12)+1,len(liste)))

# En mengde ulike funksjoner som kan brukes på lister

# liste.sort() # Den sorterer seg selv

# print(liste)
# liste.reverse() # Den sorterer seg selv
# ("hei".reverse() finnes ikke - hvorfor?)

# print(liste) # Motsatt rekkefølge av slik den var
# Merk at dette ikke er likt liste[::-1]!

# liste.remove(122)
# print(liste)
# 
# del(liste[1])
# print(liste)
# print(min(liste))
# print(max(liste))
# 
# # kopiering av lister - en lager bare en peker!
liste1 = [0,1,2,3]
liste2 = liste1
liste1[3] = 'heisann!'
print(liste2)
# # For å lage en kopi må du kopiere hvert element i listen
# liste2 = [] + liste1
# 
# # eller
# liste2 = []
# for elem in liste1:
#     liste2.append(elem)
# print(liste2)
