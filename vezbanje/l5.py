#Provera da li su svi elementi liste neparni 

def neparni(broj,n):
    for i in broj:
        if i%2==0:
            return False
    return True
brojevi = list(map(int, input("Unesite brojeve odvojene razmakom: ").split()))
if neparni(brojevi):
    print("Svi brojevi su neparni.")
else:
    print("Postoji bar jedan paran broj.")