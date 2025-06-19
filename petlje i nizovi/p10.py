#Ispisati sve delioce unetog broja.
broj=int(input("Unesite broj: "))
for i in range(1, broj+1):
    if broj%i==0:
        print(i)