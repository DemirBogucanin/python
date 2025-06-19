#Suma elemenata iznad glavne dijagonale

n = int(input("Unesite dimenziju matrice: "))

matrica = [list(map(int, input().split())) for _ in range(n)]

suma = 0
for i in range(n):
    for j in range(i, n):  
        if i<j:
            suma+=matrica[i][j]
print("Suma elemenata iznad glavne dijagonale:", suma)
