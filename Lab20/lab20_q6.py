#student grade report

students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]

total = 0
print("Grades: ")
for name, mark in students:
    if mark >= 90: grade = "A"
    elif mark >= 80: grade = "B"
    elif mark >= 70: grade = "C"
    elif mark >= 60: grade = "D"
    else: grade = "F"
    print(f"{name}: {grade}")
    total += mark

print()
avg = total / len(students)
print(f"Class Average: {avg}")
print()

topscorer, topmark = students[0]
botscorer, botmark = students[0]
for name, mark in students:
    if mark > topmark:
        topmark = mark
        topscorer = name
    if mark < botmark:
        botmark = mark
        botscorer = name
print(f"The top scorer is {topscorer} and the bottom scorer is {botscorer}")



