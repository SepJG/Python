def main():

    try:
        tall = int(input("Skriv inn et tall: "))
        print("500 delt på",tall,"er",500/tall)
        filnavn=input("Skriv inn et filnavn: ")
        f = open(filnavn)
        tekst=f.read()
        print(tekst)

        
    except ValueError:
        print("FEIL: Må skrive inn et tall, ikke tekststreng!!!")
    except ZeroDivisionError:
        print("FEIL: Kan ikke skrive tallet 0!!!")
    except IOError:
        print("FEIL: Det oppsto en feil ved lesing av fila",filnavn)
    except:
        print("FEIL: Programmet feilet av uvisst grunn!")

main() 
