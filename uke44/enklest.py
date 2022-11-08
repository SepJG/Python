def enklest(tall):
    print(tall)
    if tall > 0:
        enklest(tall-1)
        
enklest(10)

