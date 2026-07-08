from functools import reduce

def operation(func, value):
    return func(value)

square = lambda x: x ** 2

print(operation(square, 5))

add = lambda a, b: a + b
largest = lambda a, b: a if a > b else b

print(add(10, 20))
print(largest(15, 25))

nums = [1, 2, 3, 4, 5]

print(list(map(lambda x: x ** 2, nums)))
print(list(map(lambda x: x * 2, nums)))

print(list(filter(lambda x: x % 2 == 0, nums)))
print(list(filter(lambda x: x > 3, nums)))

print(reduce(lambda a, b: a + b, nums))
print(reduce(lambda a, b: a * b, nums))

a = [1, 2, 3]
b = [4, 5, 6]

print(list(map(lambda x, y: x + y, a, b)))

students = [
    ("Ash", 85),
    ("John", 70),
    ("Sara", 95),
    ("Bob", 80)
]

print(sorted(students, key=lambda x: x[1]))