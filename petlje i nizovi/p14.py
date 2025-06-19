#Pronaći drugi najmanji broj u listi brojeva.
niz=list(map(int,input("Unesite element").split()))
brojevi=sorted(set(niz))
if len(brojevi)>1:
    print(f"Drug najmanji element je {brojevi[1]}")
else:
    print("Lista je mala")