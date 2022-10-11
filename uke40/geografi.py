import random

land = ['Norge','Sverige','Spania','USA','Finland','Island',
    'Danmark','Tyskland','Frankrike']

hovedsteder = ['Oslo','Stockholm','Madrid','Washington, D.C.',
           'Helsinki','Reykjavik','København','Berlin','Paris']


# skriv(land, hovedsteder)
# skrive ut, for alle par, 'Hovedstaden i Norge er Oslo.'

def skriv(land, hovedsteder):
  for l, h in zip(land, hovedsteder):
    print(f'Hovedstaden in {l} er {h}.')
    #  for i in range(len(land)):
    #      print(f'Hovedstaden in {land[i]} er {hovedsteder[i]}.')
        
        
# def nytt_land(land, hovedsteder):
#     tmpland = input("Land: ")
#     tmpstad = input("Stad: ")
#     land.append(tmpland)
#     hovedsteder.append(tmpstad)
#     return land, hovedsteder
    
# def spm(land, hovedsteder):
    
#     i = random.randint(0,len(hovedsteder))    
#     svar = input(f'Hva er hovedstaden i {land[i]}')
#     if svar == hovedsteder[i]:
#         print("jippi")
#     else:
#         print("nah")

# spm(land, hovedsteder)
