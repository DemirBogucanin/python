def autentifikacija():
    korisnicko_ime = "korisnik"
    lozinka = "lozinka123"

    unos_ime = input("Unesite korisničko ime: ")
    unos_lozinka = input("Unesite lozinku: ")

    if unos_ime == korisnicko_ime and unos_lozinka == lozinka:
        print("Prijava uspešna!")
    else:
        print("Pogrešno korisničko ime ili lozinka.")

autentifikacija()
