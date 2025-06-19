#Pronaći minimum i maksimum u listi od 5 brojeva.

brojevi=list(map(int,input("Unesite brojeve: ").split()))
mini=min(brojevi)
maks=max(brojevi)
print(f"Najmanji element je {mini}, a najveci element je {maks}")