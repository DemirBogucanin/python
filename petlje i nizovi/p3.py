while True:
    broj=int(input("Unesite broj"))
    if broj<=0:
        break
    if broj%3==0:
        print("Broj je deljiv sa 3")
    else:
        print("Nije")