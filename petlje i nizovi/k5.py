#Sastaviti funkciju koja proverava da li su dva uneta broja međusobno prosti brojevi
import math

def medjusobno_prosti(a, b):
    return math.gcd(a, b) == 1

broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))

if medjusobno_prosti(broj1, broj2):
    print("Brojevi su međusobno prosti.")
else:
    print("Brojevi nisu međusobno prosti.")
