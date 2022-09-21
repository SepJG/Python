# Dagens tema: løkker og sløyfer
# while
# for


# Oppgave 1:
# Be brukeren om å skrive inn en streng som er enten 'krone' eller 'mynt'
# Hvis svaret er 'krone' skriver du ut 'krone'
# Hvis svaret er 'mynt' skriver du ut 'mynt'
# ellers skriver du ut 'feil svar'

# Oppgave 2: brukeren kan skrive 'k' eller 'm' også!
# hvordan skal du snike inn en or i de to testene?
# Dette er en utrolig vanlig feil: tall == 3 or 4  

# Oppgave 3: gjør dette i en uendelig løkke
# tips: hvis du skal 'lempe' en de linjer ett hakk mot høyre,
# da kan du markere dem og trykke på <tab> (shift-tab mot venstre)

# Oppgave 4
# Lag to variable, krone og mynt, FØR while-løkken, begge 0.
# Hvorfor må disse variablene deklareres før løkken og ikke inni?
# Øk respektive variabel med 1 basert på om det blir krone eller mynt.
# Hver gang gjennom løkken skal du til slutt skrive ut
# hvor mange krone og mynt brukeren har skrevet inn til nå.

antall_k = 0
antall_m = 0

while (antall_k + antall_m) < 10:
    svar = input("krone eller mynt: ")
    if (svar == 'krone') or (svar == 'k'):
        antall_k += 1
        print('krone')
    elif (svar == 'mynt') or (svar == 'm'):
        antall_m += 1
        print('mynt')
    else:
        print("Feil svar")
    print(f"k:{antall_k}, m:{antall_m} ({antall_k + antall_m})")

# Oppgave 5: Tell antall ganger du har kastet krone eller mynt
# Hvor må du deklarere denne variabelen for at den skal
# 'holde seg' hver gang gjennom løkken?
# Bonuspoeng hvis du skriver ut prosentandel krone hver runde

# Oppgave 6: Avslutt etter ti kast!
# while tester om noe er sant. Er det sant, da kjører den løkken
# Hvis ikke, da avslutter den løkken og går videre
# Hvordan kan du endre while-testen så den returnerer sant hvis og bare hvis
# variabelen kast er ti eller mindre?

# Oppgave 7: Rensk opp
# Fjern unødvendige utskrifter
# Endre slik at du skriver ut antall kron, mynt (og prosentandel mynt)
# etter at alle er skrevet inn

# Oppgave 8: hvorfor 10 kast?
# Spør brukeren hvor mange ganger det skal kastes
# hvordan kan en bruke dette rett i while-testen?


# Oppgave 9: hvorfor bestemme kast først?
# Det er mye bedre å spørre brukeren om hen skal kaste en
# gang til. Endre ting slik at du i stedet spør i slutten av
# løkka om man skal legge inn en gang til, og så sjekker while
# mot denne. Men da må du ha satt den til noe før du går inn i
# løkka også. Men denne er ment å være tricky, jeg viser løsningen
# i videoen. OG eksempel i jukselappen i samme folder som denne!  

