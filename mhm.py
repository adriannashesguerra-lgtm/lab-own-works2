# mul loop
num = int(input("Enter an integer value: "))

for i in range(1, num + 1):
    print(i*22)

for i in range(1, num + 1):
    if i % 2 == 1:
        print(i)

# round loop
round = 5

for i in range (1, round+1):
    print (f"Round {i}")
    i+=1

# total score
numsub = int(input("Enter the number of subjects: "))

totscore = 0
for i in range(numsub):
    score = float(input(f"Enter the score {i+1}: "))
    totscore += score

print (f"Score: {totscore}")

# data cleaning task
list1 = ["report.csv", "wow.csv", "ey.py"]

for file in list1:
    clean_list1 = file.strip().lower()

    if not clean_list1.endswith(".csv"):
        continue

    print(clean_list1)

# calcu ng 7
num = int(input("Enter a number: "))

for i in range(1, num+1):
    print (f"7 x {i} = {i * 7}")

# pyramid
row = 6

for i in range(1, row + 1):
    print ("*" * i)

# skipper
weekdays = ['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday", "Sunday"]

for day in weekdays:
    if day in ["Saturday", "Sunday"]:
        continue
    print(f"Working day: {day}")

# for loop
for i in (1, 2, 3):
    print(i)

for i in range (1, 6):
    print (f"Round {i}")
    i += 1

items = ['wow', 'yes', 'omg', 'go']

for item in items:
    print (item)

times = 'python'
for time in times:
    print(time)

# use of range; range (start, stop, step)
for i in range (5):
    print(i)

for i in range (1, 5 + 1):
    print(i)

for i in range (1, 5 + 1, 2):
    print(i)

scores = [80, 50, 60, 75]
total = 0

for score in scores:
    total += score
print(f"Final total: {total}")

files = ['  rePort.csv', ' datA.csv', 'fInal.Txt  ']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(file)

for i in range (1, 11):
    print(f"7 x {i} = {7 * i}")

for i in range (1, 7):
    print("*" * i)

# special loop statements
# break using if-elif-else statement
total_scores = 1
for total_score in range (total_scores):
    score = int(input("Enter your score: "))
    total_score += score
    if total_score >= 90:
        print(f"Your score is {score}.")

    elif total_score >= 80:
        print(f"Your score is {score}.")

    else:
        break
print("Goodbye!")

ft = input("What fruit do you like? ")
fruits = ['banana', 'apple', 'mango', 'grapes']

found = False
for fruit in fruits:
    if ft == fruit:
        found = True
        break
if found:
    print("Fruit name is in fruit list.")
else:
    print("Fruit name not in fruit list.")


print("Goodbye!")

# pass
for i in (1, 2, 3):
    if i ==2:
        pass
    print(i)

days_weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for day in days_weeks:
    if day in ['saturday', 'sunday']:
        continue
    print(day)

res = input("What did you input in your email? ")
emails = [
    'txt',
    'csv',
    'wowie;',
    'xls',
    'xlsx'
]

for email in emails:
    if ';' in email:
        print("An SQL injection detected")
        break
    print(email)

# for-else loop
total_scores = 1
for total_score in range (total_scores):
    score = int(input("Enter your score: "))
    total_score += score
    if total_score >= 90:
        print(f"Your score is {score}.")

    elif total_score >= 80:
        print(f"Your score is {score}.")

    else:
        print("Invalid score.")
        break
else:
    print("Goodbye!")

# match case
country = input("Enter your country: ").strip().title()

if country == 'Philippines':
    print("Welcome to Philippines!")
elif country == 'India':
    print("Welcome to India!")
else:
    print("Invalid country.")

match country:
    case 'Philippines':
        print("Welcome to Philippines!")
    case 'India':
        print("Welcome to India!")
    case _:
        print("Invalid country.")

while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 * num2
        print(result)

    except ValueError:
        print("Invalid input mo.")

    except ZeroDivisionError:
        print("Invalid input.")

    except Exception as e:
        print("Invalid user input", e)

    else:
        print("Thank you for your input.")

    finally:
        print("Program ended")

    prog = input("Do you want to end the program? Y/N ").strip().upper()

    if prog == "Y":
        print("Thank you for your input.")
        break
    else:
        continue
#
# nested loop
for num1 in range(1, 11):
    for num2 in range(1, 11):
        print(num1, num2)