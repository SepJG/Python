'''
def calculateScores(home, away):
    if home < away:
        print("Borteseier")
        
    elif home > away:
        print("Hjemmeseier")
        
    else:
        print("Uavgjort")
        
calculateScores(3, 3)
'''

puls = int(input("Din puls: "))
if puls > 160:
    print("Ikke tren på forelesning")
elif puls < 60:
    print("Det er ikke lov å sove i NTNU sine lokaler.")
else:
    print("k dud.")