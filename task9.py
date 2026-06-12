# set with duplicates
set1 = {"Python", "Java", "C++", "Python", "JavaScript", "Java"}

print("Set 1:", set1)


set2 = {"Python", "C", "Java"}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

cities = ("Delhi", "Mumbai", "Bhopal", "Delhi", "Pune")

print("Count of Delhi:", cities.count("Delhi"))
print("Index of Bhopal:", cities.index("Bhopal"))

if "Mumbai" in cities:
    print("Mumbai exists in tuple")
else:
    print("Mumbai not found")


try:
    cities[0] = "Indore"

except TypeError:
    print("Error: Tuple cannot be modified")