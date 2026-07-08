'''
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)


def divide(a,b):
    try:
        c=a/b
        logging.warning(f"division Completed sucessfully")
        return c
    except Exception as e:
        logging.exception(f"Code Wrong: {e}")
        return


a=int(input("enter no1: "))
b=int(input("enter no2: "))
logging.info(f"divide {a} by {b}")
result=divide(a,b)
'''

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("app.log", mode="a")
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def add(a, b):
    logger.info("Addition Started")
    result = a + b
    logger.info(f"Result = {result}")
    return result


def subtract(a, b):
    logger.info("Subtraction Started")
    result = a - b
    logger.info(f"Result = {result}")
    return result


def multiply(a, b):
    logger.info("Multiplication Started")
    result = a * b
    logger.info(f"Result = {result}")
    return result


def divide(a, b):
    logger.info("Division Started")
    try:
        result = a / b
        logger.info(f"Result = {result}")
        return result
    except ZeroDivisionError:
        logger.exception("Cannot Divide by Zero")


logger.info("Calculator Started")

try:
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))

    logger.debug(f"User Entered: a={a}, b={b}")

    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = int(input("Enter Choice: "))

    logger.debug(f"Choice = {choice}")

    if choice == 1:
        print(add(a, b))

    elif choice == 2:
        print(subtract(a, b))

    elif choice == 3:
        print(multiply(a, b))

    elif choice == 4:
        print(divide(a, b))

    else:
        logger.warning("Invalid Choice")

except Exception:
    logger.exception("Unexpected Error")

logger.info("Calculator Closed")