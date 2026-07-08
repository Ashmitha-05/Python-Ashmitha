'''
numbers = [10, 20, 30, 40]
print(numbers)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # first element
print(fruits[-1])  # last element

nums = [1, 2, 3]
nums[1] = 99
print(nums)

nums = (10, 20, 20, 30)
print(nums.count(20))
print(nums.index(30))

a=[1,2,3]
b=a
b.append(4)
print(a)
'''

'''
num_list=[8,7,5,2,9,3,4,1,5,7]
large=float("-inf")
small=float("inf")
largest=[(large := n) for n in num_list if n>large]
smallest=[(small := n) for n in num_list if n<small]
avg= sum(num_list)/len(num_list)
print(f" largest: {large}, smallest: {small}, avg: {avg}")
'''
'''
num_list=[1,2,2,3,1,4]
dup=[]
for n in num_list:
    if n not in dup:
        dup.append(n)
print(dup)
'''

'''
num_list=[1,2,1,3,2,1]
d={}
for n in num_list:
    if n in d:
        d[n]+=1
    else:
        d[n]=1
print(d)
'''

'''
a = [1,2,3,4,5]
b = [4,5,6,7]
aa=set(a)
bb=set(b)
common=aa & bb
aaa=aa-bb
bbb=bb-aa
print(f"common: {list(common)}, a elements: {list(aa)}, b elements: {list(bb)}")
'''

'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
'''

a=5
b=6
print(int.__add__(a,b))
print(str.__add__(a,b))