#Ispis matrice red po red
n,m=map(int,input("Unesite n i m: ").split())
matrica=[list(map(int,input().split())) for _ in range(n)]
for red in matrica:
    print(*red)