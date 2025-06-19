#Sastaviti funkciju koja prima string i vraća ga ispisanog unazad.

def string(s):
    return s[::-1]

s=input("Unesite string: ")
print(string(s))