#Sastaviti funkciju koja proverava da li je uneti broj paran ili neparan

def parnost(broj):
    if broj%2==0:
        return "paran"
    else:
        return "neparan"
        
broj=int(input("Unesite broj"))
print(parnost(broj))
