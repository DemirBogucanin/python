#Napraviti rečnik sa imenima i godinama ljudi i ispisati ih koristeći .items().
ljudi={
    "demir":20,
    "emir":30,
    "emin ":10,
    "dibe":12
    
}
for ime,godine in ljudi.items():
    print(f"{ime} ima {godine} godina")