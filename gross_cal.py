def salary_computation():
    print ("Salary Computation")
    name = input("Enter Employees name: ").strip().title()
    h_work = float(input("Enter Hours of work per day: "))
    h_rate = float(input("Enter Hourly rate per day: "))

    g_pay = h_work * h_rate

    print (f"\nEmployee name: {name}")
    print (f"Hours of work: {h_work}")
    print (f"Hourly rate: {h_rate}")
    print (f"Gross Pay: {g_pay}")
salary_computation()