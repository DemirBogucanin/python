#Prekid petlje kada se unese negativan broj

while True:  
    i = int(input("Unesite broj: "))

    if i < 0:
        print("Unet je negativan broj. Prekid programa.")
        break  
    
        