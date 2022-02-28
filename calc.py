from math import *


def power(x, y):
    counter = 1
    temp = x
    while counter < y:
        x = x*temp
        counter = counter + 1
    return x


def mode(x, y):
    result = floor(x/y)
    result = result * y
    result = x - result
    return result


num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

op = input("Type which operation you want to do: \n+\n-\n/\n*\n%\n^\nEnter:  ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "%":
    print(mode(num1, num2))
elif op == "^":
    print(power(num1, num2))
else:
    print("Invalid Operator")
