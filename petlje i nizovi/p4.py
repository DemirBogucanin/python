#Više naredbi u if grani: Napisati program sa više naredbi unutar jedne if grane (npr. validacija unosa).
stanje = 1000
while True:
    print(f"\nStanje: {stanje}€")
    akcija = input("Unesite 'p' za podizanje ili 'i' za izlaz: ")
    if akcija == 'i':
        break
    elif akcija == 'p':
        iznos = int(input("Unesite iznos: "))
        if iznos <= stanje:
            stanje -= iznos
            print("Uspešno podizanje.")
        else:
            print("Nedovoljno sredstava.")