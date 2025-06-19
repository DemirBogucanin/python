#Igra "Pogodi slovo"
import random

rec=input("Unesite rec: ").strip().lower()
if not rec:
    print("Niste uneli rec")
slovo=random.choice(rec)
while True:
    pokusaj=input("Unesite jedno slovo: ")
    if len(pokusaj)!=1 or not pokusaj.isalpha():
        print("Niste dobro uneli ")
        continue
    if pokusaj==slovo:
        print("Pogodio si")
    elif pokusaj<slovo:
        print("Uneto slovo je pre trazenog")
    else:
        print("Uneto slovo je posle trazenog")



    