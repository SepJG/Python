# liste1 = list(range(6))
# print(liste1)
# print(liste1[4])
# liste1[-1] = 0
# print(liste1)

# liste2 = list("JegborpåGløshaugen")
# print(liste2)

# liste3 = [i for i in range(51) if i % 2 == 0]
# print(liste3)

# liste4 = [True if i%2 == 0 else False for i in range(20)]
# print(liste4)

# def printNumberList(i, lst):
#   print(f"Element på indeks {i} er {lst[i]}")
# printNumberList(0, liste1)
# printNumberList(4, liste1)
# printNumberList(-2, liste1)

# def firstHalf(lst):
#   firstHalf = lst[:len(lst)//2]
#   return firstHalf
# liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(firstHalf(liste))


# def remove_ends(lst):
#   new_list = lst[1:len(lst)-1]
#   return new_list
# liste = [1,2,3,4,5,6,7,8,9,10]
# print(remove_ends(liste))

import random
def roll_dice():
  liste = list(random.randint(1,6) for i in range(5))
  return liste
# print(roll_dice())


def count_numbers(lst,i):
  count = 0
  for item in lst:
    if item == i:
      count += 1
  print(count)
# count_numbers([1,1,5,4,6,3,7],3)


def yatzy():
  sum = 0
  for i in range(1,7):
    current_throw = roll_dice
    sum += count_numbers(current_throw,i)
    print(f"Number: {i}. Number of occurences: {count_numbers(current_throw,1)}")
    print(f"Sum: {sum}")
    return sum
    
yatzy()
