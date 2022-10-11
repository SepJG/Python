def f2c(F):
    C = (F-32) * 5/9
    return C

def c2f(C):
    F = (C*9/5) + 32
    return F

def main():
    C = int(input("Skriv temperatur i celsius:"))
    F = int(input("Skriv temperatur i fahrenheit:"))
    print(f"Temperatur i Fahrenheit blir {round(c2f(C))} og temperatur i Celsius blir {round(f2c(F))}")

main()