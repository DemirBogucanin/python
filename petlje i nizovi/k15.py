#Napisati program koji simulira igru "Pogodi broj", gde računar pokušava da pogodi broj koji je korisnik zamislio.

def ping(n):
    if n > 0:
        print("Ping")
        pong(n-1)

def pong(n):
    if n > 0:
        print("Pong")
        ping(n-1)
n = int(input("Unesite broj ponavljanja: "))
ping(n)
