# to check if two strings are anagrams of each other
s1=input("Enter a string: ")
s2=input("Enter another string: ")
if sorted(s1)==sorted(s2):
    print(s1, "and", s2, "are anagrams.")
else: print(s1, "and", s2, "are not anagrams.")