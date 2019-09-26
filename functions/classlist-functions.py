from typing import Dict

def new_classroom():
    classroom = dict()

    key_1 = "coursecode"
    value_1 = input("Enter the course code: ")

    key_2 = "coursename"
    value_2 = input("Enter the course name here: ")

    key_3 = "period"
    while True:
        try:
            value_3 = int(input("Enter class period(1,2,3,4): "))
            if value_3 <= 4 and value_3 >= 1:
                break
            else:
                print("That was not a valid answer. Try again")
        
        except ValueError:
            print("That was not a valid answer. Try again")

    key_4 = "teacher"
    value_4 = input("Enter teacher's name here: ")

    key_5 = "student_list"
    value_5 = []

    key_6 = "Assignment_list"
    value_6 = []

    classroom[key_1] = value_1
    classroom[key_2] = value_2
    classroom[key_3] = value_3
    classroom[key_4] = value_4
    classroom[key_5] = value_5
    classroom[key_6] = value_6

    return classroom
    
new_classroom()


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

