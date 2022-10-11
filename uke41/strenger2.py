print("Avslutt programmet med å skrive 'stopp'")
svar = ""
while(svar!="stopp"):
    svar = input("\n\nSkriv inn tekst: ")
    lengde = len(svar)
    print("Første halvdel er:",svar[:lengde//2])
    print("Annenhver bokstav:",svar[::2])
    print("I store bokstaver:",svar.upper())
    print("Kun bokstaver?",svar.isalpha())
    print("Kun tall?",svar.isdigit())
    print("Erstatte 'er' med 'var':",svar.replace("er","var"))
    
print("\nEndelig ferdig med dette tullet, ble nesten gal!")

