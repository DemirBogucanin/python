#Napiši program koji unosi niz brojeva, sortira ga u rastućem redosledu i ispisuje sortirani niz.

niz=list(map(int,input("Unesite niz: ").split()))
sortirano=sorted(niz)
print(sortirano)