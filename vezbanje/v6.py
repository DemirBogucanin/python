#Izbacivanje duplikata iz liste

brojevi = []  
N = int(input("Koliko brojeva želite da unesete? "))

for _ in range(N):
    i = int(input("Unesite broj: "))
    brojevi.append(i)

bez_duplikata = []  

for broj in brojevi:
    if broj not in bez_duplikata:
        bez_duplikata.append(broj) 

print("Lista bez duplikata:", bez_duplikata)
