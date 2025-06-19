#Rotacija niza ulevo
#Napiši program koji unosi niz celih brojeva i broj pozicija k, te rotira niz ulevo za k pozicija koristeći slice operatore.

niz = list(map(int, input("Unesite niz: ").split()))
k = int(input("Unesite broj pozicija za rotaciju: "))
k = k % len(niz)
rotirani_niz = niz[k:] + niz[:k]

print("Rotirani niz:", rotirani_niz)
