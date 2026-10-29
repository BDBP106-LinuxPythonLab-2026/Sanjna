#extract vowels in a string using list comprehension

string=input("Enter a string: ")
vowels=[v for v in string if v in ["a", "e", "i", "o", "u"]]
print(vowels)

#filter function

print(list(filter(lambda v: v in ["a", "e", "i", "o", "u"],string)))