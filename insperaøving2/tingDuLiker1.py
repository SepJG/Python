# Lag en funksjon hvaBrukerLiker() som gjentakende sprør brukeren om ting de liker helt til de sier "ferdig". 
# Den skal returnere en liste med tingene. (NB: Den skal ikke printe det ut selv om det ser sånn ut i eksempelet)
# Eksempel:
# >>> hvaBrukerLiker()
# Si en ting du liker: hunder
# Si en ting du liker: taco
# Si en ting du liker: git
# Si en ting du liker: ferdig

# ["hunder", "taco", "git"]

def hvaBrukerLiker():
    ting = []
    while True:
        neste = input("Si en ting du liker: ")
        if neste == "ferdig":
            break
        ting.append(neste)
    return ting
print(hvaBrukerLiker())