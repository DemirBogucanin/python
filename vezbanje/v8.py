"""suma cifara broja

def suma(n):
    return sum(int(cifra) for cifra in str(n))
n=int(input("Unesit n: "))
s=suma(n)
print(s)"""

"""Filtriranje prostih brojeva
def prost(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtriraj_proste(lista):
    
    prosti_brojevi = [broj for broj in lista if prost(broj)]
    
    if prosti_brojevi:
        print("Prosti brojevi:", prosti_brojevi)
    else:
        print("Nema prostih brojeva")

# Unos liste brojeva
lista = list(map(int, input("Unesite listu brojeva: ").split()))
filtriraj_proste(lista)"""

"""#Obrtanje stringa koristeći funkciju

def sortiranje(string):
    string=niz[::-1]
    return string
niz=input("Unesite string: ")
gas=sortiranje(niz)
print(gas)"""

"""#Prosečna vrednost liste brojeva
def prosek(niz):
    suma=0
    for i in niz:
        suma+=i
    return suma/i
niz=list(map(int,input("Unesite listu: ").split()))
pro=prosek(niz)
print(pro)"""

"""Pretvaranje temperature

def far(cel):
    farenhajt = []  # Lista u kojoj ćemo čuvati rezultate
    for temp in cel:
        farenhajt.append((temp * 9/5) + 32)  # Formula za konverziju
    return farenhajt

# Unos temperature u Celzijusima
temperature = list(map(float, input("Unesite temperature u °C (razdvojene razmakom): ").split()))

# Poziv funkcije
farenhajt = far(temperature)

# Ispis rezultata
print("Temperature u °F:", farenhajt)"""

"""Brojanje samoglasnika u stringu
def samoglasnici(string):
    sam="aeiou"
    broj=0
    for i in string:
        if i in sam:
            broj+=1
    return broj
string=input("Unesite string: ")
niz=samoglasnici(string)
print(niz)"""

"""Palindromska provera
def palindrom(string):

    if string==string[::-1]:
        print("Jeste")
    else:
        print("Nije")
string=input("Unesite tekst: ")
palindrom(string)"""

"""Najduža reč u stringu

def najduzi(string):
    reci=string.split()
    najduza=max(reci,key=len)
    return najduza
string=input("Unesite sstring: ")
rezultat=najduzi(string)
print(rezultat)"""

"""#Kvadrati parnih brojeva

def parni(niz):
    novi=[]
    for i in niz:
        if i%2==0:
            novi.append(i*i)
    return novi
niz=list(map(int,input("Unesite elemente: ").split()))
steje=parni(niz)
print(steje)"""

"""#Provera anagrama

def anagram(string1,string2):
    string1=string1.replace(" ","").lower()
    string2=string2.replace(" ","").lower()
    if sorted(string1)==sorted(string2):
        print("STeje")
    else:
        print("Nije")
string1=input("Unesite string: ")
string2=input("Unessite drugi string: ")
anagram(string1,string2)"""

"""#Najčešći karakter u stringu


def najcesci(string):
    frekvencija = {}  # Koristimo rečnik da pratimo broj ponavljanja karaktera
    
    for i in string:
        if i in frekvencija:
            frekvencija[i] += 1  # Povećavamo broj ako je karakter već u rečniku
        else:
            frekvencija[i] = 1  # Ako karakter nije u rečniku, dodajemo ga sa brojem 1
    
    # Pronalazimo karakter sa najvećim brojem ponavljanja
    najcesci = max(frekvencija, key=frekvencija.get)
    
    return najcesci

# Unos stringa
string = input("Unesite string: ")

# Poziv funkcije
rezultat = najcesci(string)

# Ispis rezultata
print(f"Najčešći karakter je: '{rezultat}'")"""

"""#treca lab vezba 1.zadatak
def unos():
    n=int(input("Unesite broj elemenata: "))
    a=list(map(int,input("Unesite elemente: ").split()))
    b=list(map(int,input("Unesite elemente: ").split()))
    if n<1 or n>200:
        return False
    if len(a)!=n or len(b)!=n:
        return False
    else: 
        return a,b
    
def obrada(a,b):
    
    return [max(a[i],b[i]) for i in range (len(a) and len(b))]
def ispis(c):
    
    print(*c)
while True:
    podaci = unos()
    if podaci is None:  # Prekid ako je unos nevalidan
        break
    a, b = podaci
    c = obrada(a, b)
    ispis(c)"""


"""#treca lab vezba drugi zadatak

n=int(input("Unesite broj elemenata: "))
if n<3 or n>100:
    print("Broj se ne nalazi u tom opsegu")
else:
    a=list(map(int,input(f"Unesite {n} elemenata").split()))
    for i in range(1,n-1):
        if a[i]==(a[i-1]+a[i+1]/2):
            print(i)"""
            
            
"""#treca lab vezba 5.zad

def dozvoljeni():
    a=input("Unesite dozvoljene znakove: ")
    return a
def palindrom(b,a):
    for i in b:
        if i not in a:
            return False
    return b==b[::-1]
znakovi=dozvoljeni()
while True:
    b=input("Unesite string").strip()
    if b=="":
        break
    if palindrom(b,znakovi):
        print("Palindrom")
    else:
        print("Nije palindrom")"""



#treca lab vezba 7. zad








        

