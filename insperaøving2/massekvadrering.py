# Lag en funksjon kvadrer(l) som tar inn en liste med tall, og returnerer en ny liste der alle tallene er kvadrert.
# Eksempel:

# >>> liste = [1, 2, 5, 9]
# >>> kvadrer(liste)
# [1, 4, 25, 81]

# Med map
def kvadrer(l):
    return list(map(lambda x: x * x, l))

# Med list comprehension
def kvadrer(l):
    return [x * x for x in l]

# Med en for-løkke
def kvadrer(l):
    out = []
    for x in l:
        out.append(x*x)
    return out

liste = [1, 2, 5, 9]
print(kvadrer(liste))