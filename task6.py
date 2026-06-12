try:
    # creating file
    file = open("report.txt", "w")
    file.write("Rahul-85\n")
    file.write("Priya-90\n")
    file.write("Rohan-78\n")
    file.write("Sneha-92\n")
    file.write("Amit-65\n")
    file.close()

    
    file = open("report.txt", "r")

    print("Students with marks greater than 80:")
    for line in file:
        name, marks = line.strip().split("-")

        if int(marks) > 80:
            print(name, "-", marks)

    file.close()

except FileNotFoundError:
    print("File not found")

finally:
    print("File operation completed")