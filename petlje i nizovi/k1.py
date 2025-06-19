#Napisati program koji izračunava zbir svih cifara unetog broja.
broj=int(input("Unesite broj: "))
suma=0
while (broj>0):
    cifra=broj%10
    suma+=cifra
    broj//=10
print(suma)