#Formiranje niza maksimalnih elemenata
# Funkcija za unos nizova
def unos():
    niz1 = list(map(int, input("Unesite prvi niz: ").split()))
    niz2 = list(map(int, input("Unesite drugi niz: ").split()))
    return niz1, niz2
def obrada(niz1, niz2):
    maks1 = max(niz1) 
    maks2 = max(niz2)  
    niz3 = [maks1, maks2]  
    return niz3
def ispis(niz3):
    print(niz3)
niz1, niz2 = unos()  # Unos nizova
niz3 = obrada(niz1, niz2)  
ispis(niz3) 


    
    
