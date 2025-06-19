"""#Obrnuti redosled

def obrnuta(niz):
    for i in range(len(niz)//2):
        niz[i],niz[-i-1]=niz[-i-1],niz[i]
niz=list(map(int,input("Unesite elemente: ").split()))
print("originalni niz",niz)
obrnuta(niz)
print("novi niz",niz)"""

"""#Zbir parnih i neparnih

def parnep(niz):
    s1=0
    s2=0
    for i in niz:
        if i%2==0:
            s1+=i
        if i%2==1:
            s2+=i
    return s1,s2
niz=list(map(int,input("Unesite elemente niza: ").split()))
zbir=parnep(niz)
print(zbir)"""

"""#Prosek bez minimuma i maksimuma

def prosek(niz):
    s=0
    a=max(niz)
    b=min(niz)
    niz.remove(a)
    niz.remove(b)
    n=len(niz)
    for i in niz:
        s+=i
    return s/n

niz=list(map(int,input("Unesite elemente: ").split()))
print(niz)
ari=prosek(niz)
print(f"prossek bez naj i najv je {ari}")"""


"""#Najduža rastuća podlista 

def podlista(niz):
    tren=1
    maks=1
    for i in range(1,len(niz)):
        if niz[i]>niz[i-1]:
            tren+=1
        else:
            maks=max(maks,tren)
            tren=1
    maks=max(maks,tren)
    return maks,tren
    
niz=list(map(int,input("Unesite niz: ").split()))
gas=podlista(niz)
print(niz)"""

"""#rotacija liste

def rotacija(niz,k):
    k=k%len(niz)
    return niz[k:] + niz[:k]
niz = list(map(int, input("Unesite niz: ").split()))
k = int(input("Unesite k: "))

# Pozivanje funkcije
novi_niz = rotacija(niz, k)
print("Nakon rotacije ulevo:", novi_niz)"""

"""#Matrica transponovanje

redovi = int(input("Redovi = "))
kolone = int(input("Kolone = "))

# Unos matrice
matrica = [list(map(int, input(f"Unesite {kolone} elementa za red {i+1}: ").split())) for i in range(redovi)]

# Transponovanje matrice koristeći zip
transponovana_matrica = [list(row) for row in zip(*matrica)]

# Ispis matrice
print("Originalna matrica:")
for red in matrica:
    print(red)

print("Transponovana matrica:")
for red in transponovana_matrica:
    print(red)"""
    
"""#Glavna i sporedna dijagonala

redovi=int(input("Unesite broj redova: "))
kolone=int(input("Unesite broj kolona: "))
matrica=[list(map(int,input("Unesite {kolona} elemenata za svaki red").split())) for i in range(redovi)]
for i in range(redovi):
    print(matrica[i][i], end=" ")
print("sporedna")
for i in range(redovi):
    print(matrica[i][redovi-i-1], end=" ")  """
    
     

