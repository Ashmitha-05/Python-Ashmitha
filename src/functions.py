def greet():
    print("Hello, Welcome!")

greet()

def greet(name):
    print("Hello", name)

greet("Ashmitha")
greet("xyz")

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


def multiply(a, b):
    print(a * b)

x = multiply(3, 4)
print("Returned:", x)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

print(add(10, 5))
print(sub(10, 5))
print(mul(10, 5))