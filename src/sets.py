
python_students = {
    "Ash",
    "Bob",
    "Charlie",
    "David",
    "Eva",
    "George"
}

java_students = {
    "Charlie",
    "David",
    "Frank",
    "George",
    "Helen"
}

ai_students = {
    "Bob",
    "Charlie",
    "Eva",
    "Ivy",
    "Jack"
}





print("Python Students :", python_students)
print("Java Students   :", java_students)
print("AI Students     :", ai_students)

print("Python Count :", len(python_students))
print("Java Count   :", len(java_students))
print("AI Count     :", len(ai_students))



if "Ash" in python_students:
    print("Ash is enrolled in Python")
else:
    print("Ash is not enrolled")


python_students.add("xyz")

java_students.update(["Lily", "Mike"])

print("Python :", python_students)
print("Java   :", java_students)



python_students.remove("George")

java_students.discard("Unknown")

print("Python :", python_students)
print("Java   :", java_students)



print("Union")
print(python_students | java_students)

print("\nIntersection")
print(python_students & java_students)

print("\nOnly Python")
print(python_students - java_students)

print("\nOnly Java")
print(java_students - python_students)

print("\nExactly One Course")
print(python_students ^ java_students)



print("All Three Courses")
print(python_students & java_students & ai_students)

print("\nPython and AI")
print(python_students & ai_students)

print("\nJava and AI")
print(java_students & ai_students)

print("\nPython or AI")
print(python_students | ai_students)

print("\nAt Least One Course")
print(python_students | java_students | ai_students)


print("\n----- Part 7 -----")

beginners = {"Ash", "Bob"}

print("Subset :", beginners.issubset(python_students))

print("Superset :", python_students.issuperset(beginners))

new_students = {"Tom", "Jerry"}

print("Disjoint :", python_students.isdisjoint(new_students))



print("\n----- Part 8 -----")

backup = python_students.copy()

backup.add("Zara")

print("Original :", python_students)
print("Backup   :", backup)



new_set = python_students.union(java_students)

print("Original Python")
print(python_students)

print("\nNew Set")
print(new_set)

python_students.update(java_students)

print("\nPython After Update")
print(python_students)



A = {1,2,3,4}
B = {4,3,2,1}

print(A == B)



A = {
    (1,2),
    frozenset({3,4}),
    "Python",
    100,
    True
}

print(A)

