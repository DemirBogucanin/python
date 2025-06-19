#Sastaviti funkciju koja proverava da li je uneti broj Armstrongov broj (npr. 153 jer je 1³ + 5³ + 3³ = 153).

import math
def arm(broj):
    suma=0
    n=broj
    while broj>0:
        cifra=broj%10
        suma+=math.pow(cifra,3)
        broj//=10
    if suma==n:
        return "Steje armstrongov broj"
    else:
        return "jeni arsmtrongov broj"
broj=int(input("Unesite broj: "))
m=arm(broj)
print(m)