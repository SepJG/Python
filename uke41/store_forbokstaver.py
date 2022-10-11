# Funksjon som gjør at alle ord i en setning starter med stor bokstav
def overskrift(tekst):
  liste_tekst=tekst.split() # Gjør om tekst til liste med ord
  ny_tekst="" # Lager en tom streng
  for ord in liste_tekst: # Går igjennom tekststrengen ord for ord
    ny_tekst+= ord[0].upper()+ord[1:] # Lager stor forbokstav og legger til resten
    ny_tekst+=" " # Legger space mellom hvert ord
  return ny_tekst # Returnerer ny tekststreg

tekst="Jeg gikk en tur på stien og hørte skogens ro."
print(overskrift(tekst))

