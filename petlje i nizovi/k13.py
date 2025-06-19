#Napisati program koji iz niza uklanja sve duplikate i ispisuje preostale elemente.

lista=list(map(int,input("Unesite elemente: ").split()))
ostali=[]
for i in lista:
    if i not in ostali:
        ostali.append(i)
print(ostali)