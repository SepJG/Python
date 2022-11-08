# Be brukeren om å skrive inn to tall.
# Skriv ut '3 delt på 2 er 1.5'
# Innkapsle delingen i en try/except, slik at deling på 0 ikke utløser unntak
# men heller skriver ut 'Noe galt har skjedd'

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(f'{a} delt på {b} er {a/b}')
except ValueError:
    print('Noe er feil')
except ZeroDivisionError:
    print('Dele på null er ikke bra')
except:
    print('Noe annet er feil')
else:
    print('Hvordan blir du med i leken, da?')
finally:
    print('Til slutt!')

