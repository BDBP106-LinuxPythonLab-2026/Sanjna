# course enrollment analysis

python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]

p=set(python_class)
print(f"{p} are enrolled in the python class")
j=set(java_class)
print(f"{j} are enrolled in the java class")

print(f"The students taking both classes are: {p.intersection(j)}")
print(f"The students taking only Python are: {p.difference(j)}")
print(f"The students taking only one course are: {(p|j)-(p.intersection(j))}")
print(f"List of every unique student, sorted: {sorted(p|j)}")

name=input("Enter a name: ")
if name in (j.intersection(p)): print("Enrolled in the python and java course")
elif name in p: print("Enrolled in the python course")
elif name in j: print("Enrolled in the java course")
else: print("Not enrolled in any course")



