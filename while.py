def main():
    number = washitong()
    meow(number)

def washitong():
    while True:
        n = int(input("Enter a number: "))
        if n >0:
            return n
def meow(n):
    for i in range (n):
        print("Meow")

main()


Input = input("Enter your name").strip().lower()
name = ['mama', 'harry', 'ron']

if Input in name:
    print("Authorized personel, enter.")
else:
    print("Unauthorized personel, do not enter.")
