


"""
Markbook Application
Group members: 
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    assignment = {
        'name': name,
        'due': due,
        'points': points
    }
    return assignment


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    classroom = {
        'course_code': course_code,
        'course_name': course_name,
        'period': period,
        'teacher': teacher,
        'student_list': [],
        'assignment_list': []
    }
    return classroom


def create_student(first_name: str, last_name: str, gender: str,
                   student_number: int, grade: int, email: str, comments: str) -> Dict:
    
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "student_number": student_number,
        "grade": grade,
        "email": email,
        "marks": [],
        "comments": comments
    }

    return student


def calculate_average_mark(student: Dict) -> float:
    counter = 0
    for marks in student.keys():
        for mark in student[marks]:
            counter += mark
    return(counter / len(student[marks]))


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

