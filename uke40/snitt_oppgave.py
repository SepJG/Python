# Oppgave 1:
# Skriv funksjonen lag_tall_liste()
# Inneholder en løkke der brukeren blir bedt om å skrive inn heltall.
# Hvert tall skal legges til i en liste. Når brukeren taster inn 0 skal
# listen med alle tallene som er lagt inn til nå returneres. Se eksempel

# Eks:
# print(lag_tall_liste())
# [2, 3, 11, -1, 122]

# def lag_tall_liste():
#     liste = []
#     svar = int(input("tall: "))
#     while svar:
#         liste.append(svar)
#         svar = int(input("tall: "))
#     return liste
# print(lag_tall_liste())

# def ltl():
#     liste = []
#     while tall := int(input("tall:")):
#         liste.append(tall)
#     return liste
# print(ltl())

# def ltl2():
#     liste = []
#     while True:
#         tall = int(input("tall:"))
#         if not tall: 
#           return liste
#         else: 
#           liste.append(tall)
# print(ltl2())

# Oppgave 2
# Skriv funksjonen beregn_snitt():
# Denne funksjonen skal ta inn en liste som parameter,
# beregne gjennomsnittet av alle tall i listen, og returnere
# dette snittet. Se eksempel

# print(gjennomsnitt([2, 3, 11, -1, 122]))
# 27.4

# def beregn_snitt(liste):
#     return sum(liste)/len(liste)

# print(beregn_snitt([2, 3, 11, -1, 122]))

# Oppgave 3
# Skriv funksjonen topp_og_bunn().
# Funksjonen tar inn en liste, og returnerer TO ting:
# Laveste og høyeste verdi i listen. Se eksempel

# print(topp_og_bunn([2, 3, 11, -1, 122]))
# (-1, 122)

def topp_og_bunn(liste):
     return min(liste),max(liste)

svar = topp_og_bunn([2, 3, 11, -1, 122])
print(svar)
#svar[0] = 12

