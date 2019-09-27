def create_student():
    students = dict()

    key_1 = 'first_name'
    value_1 = str(input("Enter the student's first name: "))

    key_2 = 'last_name'
    value_2 = str(input("Enter the student's last name: "))
    
    key_3 = 'gender'
    while True:
        try:
            value_3 = str(input("Enter the student's gender (M/F): "))
            if value_3 == 'M' or value_3 == 'F':
                break
            else:
                print("That was not a valid. Try again.")
               
            
        except ValueError:
            print("That was not a valid. Try again.")

    key_4 = 'student_number'
    while True:
        try:
            value_4 = int(input("Enter the student's student number: "))            
            if value_4 >= 1000000:
                break
            else:
                print("That was not a valid. Try again.")

        except ValueError:
            print("That was not a valid. Try again.")

    key_5 = 'grade'
    while True:
        try:
            value_5 = int(input("Enter the student's grade: "))
            if value_5 <= 13 and value_5 >= 1:
                break
            else:
                print("That was not a valid. Try again.")

        except ValueError:
            print("That was not a valid. Try again.")

    key_6 = 'email'
    value_6 = str(input("Enter the student's email: "))

    key_7 = 'marks'
    value_7 = []

    key_8 = 'comments'
    value_8 = str(input("Enter any comments for the student: "))

    students[key_1] = value_1
    students[key_2] = value_2
    students[key_3] = value_3
    students[key_4] = value_4
    students[key_5] = value_5
    students[key_6] = value_6
    students[key_7] = value_7
    students[key_8] = value_8

    return students

create_student()
