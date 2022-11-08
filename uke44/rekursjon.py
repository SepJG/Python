# Eksempel på rekursivt funsjonskall

def count_down(antall):
    if antall > 0:
        print("Teller ned:",antall)
        count_down(antall - 1)
    # base-case: antall == 0, da gjør vi ingen ting
    # her slutter funksjonen, og vi returnerer

count_down(5)
