# # Sekvenser, blant annet lister og tupler
# # Tupler kan en ikke endre verdien på, lister kan en endre på

# liste = [1,2,3,4]
# print("liste = [1,2,3,4]: ",liste)

# for i in range(5):
#     print(i)
# 
# liste = list(range(5))
# print("list(range(5)):",liste)
# 
# liste = [1,2,'eik',True]
# print("liste = [1,2,'eik',True]:",liste)
# 
# liste = [0]*10
# print(liste)
# 
# liste = [0,1,'hei']*10
# print("liste = [0]*10: ",liste)
# 
# liste = [None] * 5
# print("liste = [None] * 5: ",liste)
# 

# liste[3] = 3
# print("liste[3] = 3: ",liste)
# 
# liste = [1]
# print("liste = [1], så print(liste*5): ",liste*5)
#

# Hva med tupler? Hva, hvem, hvorfor?
# Kan du vise zip?


# # Extend og append
# liste = [0,1,2,3]
# liste.extend([4,5,6])
# print(liste)
# 
# liste.append('sisten!') # Men kan bare legge til ett element
# print(liste)


# liste = list(range(5))
# for i in liste:
#     print(i)
# 
# # Indeksering> fra 0 til len(liste)-1
# liste = list(range(5))
# for i in liste:
#     print("Liste["+str(i)+"] = "+str(liste[i]))
# 
# # prøv print av indeksverdi utenfor lengden
# liste = [0,1,2]
# #print(liste[3])
# 
# # len
# liste = [0,1,2]
# print("Lengden av liste er",len(liste))
# 
# # Lister er muterbare - kan endre verdi av elementer
# liste = [0,1,2]
# print(liste)
# liste[0] = 'nyverdi'
# print(liste)
# 
# # Konkatinering - sammensetting av lister
# liste1 = [0,1,2]
# liste2 = [3,4,5]
# liste3 = liste1 + liste2 # Ny liste er to andre satt sammen
# print(liste3)
# liste2 += liste1 # gammel liste får lagt til nye element
# print(liste2)
# liste2 += ['slutt!'] # Alle typer element
# liste2 += [True] # Alle typer element
# print(liste2)
# 
# # Slicing: liste[start:slutt:inkrement] # Som range!
# liste = [0,1,2,3,4,5]
# print(liste[0:2]) # De to første verdiene, i en liste
# print(liste[3:-1]) # Liste med verdier fra element 4 og ut til og uten siste
# print(liste[:-1:2]) # Liste med annenhver verdi til og uten siste
# 
# # Man kan endre på listen selv med slicing:
# liste = [0,1,2,3,4,5]
# liste[0:3] = ['slett'] # Skriver over tre element med ett!
# print(liste)
# liste[3:] = [] # Skriver over _etter_ tredje element med en tom liste
# print(liste)
# 
# 
# # in
# liste = [0,12,2,3,122,12]
# if 2 in liste: # motsatt: legg inn not foran True
#     print(True)
#     
# # funksjoner som index, sort, reverse, remove
# print(liste.index(3)) # Hvilket nummer er første treff på 3
# liste.sort() # Den sorterer seg selv
# print(liste)
# liste.reverse() # Den sorterer seg selv
# print(liste) # Motsatt rekkefølge av slik den var
# liste.remove(122)
# print(liste)
# 
# del(liste[1])
# print(liste)
# print(min(liste))
# print(max(liste))
# 
# # kopiering av lister - en lager bare en peker!
# liste1 = [0,1,2,3]
# liste2 = liste1
# liste1[3] = 'heisann!'
# print(liste2)
# # For å lage en kopi må du kopiere hvert element i listen
# liste2 = [] + liste1
# 
# # eller
# liste2 = []
# for elem in liste1:
#     liste2.append(elem)
# print(liste2)
