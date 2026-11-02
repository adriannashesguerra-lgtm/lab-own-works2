def admission_checker():
    print ("admission checker")
    score = float(input("Enter your score: "))
    interview = input("Enter your interview[True/False]: ").strip().lower()
    interview = True if interview.lower() == "true" else False

    eligible = (score >= 85 and interview) or score >= 90

    print (f"Entrance exam score: {score}")
    print (f"Interview result: {interview}")
    print(f"\nEligible for admission: {eligible}")
admission_checker()
