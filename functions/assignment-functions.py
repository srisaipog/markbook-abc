def create_assignment():
    all_assignments = dict()
    
    key_title = 'assignment_title'
    value_title = input("Enter the assignment title: ")

    key_date = 'due date'
# input month
    while True:
        try:
            value_month = int(input("Enter the month of due date (MM): "))
            if value_month <= 12 and value_month >= 1:
                break
            else:
                print("That was not a valid month. Try again.")

        except ValueError:
            print("That was not a valid number. Try again.")

# input date
    while True:
        try:
            value_day = int(input("Enter the day of due date (DD): "))
            if value_month == 1 and value_day <= 31 and value_day >= 1 :
                break
            elif value_month == 2 and value_day <= 28 and value_day >= 1:
                break
            elif value_month == 3 and value_day <= 31 and value_day >= 1:
                break
            elif value_month == 4 and value_day <= 30 and value_day >= 1:
                break
            elif value_month == 5 and value_day <= 31 and value_day >= 1:
                break
            elif value_month == 6 and value_day <= 30 and value_day >= 1:
                break
            elif value_month == 7 and value_day <= 31 and value_day >= 1:
                break
            elif value_month == 8 and value_day <= 31 and value_day >= 1:
                break
            elif value_month == 9 and value_day <= 30 and value_day >= 1:
                break
            elif value_month == 10 and value_day <= 31 and value_day >= 1:
                break
            elif value_month == 11 and value_day <= 30 and value_day >= 1:
                break
            elif value_month == 12 and value_day <= 31 and value_day >= 1:
                break
            else:
                print("That was not a valid date. Try again.")
    
        except ValueError:
            print("That was not a valid date. Try again.")

# input year
    while True:
        try:
            value_year = int(input("Enter the year of due date (YYYY): "))
            if value_year >= 2019:
                break
            else:
                print("That was not a valid year. Try again.")
    
        except ValueError:
            print("That was not a valid number. Try again.")

    key_points = 'points'
    while True:
        try:
            value_points = int(input("Enter how much the assignment is out of: "))
            break
        except ValueError:
            print("That was not a valid number. Try again.")

    all_assignments[key_title] = value_title
    all_assignments[key_date] = f"{value_year} - {value_month} - {value_day}"
    all_assignments[key_points] = value_points

    return all_assignments
    
create_assignment()
