try:
    num = int(input("Enter a number: "))
    print(10 / num)

except:
    print("Something went wrong!")

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Enter numbers only.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", result)

finally:
    print("Execution Completed")