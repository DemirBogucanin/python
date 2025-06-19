#Pronalaženje treće najveće vrednosti u listi

lista=list(map(int,input("Unesite listu: ").split()))

if len(lista)<3:
    print("Nema dovoljno elemenata")
else:
    lista.sort(reverse=True)
    print("Treci najveca vrednost je: ",lista[2])
        