


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
    classroom['student_list'].append(student)


def remove_student_from_classroom(student: Dict, classroom: Dict):
    classroom['student_list'].remove(student)


def edit_student(student: Dict, **kwargs: Dict):
    for key, value in kwargs.items():
        student[key] = value
    return student
