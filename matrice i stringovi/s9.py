#Provera heterograma 
def heerogram(recenica):
    slova=set()
    for karakter in recenica:
        if karakter.isalpha():
            karakter=karakter.lower()
            if karakter in slova:
                return False
            slova.add(karakter)
    return True
recenica=input("Unesite recenicu: ")
if heerogram(recenica):
    print("Recenica je here")
else:
    print("Nije")