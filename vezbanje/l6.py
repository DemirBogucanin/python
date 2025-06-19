#Rotacija matrice za 90 stepeni 

n=int(input("Unesite dimenzije matrice: "))
matrica=[]
print("Unesite redove matrice: ")
for i in range(n):
    red=list(map(int,input().split()))
    matrica.append(red)
rotirana=[[matrica[n-i-1][i]for j in range(n) ]for i in range(n)]
print("Rotirana matrica je: ")
for red in matrica:
    print(*red)