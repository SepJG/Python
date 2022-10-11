# et eksempel på hvordan man kan løse en slik oppgave
# gjennom bruk av både lister og strengmanipulasjon

def roter(tegn):
#    print(tegn, end="")
    oord = ord(tegn)
    if oord < 97 or oord > 122:
        return tegn
    if oord > 119: # Flippe tilbake til starten av alfabetet
        return chr(oord-(122-96)+3)
    else:
        return chr(oord+3)

def caesar(streng):
    nystreng = []
    for tegn in streng:
        nystreng.append(roter(tegn))
    return "".join(nystreng)

print(caesar("abcdefghijklmnopqrstuvwxyz"))
