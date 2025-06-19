def srednja_duzina_reci(naziv_fajla):
    try:
        with open(naziv_fajla, "r", encoding="utf-8") as fajl:
            tekst = fajl.read()
        reci = tekst.split()
        ukupna_duzina = sum(len(reka) for reka in reci)

        if len(reci) == 0:
            return 0  
        else:
            srednja_duzina = ukupna_duzina / len(reci)
            return srednja_duzina

    except FileNotFoundError:
        print(f"Datoteka '{naziv_fajla}' nije pronađena.")
        return None
    except Exception as e:
        print(f"Došlo je do greške: {e}")
        return None

naziv_fajla = "tekst.txt"  
rezultat = srednja_duzina_reci(naziv_fajla)
if rezultat is not None:
    print(f"Srednja dužina reči u datoteci '{naziv_fajla}' je: {rezultat:.2f}")
