# rounding off numbers using round and f string
x = float(input("Value 1: "))
y = float(input("Value 2: "))

ans = round(x + y, 2)
anss = x + y
print(ans)
print(f"{anss:.2f}")

# defining your function
def hello(to):
    print("hello,", to)

name = input("Enter your name: ")
hello(name)

def hello(to="world"):
    print("hello,", to)

name = input("Enter your name: ")
hello(name)
hello()

def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

# return function
def main():
    x = int(input("Enter a number: "))
    print("x squared is:", square(x))

def square(x):
    return pow(x, 2)

main()

