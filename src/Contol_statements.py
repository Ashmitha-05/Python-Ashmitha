'''
Accept an integer from the user and determine:

Whether it is Positive, Negative, or Zero.
'''
'''
no=int(input("enter a no: "))
if no>0 or no<0:
    if no>0 and no%2==0:
        print("positive and even")
    elif no>0 and no%2!=0:
        print("positive and odd")
    elif no<0 and no%2==0:
        print("negative and even")
    else:
        print("negative and odd")
else:
    print("Zero")
'''
#ternary
no=int(input("enter a no: "))
result= "even" if no%2==0 else "odd"
print(result)

#multiple ternary
'''
marks = int(input())

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"
'''

marks=int(input())
result= (
    "A" if marks>=90
    else "B" if marks>=75 and marks<90
    else "C " if marks>=50 and marks<75
    else "fail"
)
print(result)