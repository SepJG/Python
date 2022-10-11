# Ignorer måten jeg skriver dette - det kalles 'list comprehension' og er utrolig effektivt.
# jeg kommer til å vise det i mer detalj senere, men dette lager en liste med tall fra 0 til 9.
liste1 = [x for x in range(10)]

# Denne vil nå skrive ut tallene mellom 0 og 9:
print(liste1)

print('\nbare bruk av = blir slik. Rimer, hihi')

# Nå setter vi nyliste lik liste
# Hvis vi endrer verdien på et element, da vil
# endringen vises på begge steder!
nyliste = liste1
liste1[0] = 'null'
print(liste1)
print(nyliste)

# Dette skjer fordi nyliste peker til det samme
# minneområdet. Nå har vi altså to variable som
# peker til det samme stedet. Dette er kult, men
# det kan også hende at vi ikke ønsker at det
# skal skje. Dette kan vi fikse på et par ulike
# måter

print('\nbruk av []+liste1 blir slik:')
liste1 = [x for x in range(10)]
nyliste = []+liste1 # Ser du forskjellen fra eksempelet over?
liste1[0] = 'null'
print('liste1:',liste1) # Nå er disse 
print('nyliste:',nyliste)# to ulike 

# Her har vi altså satt nyliste til å bli verdien av
# en tom liste PLUSS verdien av liste1. DA kopieres
# verdiene, og det er ikke lenger en peker til samme
# sted i minneområdet.
