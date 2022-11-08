'''
Det som skjer her er at vi skal oppdatere en dict med verdier.
Første gang nøkkel og verdi legges til blir verdien lagt til
som verdien selv, nøkkelen lagt til som nøkkel. Så rart.
Vi bruker append, selv om append jo vil krasje hvis nøkkelen
ikke allerede finnes. Det løses med unntakshåndtering.
Hvis en senere forsøker å appende noe til den samme nøkkelen
(og verdi ikke er en liste) så vil et annet unntak utløses.
Liste lages, gammel verdi blir lagt inn der, så ny verdi.
Denne listen settes så til verdi.


Legg merke til at det er to unntak etter hverandre, som vil
kunne utløses av ulike situasjoner.

'''

def leggTilNoe(dikt):
    try:
        navn=input('For hvem vil du oppdatere dictionarien: ')
        leggTil = input('Oppgi verdien som skal legges til: ')
        dikt[navn].append(leggTil)

# Hver verdi er først tall. Dermed vil append krasje.
# da vil den utløse AttributeError. Her vil verdien
# gjøres om til en liste med det som fantes pluss det nye.

    except AttributeError as e:
        print('Håndterer AttributeError', e)
        dikt[navn] = [dikt[navn],leggTil]

# Hvis nøkkelen ikke allerede finnes kommer vi hit:

    except KeyError as e:
        print('Håndterer KeyError', e)
        dikt[navn] = leggTil


minDikt = {'Per':92925492}      # Opprette

print(minDikt)

minDikt['Nils'] = 92939495      # Legge til

print(minDikt)

leggTilNoe(minDikt)

print(minDikt)
