#Napiši funkciju koja rotira elemente liste za k pozicija ulevo ili udesno. 
def rotacija(lista,k,pravac):
    if pravac=="levo":
        k=k%len(lista)
        lista=lista[k:]+lista[:k]
    elif pravac=="desno":
        k=k%len(lista)
        lista=lista[-k:]+lista[:-k]
    return lista
lista = list(map(int, input("Unesite elemente liste (odvojene razmakom): ").split()))
k = int(input("Unesite broj k: "))
pravac = input("Unesite pravac rotacije ('levo' ili 'desno'): ").strip().lower()

# Pozivanje funkcije i ispis rezultata
novalista = rotacija(lista, k, pravac)
print("Rezultat rotacije:", novalista)