def unos():
    niz=list(map(int,input("Unesite elemente: ").split()))
    return niz
def jedan(niz,k):
    for i in niz:
        if i%k==0:
            print(niz)
            return True
        
    print("Nijedan nije deljiv")
            
    return False
def svi(niz,k):
    for i in niz:
        if i%k!=0:
            print("Nije deljiv sa k")
            return False
    print("Svi su elementi deljivi sa k")
    return True
niz=unos()
k=int(input("Unesite k: "))
jedan(niz,k)
svi(niz,k)