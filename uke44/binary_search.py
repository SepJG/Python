# Name: binary_search
# Input: a list and a search value
# Ouput: Index of first occurrence of searchValue is found, else -1
# Description: Search through a sorted list using the binary search algorithm

def binary_search(liste, verdi, imin, imax):
    if imax < imin:
        return False
    else:
        imid = (imin+imax)//2 # Midtpunktet
        if verdi < liste[imid]:
            return binary_search(liste, verdi, imin, imid-1)
        elif (verdi>liste[imid]):
            return binary_search(liste, verdi, imid+1, imax)
        else:
            return imid

A = [1,2,3,9,11,13,17,25,57,90]
result = binary_search(A, 57, 0, len(A)-1)
print(result)

