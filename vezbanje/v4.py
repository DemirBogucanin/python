#Preskakanje parnih brojeva

n=int(input("Unesite broj"))
for i in range(1,n+1):
    if i%2==0:
        continue
    else:
        print(i,end=" ")