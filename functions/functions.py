from typing import Dict

def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    classroom = {'Coursecode': course_code,
    'Course name': course_name,
    'Period': period,
    'Teacher': teacher
    }
    """Creates a classroom dictionary"""
    return {}

def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    pass

def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    pass

def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass



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
            
        except ValueError:
            print("That was not a valid date. Try again.")


    key_4 = 'due date year'
    while True:
        try:
            value_4 = int(input("Enter the year of due date (YYYY): "))
            if value_4 >= 2018:
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

    all_assignments[key_1] = value_1
    all_assignments[key_2] = value_2
    all_assignments[key_3] = value_3
    all_assignments[key_4] = value_4
    all_assignments[key_5] = value_5

    return all_assignments
    
new_assignment()
