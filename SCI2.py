def get_input(label, max_digits):
    while True:
        try:
            value_str = input(f"{label}: ")
            if len(value_str) > max_digits:
                print(f"{label} must be at most {max_digits} digits long.")
                continue
            value = float(value_str)
            if value < 0:
                print(f"{label} cannot be negative.")
                continue
            return value
        except ValueError:
            print("Please enter numbers only.")

for i in range(1, 10):
    Budget = get_input("Budget", 6)
    Travel = get_input("Travel", 6)
    Eat    = get_input("Eat", 6)
    Rent   = get_input("Rent", 6)

    Daily = Travel + Eat + Rent
    One_week = Daily * 7
    Remain = Budget - One_week

    if Remain < 0:
        print("Invalid")
    else:
        print("Daily expense: ", Daily)
        print("Weekly expense: ", One_week)
        print("Remain: ", Remain)