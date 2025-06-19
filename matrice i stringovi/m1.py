#Ispis prvog i zadnjeg elementa niza

niz = input("Unesite elemente niza odvojene razmakom: ").split()
if len(niz) < 3:
    print("Niz mora imati bar tri elementa.")
else:
    treci_element = niz[2]
    poslednji_element = niz[-1]
    print(f"Treći element niza: {treci_element}")
    print(f"Poslednji element niza: {poslednji_element}")   