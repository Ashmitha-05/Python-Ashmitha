student = {
    "name": "Ash",
    "age": 20,
    "city": "Bangalore"
}

print(student)
print(student["name"])
print(student.get("age"))

student = {
    "name": "Ashmitha",
    "age": 22,
    "city": "Hosur"
}

del student["city"]

print(student)

numbers = [1, 2, 2, 3, 1, 4, 2]

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print(freq)

marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}

maximum = max(marks.values())

print(maximum)
