def grade_calculator(score):
    print ("Welcome to the Grade Calculator")
    num_subjects = int(input("Enter the number of subjects: "))

    total_score = 0
    for i in range (num_subjects):
        score = float(input(f"Enter your score {i+1}:  "))
        total_score += score
    average_score = round(total_score / num_subjects, 2)
    print ("Your average score is", average_score)

    #Determine the classification of grades according to the average score

    if average_score >= 90:
        print ("Congratulations! You are entitled to receive an academic excellence award")

    elif average_score >= 85:
        print ("Good job! But, lets aim for an academic excellence award next time")

    else:
        print ("You may want to do some adance reading now to catch up, you can do it")

# Run the grade calculator function
grade_calculator(85)


def grade_calculator():
    print ("Welcome to the Grade Calculator")
    num_subjects = int(input("Enter the number of subjects: "))
    scores = []
    for i in range (num_subjects):
        score = float(input(f"Enter your score {i+1}:  "))
        scores.append(score)
    average_score = avg_cal(scores)
    print("Your average score is: ", average_score)
    if average_score >= 90:
        print("Congratulations! You are entitled to receive an academic excellence award")

    elif average_score >= 85:
        print("Good job! But, lets aim for an academic excellence award next time")

    else:
        print("You may want to do some adance reading now to catch up, you can do it")

def avg_cal(n):
    return round(sum(n) / len(n), 2)



grade_calculator()


while True:
    print("Welcome to the Grade Calculator")
    num_subjects = int(input("Enter the number of subjects: "))
    scores = []
    for i in range (num_subjects):
        score = float(input(f"Enter your score {i+1}:  "))
        scores.append(score)
    avg_score = round(sum(scores) / len(scores), 2)

    print(f"Your average score is: {avg_score:.2f}")
    if avg_score >= 90:
        print("A")
    elif avg_score >= 85:
        print("B")
    elif avg_score >= 75:
        print("C")
    elif avg_score <= 0:
        print("grade cannot be zero or negative ")
        continue
    else:
        print("F")
        break