import os


file = open("employees.txt", "w")
file.write("Rahul\n")
file.write("Priya\n")
file.write("Amit\n")
file.close()


print("Original File Data:")
file = open("employees.txt", "r")
print(file.read())
file.close()

file = open("employees.txt", "a")
file.write("Sneha\n")
file.write("Rohan\n")
file.close()


print("Updated File Data:")
file = open("employees.txt", "r")
print(file.read())
file.close()


os.remove("employees.txt")


if os.path.exists("employees.txt"):
    print("File still exists")
else:
    print("File deleted successfully")