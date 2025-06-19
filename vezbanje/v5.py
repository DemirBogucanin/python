#Suma unetih brojeva (prekid na nulu)
suma=0
ari=0
while True:
    broj=int(input("Unesite broj: "))
    
    if broj==0:
        break
    suma+=broj
print(suma)