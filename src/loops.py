marks = [78, 92, 45, 88, 67, 95, 45, 100, 56, 39]
'''
for i,m in enumerate(marks):
    print(f"mark of {i} : {m}")
total=0
for m in marks:
    total +=m
print(f"{total} and avg is {total/len(marks)}")
'''
'''
for i in range(len(marks)-1,1,-1):
    print(f"{marks[i]}")
'''

#value error
'''
for i in range(10,20,0):
    print(i)
'''

#zip
'''
marks=[90,10,20]
name=['ash']
for marks,name in zip(marks,name):
    print(marks,name)
'''


text = "Python"

reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)