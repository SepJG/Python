import pickle # Importerer pickle bibliotek

print('Skriv inn navn, telefon og adresse. Avslutt ENTER')

tlf={} # Oppretter tom dictionary

while True:
    navn = input('Navn: ')
    if(navn==''):
        break # Hopper ut av while-løkka
    telefon = input('Telefonnr: ')
    adresse = input('Adresse: ')
    tlf[navn]=[telefon,adresse]

filnavn = input('Skriv navn på fila: ')
f = open(filnavn,'wb') # Åpner fila for skriving, binær
pickle.dump(tlf,f) # Dumper tlf til disk
f.close() # Stenger fila
