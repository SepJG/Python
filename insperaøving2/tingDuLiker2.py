# Lag en funksjon printHvaBrukerLiker(l) som tar inn en liste med strenger og printer ut en oppsummering ved å skrive ut alle ordene med komma mellom. 
# Det skal være "og" mellom de to siste tingene.
# Du kan anta at det er minst to strenger i listen
# Eksempel:

# >>> printHvaBrukerLiker(["hunder", "taco", "git"])
# Du liker hunder, taco og git

# Med join
def printHvaBrukerLiker(ting):
    print("Du liker " + ", ".join(ting[:-1]) + " og " + ting[-1])

# Med en for-løkke
def printHvaBrukerLiker(ting):
    print("Du liker ", end="")
    for neste in ting[:-1]:
        print(neste + ", ", end="")
    print("og " + ting[-1])

printHvaBrukerLiker(["kake","ost","pølse"])