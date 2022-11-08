# Name: insertion_sort
# Input: a list
# Output: a sorted liste
# Description: sort a list using the insertion sort algorithm

def insertion_sort(liste):
    L = len(liste)                # L er lengden av lista
    for i in range(1,L):          # range gaar til L-1
        element = liste[i]
        hull = i
        while hull > 0 and liste[hull-1] > element:
            liste[hull] = liste[hull-1]
            hull = hull - 1
            
        liste[hull] = element
    return liste

A=['Petter','Alex','Diana','Bodil','Anne']
B=insertion_sort(A)
print(B)

