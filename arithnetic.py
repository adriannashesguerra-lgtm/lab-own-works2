from math import prod
from operator import add


def arithmetic_calculator():
    num1 = float(input("enter your first number: "))
    num2 = float(input("enter your second number: "))

    add = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quo = num1 / num2
    rem = num1 % num2

    print (f"First number: {num1}")
    print (f"Second number: {num2}")
    print (f"Sum: {add}")
    print (f"Difference: {diff}")
    print (f"Product: {prod}")
    print (f"Quotiment: {quo}")
    print (f"Remainder: {rem}")
arithmetic_calculator()
