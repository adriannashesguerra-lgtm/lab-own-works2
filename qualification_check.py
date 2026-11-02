def scholarship():
    avg_grade = float(input("Enter average grade: "))
    qualification = True if avg_grade >= 90 else False

    print (f"Average grade: {avg_grade}")
    print (f"Scholarship qualification: {qualification}")
scholarship()