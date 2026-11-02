Loop - while loop
while - habang (there is a condition [true or false]). kapag ang condition ay true, maglu loop yung program.

create a program na magbibilang from 1-5
i = 1

while i <= 5:
    print(i)
    i += 1

# infinite loop
"""How to do infinite loop and how to stop them"""

# # intentional
# while True:
#     print("ayooooooo")

use a stopper in the infinite loop
while True:
    i = int(input("what is the value of i? "))
    print(i)
    ans = input("Type exit ")
    if ans == "exit":
        break

# how to do break and continue
"""
break - stop the loop early
continue - skip a part/continue to the another step
"""

i = 1

while i <= 10:
    if i == 5:
        break

    print(i)
    i += 1


i = 0
while i <= 10:
    i += 1

    if i == 5:
        continue
    print(i)