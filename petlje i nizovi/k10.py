#Napisati program koji računa aritmetičku i geometrijsku sredinu liste brojeva.
import math
lista=list(map(int,input("Unesite brojeve: ").split()))
suma=0
for i in lista:
    suma+=i
ari=suma/(len(lista))
print(ari)
proizvod=1
for broj in lista:
    proizvod*=broj
geo=math.pow(proizvod,1/len(lista))
print(f"aritmeticka sredina: {ari}, geometrija sredina: {geo}")