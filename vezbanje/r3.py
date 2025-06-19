#. Izuzetak za deljenje sa nulom:

try:
    broj=int(input("Unesite broj: "))
    deljenje=broj/int(input("Unesite broj za deljenje: "))
except ZeroDivisionError:
    print("Deljenje nulom nije dozvoljeno")
except ValueError:
    print("Nije broj")