#Implementirati simulaciju bacanja kockica dok ne dobijemo šest šestica zaredom.
import random

broj_sestica = 0
bacanja = 0

while broj_sestica < 6:
    bacanje = random.randint(1, 6)
    bacanja += 1
    if bacanje == 6:
        broj_sestica += 1
    else:
        broj_sestica = 0

print(f"Potrebno je {bacanja} bacanja da se dobiju šest šestica zaredom.")
