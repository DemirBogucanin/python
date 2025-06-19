#Prepoznavanje HTML tagova

import re

patern=r"</?[\w]+>"
html=input("Unesite html tag: ")
if re.match(patern,html):
    print("hrml taj je prepoznat")
else:
    print("Pak nije")