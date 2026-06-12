# list of students
students = ["Rahul", "Priya", "Amit", "Sneha", "Rohan"]


students.append("Ankit")
students.insert(2, "Neha")


students.remove("Amit")
students.pop(3)


students.sort()

print("Sorted List:", students)


students.reverse()
print("Reverse Order:", students)


print("First 3 Students:", students[:3])