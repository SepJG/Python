# Et program som leser inn et tall fra tastaturet
# og konverterer det til float

try:
    tall = input('Oppgi et tall: ')
    print(float(tall))
except:
    print('Det går ikke.')
