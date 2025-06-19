#spis glavne dijagonale matrice

n=int(input("Unesite dimenziju: "))
matrica=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    print(matrica[i][i], end=" ")