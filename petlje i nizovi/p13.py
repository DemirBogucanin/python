#Zamijeniti sve samoglasnike u stringu sa *.
tekst = input("Unesite tekst: ")
samoglasnici = "aeiouAEIOU"
novi_tekst = ""

for slovo in tekst:
    if slovo in samoglasnici:
        novi_tekst += "*"
    else:
        novi_tekst += slovo

print(novi_tekst)

