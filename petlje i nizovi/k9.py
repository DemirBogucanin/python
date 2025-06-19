#Sastaviti funkciju koja proverava da li je uneti string palindrom.

def palindrom(string):
    if string==string[::-1]:
        return True
    else:
        return False
unos = input("Unesite string: ")
if palindrom(unos):
    print("String je palindrom.")
else:
    print("String nije palindrom.")