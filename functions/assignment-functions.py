def new_assignment():
    add_assignment = dict()
    
    key_1 = 'assignment_title'
    value_1 = input("Enter the assignment title: ")

    key_2 = 'due date month'
    while True:
        try:
            value_2 = int(input("Enter the month of due date (MM): "))
            if value_2 <= 12:
                break
        except ValueError:
            print("That was not a valid number. Try again.")

    key_3 = 'due date day'
    while True:
        try:
            value_3 = int(input("Enter the day of due date (DD): "))
            if value_2 == 1 and value_3 <= 31:
                break
            elif value_2 == 2 and value_3 <= 28:
                break
            elif value_2 == 3 and value_3 <= 31:
                break
            elif value_2 == 4 and value_3 <= 30:
                break
            elif value_2 == 5 and value_3 <= 31:
                break
            elif value_2 == 6 and value_3 <= 30:
                break
            elif value_2 == 7 and value_3 <= 31:
                break
            elif value_2 == 8 and value_3 <= 31:
                break
            elif value_2 == 9 and value_3 <= 30:
                break
            elif value_2 == 10 and value_3 <= 31:
                break
            elif value_2 == 11 and value_3 <= 30:
                break
            elif value_2 == 12 and value_3 <= 31:
                break
        except ValueError:
            print("That was not a valid date. Try again.")


    key_4 = 'due date year'
    while True:
        try:
            value_4 = int(input("Enter the year of due date (YYYY): "))
            if value_4 <= 2100:
                break
        except ValueError:
            print("That was not a valid number. Try again.")

    key_5 = 'points'
    while True:
        try:
            value_5 = int(input("Enter how much the assignment is out of: "))
            break
        except ValueError:
            print("That was not a valid number. Try again.")

    add_assignment[key_1] = value_1
    add_assignment[key_2] = value_2
    add_assignment[key_3] = value_3
    add_assignment[key_4] = value_4
    add_assignment[key_5] = value_5

    return add_assignment
    
