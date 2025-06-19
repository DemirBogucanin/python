#Prosečna vrednost torke
#Napiši program koji definiše torku brojeva, računa i ispisuje prosečnu vrednost njenih elemenata.

torka=tuple(map(int,input("Unesite torku: ").split()))
prosek=sum(torka)/len(torka)
print(prosek)