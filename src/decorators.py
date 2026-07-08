'''
def wrapper(func):
    def functionality():
        print("Program started")
        func()
        print("program ended")
    return functionality

@wrapper
def greet():
    print("Hello all")

greet()
'''

'''
def wrapper(func):
    def average_func(*args, **kwargs):
        print("program started")
        result = func(*args)
        avg = result / len(args)
        print("program ended")
        return avg
    return average_func

@wrapper
def summation(*args):
    return sum(args)

print(summation(3,4,5))
'''

'''
def wrapper1(func):
    def average_func(*args, **kwargs):
        print("program started during add")
        result = func(*args)
        avg = result / len(args)
        print("program ended during add")
        return avg
    return average_func

def wrapper2(func):
    def mul(*args, **kwargs):
        print("program started during mul")
        result = func(*args)
        multi=result*2
        print("program ended during mul")
        return multi
    return mul

@wrapper1
@wrapper2
def summation(*args):
    return sum(args)

print(summation(3,4,5))
'''


def wrapper1(func):
    def average_func(*args, **kwargs):
        print("program started during add")
        result = func(*args)
        avg = result / len(args)
        print("program ended during add")
        return avg
    return average_func

def wrapper2(func):
    def mul(*args, **kwargs):
        print("program started during mul")
        result = func(*args)
        multi=result*2
        print("program ended during mul")
        return multi
    return mul

@wrapper1
@wrapper2
def summation(*args):
    return sum(args)

print(summation(3,4,5))