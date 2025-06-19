#Pronalaženje duplikata u list

def duplikat(lista):
    duplikati=set()
    vidjeni=set()
    for broj in lista:
        if broj in vidjeni:
            duplikati.add(broj)
        else:
            vidjeni.add(broj)
    return list(duplikati)
lista=list(map(int,input("Unesite listu: ").split()))
duplikati=duplikat(lista)
if duplikati:
    print(duplikati)
else:
    print("Nema")
