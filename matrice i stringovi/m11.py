#Rotacija niza bez slice operatora
#Napiši program koji rotira niz ulevo za k pozicija koristeći petlje (bez korišćenja slice operatora).

niz=list(map(int,input("Unesite niz: ").split()))
k=int(input("Unesite k: "))
n=len(niz)
for i in range(k):
    prvi=niz[0]
    for j in range(n-1):
        niz[j]=niz[j+1]
    niz[n-1]=prvi
print(niz)