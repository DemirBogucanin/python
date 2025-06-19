#Implementirati jednostavan kalkulator sa operacijama +, -, *, /.
def kalkulator():
    operacija = input("Unesite operaciju (+, -, *, /): ")
    broj1 = float(input("Unesite prvi broj: "))
    broj2 = float(input("Unesite drugi broj: "))

    if operacija == "+":
        print(f"Rezultat: {broj1 + broj2}")
    elif operacija == "-":
        print(f"Rezultat: {broj1 - broj2}")
    elif operacija == "*":
        print(f"Rezultat: {broj1 * broj2}")
    elif operacija == "/":
        if broj2 != 0:
            print(f"Rezultat: {broj1 / broj2}")
        else:
            print("Greška! Deljenje sa nulom.")
    else:
        print("Nepoznata operacija.")

kalkulator()
