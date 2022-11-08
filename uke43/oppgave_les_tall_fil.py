# Be om navnet på en fil som skal leses inn.
# Les innholdet av filen som blir skrevet inn.
# Hver linje inneholder tall (strenger) mellom 0 og 100
# Skriv ut en linje for hvert tall (opphøy hver tall i tredje):
# 22 i tredje er 10648.


filnavn = input("Oppgi navn på fila: ")
with open(filnavn,"r") as f: # Åpner fila for lesing
  liste = f.readlines()
  for tall in liste: # Enda en måte å lese inn, trenger ikke readline()
    ektetall = int(tall.strip()) # Oversetter streng til heltall
    print(f'{ektetall} i tredje er {ektetall**3}.')

