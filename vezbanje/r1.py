#Prepoznavanje broja telefon
 
import re

patern=r"\(\d{3}\) \d{3}-\d{4}"
broj="(123) 456-8743"
if re.match(patern,broj):
    print("Broj telefona je u ispravnom formatu")
else:
    print("Pak nije")