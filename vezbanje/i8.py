# c[i] = max(a[i], b[i]). 

def unos(n):
    niz1 = list(map(int, input(f"Unesite {n} brojeva za prvi niz: ").split()))
    niz2 = list(map(int, input(f"Unesite {n} brojeva za drugi niz: ").split()))
    return niz1, niz2

def obrada(niz1, niz2):
    c = [max(niz1[i], niz2[i]) for i in range(len(niz1))]
    return c

def ispis(niz1, niz2):
    c = obrada(niz1, niz2)
    for el in c:
        print(el)

n = int(input("Unesite n: "))
niz1, niz2 = unos(n)
ispis(niz1, niz2)


    