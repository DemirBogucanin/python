#Tražiti od korisnika unos i upisati ga u tekstualnu datoteku.

with open("gas.txt","w",encoding="utf-8") as fajl:
    while True:
        recenica=input("Unesite recenicu: ")
        if recenica.lower()=="kraj":
            break
        fajl.write(recenica + "\n")