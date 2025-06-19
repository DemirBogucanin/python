broj=int(input("Unesite broj"))
if (broj%3==0) and (broj%5==0):
    print("Broj je deljiv sa 5 i 3")
elif(broj%3==0) or (broj%5==0):
    print("Deljiv sa jednim od brojeva")
else:
    print("Broj nije deljiv ni sa jednim brojem")
