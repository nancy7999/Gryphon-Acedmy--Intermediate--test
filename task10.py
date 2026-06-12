# dictionary of students
students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 21, "marks": 90},
    "Rohan": {"age": 19, "marks": 78}
}


students["Sneha"] = {"age": 20, "marks": 92}

# update marks
students["Rahul"]["marks"] = 88


del students["Rohan"]


if "Priya" in students:
    print("Priya exists")
else:
    print("Priya not found")

print("\nKeys:")
for key in students.keys():
    print(key)

print("\nValues:")
for value in students.values():
    print(value)

print("\nItems:")
for item in students.items():
    print(item)


names_list = list(students.keys())
print("\nStudent Names List:", names_list)