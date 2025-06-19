#Obrnuti cifre unetog broja (npr. 1234 → 4321).
broj=int(input("Unesite broj: "))
obrnuti=0

while broj>0:
    cifra=broj%10
    obrnuti=obrnuti*10+cifra
    broj//=10
print(obrnuti)