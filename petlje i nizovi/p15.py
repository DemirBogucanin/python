#Ispisati brojeve Fibonaccijevog niza do n.

n=int(input("Unesite broj: "))
a=0
b=1
while a<=n:
    print(a,end=" ")
    a,b=b,a+b