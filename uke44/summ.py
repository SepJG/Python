import random 

def summ():
#     temp = random.randint(0,100)
    temp = int(input("tall: "))
    print(temp)
    if temp > 80:
        return [temp]
    tmpsum = summ()
    print(tmpsum, temp)
    return tmpsum+[temp]

print(summ())
    
