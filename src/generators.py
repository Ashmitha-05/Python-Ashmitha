'''
def num(*args):
    for i in args:
        yield i

result= num(1,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,1,2,3,4,4)
print(result)
print(next(result))
print(next(result))
for i in result:
    print(i)
'''

'''
def fruits():
    yield "Apple"
    yield "Banana"

def vegetables():
    yield "Carrot"
    yield "Potato"

def food():
    yield from fruits()
    yield from vegetables()

for i in food():
    print(i)
'''

def gen():
    print("gen started")
    y=yield
    print(f"gen ended with {y}")

g=gen()
next(g)
g.send(100)
