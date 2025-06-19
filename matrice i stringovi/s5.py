#Provera anagrama pomoću skupova
def anagram(rec1,rec2):
    return sorted(rec1)==sorted(rec2)
print(anagram("listen", "silent")) 
print(anagram("hello", "world")) 