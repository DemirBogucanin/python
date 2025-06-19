#Napisati program koji za uneti string ispisuje koliko puta se svako slovo pojavljuje.
def ponavljanje(s):
    brojac={}
    for slovo in s:
        if slovo in brojac:
            brojac[slovo]+=1
        else:
            brojac[slovo]=1
    return brojac
string=input("Unesite string: ")
rezultat=ponavljanje(string)
for slovo, broj in rezultat.items():
    print(f"'{slovo}' se pojavljuje {broj} puta")
