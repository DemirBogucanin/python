#Spajanje i sortiranje torki
# Unos dve torke
torka1 = tuple(map(int, input("Unesite prvu torku: ").split()))
torka2 = tuple(map(int, input("Unesite drugu torku: ").split()))
spojena_torka = tuple(sorted(torka1 + torka2))
print("Sortirana spojena torka:", spojena_torka)
