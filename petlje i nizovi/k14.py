#Sastaviti funkciju koja prima dva broja i vraća njihov najmanji zajednički sadržalac (NZS).

import math

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def nzs(a,b):
    nz=gcd(a,b)
    return abs(a*b)//nz
a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
rezultat = nzs(a, b)
print(f"Najmanji zajednički sadržalac ({a}, {b}) je: {rezultat}")