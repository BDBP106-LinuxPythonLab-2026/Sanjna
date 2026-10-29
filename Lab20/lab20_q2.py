# vowel and consonant counter
string=input("Enter text: ")
v=0
c=0
d=0
s=0
for i in string:
    if i.isnumeric(): d+=1
    elif i.isspace(): s+=1
    elif i.isalpha():
            if i.lower() in ["a","e","i","o","u"]: v+=1
            else: c+=1

print(f"Vowels:{v} Consonants:{c} Digits:{d} Spaces:{s}")

