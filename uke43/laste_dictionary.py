import pickle # Importerer pickle bibliotek

filnavn = input("Skriv inn navn på datafil: ")

f = open(filnavn,"rb") # Åpner for lesing og binærfil
database = pickle.load(f) # Laste inn dictionary fra disk
f.close() # Stenger fila

for item in database:
    print(item,":",database[item])
