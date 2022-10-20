import random

'''
Opprette tom dictionary/ordbok
Gjøre om strengen til liste av ord
Gå igjennom hvert ord og:
 - Er ordet i dict fra før? Legg på 1 på verdien som er der
 - Hva skal du gjøre hvis ordet ikke er det fra før? Se på d.get igjen.
Returner dictionary
'''

def count_words(streng):
    dict = {}
    ord = streng.split()
    for o in ord:
      gammelverdibako = dict.get(o,0)
      nyverdibak0 = gammelverdibako + 1
      dict[o] = nyverdibak0
    return dict # Ja, _hva_ skal den returnere tro!
    
import random

# Jeg lager bare kjapt en streng med en drøss tilfeldige tall mellom 0 og 10:
streng = " ".join([str(random.randint(1, 15)) for i in range(100)])
print(streng)
d = count_words(streng)

pass
# skriver dem ut:
# for key in sorted(d):
#     print(f'{key} var der {d[key]} ganger.')

# # Hvis dere har veldig lyst:
# import lyric
# print(count_words(lyric.TEKST))

