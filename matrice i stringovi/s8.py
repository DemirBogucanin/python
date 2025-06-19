#Brojanje slova u rečenici 
def brojanje_slova(recenica):
    # Kreiranje praznog rečnika za brojanje slova
    broj_slova = {}

    # Prolazak kroz svaki karakter u rečenici
    for slovo in recenica:
        # Proveravamo samo slova (ignorišemo razmake i interpunkciju)
        if slovo.isalpha():  # isalpha() proverava da li je slovo
            slovo = slovo.lower()  # Pretvaramo u mala slova (ne razlikujemo velika i mala slova)
            
            # Ako slovo već postoji u rečniku, povećaj broj
            if slovo in broj_slova:
                broj_slova[slovo] += 1
            else:
                broj_slova[slovo] = 1  # Ako slovo nije u rečniku, dodaj ga sa vrednošću 1
    
    # Ispisivanje rezultata
    for slovo, broj in broj_slova.items():
        print(f"Slovo '{slovo}' se pojavljuje {broj} puta.")

# Unos rečenice od korisnika
recenica = input("Unesite rečenicu: ")

# Pozivanje funkcije za brojanje slova
brojanje_slova(recenica)
