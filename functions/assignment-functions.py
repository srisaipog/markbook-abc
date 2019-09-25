def new_assignment():
    all_assignments = dict()
    
    key_1 = 'assignment_title'
    value_1 = input("Enter the assignment title: ")

    key_2 = 'due date month'
    while True:
        try:
            value_2 = int(input("Enter the month of due date (MM): "))
            if value_2 <= 12 and value_2 >= 1:
                break
            else:
                print("That was not a valid month. Try again.")

        except ValueError:
            print("That was not a valid number. Try again.")

    key_3 = 'due date day'
    while True:
        try:
            value_3 = int(input("Enter the day of due date (DD): "))
            if value_2 == 1 and value_3 <= 31 and value_3 >= 1 :
                break
            elif value_2 == 2 and value_3 <= 28 and value_3 >= 1:
                break
            elif value_2 == 3 and value_3 <= 31 and value_3 >= 1:
                break
            elif value_2 == 4 and value_3 <= 30 and value_3 >= 1:
                break
            elif value_2 == 5 and value_3 <= 31 and value_3 >= 1:
                break
            elif value_2 == 6 and value_3 <= 30 and value_3 >= 1:
                break
            elif value_2 == 7 and value_3 <= 31 and value_3 >= 1:
                break
            elif value_2 == 8 and value_3 <= 31 and value_3 >= 1:
                break
            elif value_2 == 9 and value_3 <= 30 and value_3 >= 1:
                break
            elif value_2 == 10 and value_3 <= 31 and value_3 >= 1:
                break
            elif value_2 == 11 and value_3 <= 30 and value_3 >= 1:
                break
            elif value_2 == 12 and value_3 <= 31 and value_3 >= 1:
                break
            else:
                print("That was not a valid date. Try again.")

            
        except ValueError:
            print("That was not a valid date. Try again.")


    key_4 = 'due date year'
    while True:
        try:
            value_4 = int(input("Enter the year of due date (YYYY): "))
            if value_4 >= 2019:
                break
            else:
                print("That was not a valid year. Try again.")
    
        except ValueError:
            print("That was not a valid number. Try again.")

    key_5 = 'points'
    while True:
        try:
            value_5 = int(input("Enter how much the assignment is out of: "))
            break
        except ValueError:
            print("That was not a valid number. Try again.")

    all_assignments[key_1] = value_1
    all_assignments[key_2] = value_2
    all_assignments[key_3] = value_3
    all_assignments[key_4] = value_4
    all_assignments[key_5] = value_5

    return all_assignments
    
new_assignment()
