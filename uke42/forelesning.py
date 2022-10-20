# import random

# liste = [random.randint(0,100) for x in range(6)]
# sett1 = set(liste)
# liste = [random.randint(0,100) for x in range(6)]
# sett2 = set(liste)

# print(sett1.union(sett2))
# # unike = []

# for tall in liste:
#   if tall not in unike:
#     unike.append(tall)

# print(type(set(liste)))


#Dictionaries

dict = {}
dict['espen'] = 45
dict['pia'] = 25
dict['bernt'] = 12

# print(dict.get('pia',0))
# print(dict.get('oskar',0))
# print(dict.keys())

# for key in dict.keys():
#   print(key, dict[key])

# for value in dict.values():
#   print(value)

# for k,v in dict.items():
#   print(k, v)

# for k in dict.keys():
#   print(k, dict[k])

for k in sorted(dict):
  print(k, dict[k])