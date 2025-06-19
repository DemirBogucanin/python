#Napraviti funkciju koja prima proizvoljan broj ključ-vrednost parova i vraća rečnik.
def recnik(**rec):
    return rec
rezultat=recnik(demir=29,emin=18,emir=8)
print(rezultat)
podaci={"semir":10,"mir":19}
novi=recnik(**podaci)
print(novi)