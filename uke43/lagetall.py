import random

f = open('100tall.txt',"w") # Åpner fila for lesing
for i in range(100):
    f.write(str(random.randint(0,100))+"\n")

# Fancy måte (men ikke nødvendigvis bedre:)
#f.writelines([str(random.randint(0,100))+'\n' for x in range(100)])
f.close()
