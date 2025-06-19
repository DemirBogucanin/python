#Prosti brojevi u intervalu 

donja = int(input("Unesite donju granicu: "))
gornja = int(input("Unesite gornju granicu: "))

if gornja < 2:  
    print("Nema prostih brojeva u ovom opsegu")
else:
    if donja < 2:
        donja = 2  

    for broj in range(donja, gornja + 1):
        prost = True
        for i in range(2, int(broj ** 0.5) + 1): 
            if broj % i == 0:
                prost = False
                break  

        if prost:
            print(broj) 
