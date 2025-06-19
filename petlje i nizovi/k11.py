#Sastaviti funkciju koja vraća zbir svih prostih brojeva u opsegu od 1 do unetog broja.
def prost(n):
    suma=0
    for i in range(2,n+1):
        prost=True
        for j in range(2,i):
            if i%j==0:
                prost= False
                break
        if prost:
            suma+=i
    return suma    
n=int(input("Unesite n: "))
prosti=prost(n)
print(prosti)