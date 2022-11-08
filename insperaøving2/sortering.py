# Lag en funksjon sorterEtterNavn(personer) som tar inn en liste med navn  (Eks: ["Thomas", "Sara", "Eric"]) 
# og returnerer listen sortert alfabetisk.
# Eks:

# personer = ["Thomas", "Sara", "Eric"]

# print(sorterEtterNavn(personer))
# Vil printe: ["Eric", "Sara", "Thomas"]

# Med sorted()
def sorterEtterNavn(personer):
    return sorted(personer)
    
# Med list.sort()
def sorterEtterNavn(personer):
    personerCopy = personer.copy()
    personerCopy.sort()
    return personerCopy
print(sorterEtterNavn(["Thomas", "Sara", "Eric"]))