"""
(i) Using the join method.
(a) Create a string by joining the numbers in the above list a using the comma.
(b) Create a string by joining the numbers in the above list a using the period.
(c) Create a string by joining the numbers in the above list a using the ‘—’.
(d) Create a new string by first creating a list of squares of the elements in a,
then listing them alongside the elements of a line by line. In other words,
we want a data set that looks like
1 1
2 4
3 9
. . .

(ii) Make a list of 10 people you know, and do the following:
(a) Convert each element in the list to upper case using list comprehension
(b) Swap the first name and surname of each element in the list
(c) Join the first name and surname in each element as ’First.Last’. Note that the first letter of the first name and
first letter of the surname should be upper case.
(iii) Find the longest word in this sentence using list comprehension:
”She sells sea shells that she collects from the sea floor”.
(iv) Create a list of the words that are repeated in the above sentence."""

#(i)
a=[i for i in range(1,51)]
print(a)
#(a)
str1=[",".join(str(i) for i in a)]
print(str1)
#(b)
str2=[".".join(str(i) for i in a)]
print(str2)
#(c)
str3=["-".join(str(i) for i in a)]
print(str3)
#(d)
squares=[x**2 for x in a]
table = "\n".join([" ".join(  [str(a[i]), str(squares[i])]) for i in range(0,len(a))])
print(table)
t1 = [" ".join( [str(a[i]), str(squares[i])]) for i in range(0,len(a))]
print(t1)

# (ii)
names = ["kaumudi mishra", "mahima shukla", "manekha varma", "sneha bhatta", "tanishq kokate", "navya pandey"]
#(a)
upper = [x.upper() for x in names]
print(upper)
#(b)
swap = [f"{last} {first}" for name in names for first, last in [name.split()]]
print(swap)
#(c)
formatted = [f"{first.capitalize()}.{last.capitalize()}" for name in names for first, last in [name.split()]]
print(formatted)

#(iii)
sentence = "She sells sea shells that she collects from the sea floor."
words = sentence.split()
longest_word = [w for w in words if len(w) == max(len(x) for x in words)]
print(longest_word)

#(iv)
repeats = [x for x in words if words.count(x) > 1]
print(set(repeats))

