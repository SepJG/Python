# Del 1:
# Lag en funksjon differanse(tall1, tall2)
# Den skal _returnere_ differansen mellom tallene,
# absoluttverdien
# Inntil videre kaller vi bare denne ved at du skriver ut
# resultatet av et kall til differanse() med to valgfrie tall

def differanse(tall1, tall2):
     return abs(tall1 - tall2)
    #return "hei"

tall1 = int(input("Skriv inn et tall: "))
tall2 = int(input("Skriv inn et til tall: "))
print(differanse(tall1, tall2))

# Del 2:
# Lag en funksjon tilfeldig_tall som spør brukeren om
# maksgrensen. Funksjonen skal returnere et tilfeldig tall
# mellom 0 og dette tallet.
import random
def tilfeldig_tall():
    tall = int(input("maks_antall"))
    return random.randint(0, tall)

# Del 3
# Lag funksjonen main()
# Den skal hente inn to tilfeldige tall med
# maksgrense gitt over. Så skal den skrive
# ut tallene og absoluttverdien av differansen.
# kjør så main()
