def logical_evaluator():
    val1 = input("enter first value [true/false]").strip().lower()
    val2 = input("enter second value [true/false]").strip().lower()

    val1 = True if val1 == "true" else False
    val2 = True if val2 == "true" else False

    print (f"AND: {val1 and val2}")
    print (f"OR: {val1 or val2}")
    print (f"NOT First value: {not val1}")
logical_evaluator()