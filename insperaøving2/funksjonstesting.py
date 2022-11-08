# Lag en funksjon test(funksjon, inn, ut). inn og ut er lister med verdier. 
# test skal returnere True kun dersom funksjon(inn[i]) == ut[i]) for alle inputs.
# Eksempel:

# def kvadrat(x):
#     return x * x

# inn = [1, 2, 10]
# ut = [1, 4, 100]
# print(test(kvadrat, inn, ut)) # Vil printe True

# inn = [1, 3]
# ut = [1, 10]
# print(test(kvadrat, inn, ut)) # Vil printe False fordi kvadrat(3) != 10

def test(funksjon, inn, ut):
    for i in range(len(inn)):
        if funksjon(inn[i]) != ut[i]:
            # Feil i funksjonen
            return False
    # Ingen feil
    return True

def kvadrat(x):
  return x * x

inn = [1, 2, 10]
ut = [1, 4, 100]
print(test(kvadrat, inn, ut)) 

inn = [1, 3]
ut = [1, 10]
print(test(kvadrat, inn, ut)) 
