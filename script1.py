def profile_builder():
    print("Welcome to your Profile builder"
          " wherein you can build your profile whatever you want")

    name = input("Let's start! First, what is your name? ").strip().title()
    age = int(input("Next, what is your age? "))
    if age >= 18:
        print("Gurang kana gago.")
    else:
        print("Wow minor.")

    course = input("What is your current course? ").strip().upper()
    dream = input("What is your current dream? ").strip().upper()

    print(f"\n=========Profile=========")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Dream: {dream}")
profile_builder()