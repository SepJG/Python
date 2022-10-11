# Funksjon som skriver ut indeks der tegn befinner seg i tekst
def skriv_tegn_indeks(tekst, tegn): 
  for indeks in range(0, len(tekst)):
    if tekst[indeks] == tegn:
      print(indeks)


tekst="Jeg gikk en tur på stien og hørte skogens ro."
tekst+="Da hørte jeg fra lien en fugls som sa ko-ko."
tekst+="Ko-ko, ko-ko, ko-ko-ko-ro-ko-ko."
tekst+="Ko-ko, ko-ko, ko-ko-ko-ro-ko-ko."

skriv_tegn_indeks(tekst,"e")

