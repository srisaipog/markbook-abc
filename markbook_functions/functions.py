from typing import Dict
from data import classroom


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

# new_classroom()


def create_classroom(course_code: str, course_name: str, period: int, teacher: str, student_list: list) -> Dict:
    classroom = {'Coursecode': course_code,
                 'Course name': course_name,
                 'Period': period,
                 'Teacher': teacher
                 'Students': student_list
                 }
    """Creates a classroom dictionary"""
    return classroom


def add_student_to_classroom(student, classroom):
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    return classroom['students'].append(student)


def remove_student_from_classroom():

    first_name = input("Enter first name of student you wish to remove: ")
    last_name = input("Enter last name of student you wish to remove: ")
    student_list = classroom["student_list"]
    student_found = False

    for i in range(len(student_list)):
        if first_name in student_list[i]["first_name"]:
            if last_name in student_list[i]["last_name"]:
                del student_list[i]
                student_found = True
                break

    if student_found is False:
        print("Student name cannot be found")
    return classroom


def edit_student(student: Dict, **kwargs: Dict):
    for key, value in kwargs.items():
        student[key] = value
    return student"""Edits the student's info with the provided key/value pairs"""


def create_assignment():
    all_assignments = dict()

    key_title = 'assignment_title'
    value_title = input("Enter the assignment title: ")

    key_date = 'due date'
# input month
    while True:
        try:
            value_month = int(input("Enter the month of due date (MM),(enter 0 for no due date):"))
            if value_month <= 12 and value_month >= 0:
                break
            else:
                print("That was not a valid month. Try again.")

        except ValueError:
            print("That was not a valid number. Try again.")

    if value_month == 0:
        value_month = None
        value_day = None
        value_year = None
    else:
        # input date
        while True:
            try:
                value_day = int(input("Enter the day of due date (DD): "))
                if value_month == 1 and value_day <= 31 and value_day >= 1:
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
            value_points = int(input("Enter how much the assignment is out of:"))
            break
        except ValueError:
            print("That was not a valid number. Try again.")

    all_assignments[key_title] = value_title
    if value_month is None:
        all_assignments[key_date] = None
    else:
        all_assignments[key_date] = f"{value_year} - {value_month} - {value_day}"
    all_assignments[key_points] = value_points

    return all_assignments


def drop_lowest_mark(student_marks_list):
    lowest_mark = student_marks_list[0]
    for mark in student_marks_list:
        if mark < lowest_mark:
            lowest_mark = mark
    student_marks_list.remove(lowest_mark)
    return student_marks_list


def average_of_marks(marks_list):
    mark_count = 0
    for mark in marks_list:
        global mark_total
        mark_count += 1
        mark_total = sum(marks_list)
    mark_average = round(mark_total/mark_count, 1)
    return mark_average


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


def calculate_average_mark(student: Dict) -> float:
    counter = 0
    for marks in student.keys():
        for mark in student[marks]:
            counter += mark
    return(counter / len(student[marks]))


def edit_student(student: Dict, **kwargs: Dict):
    for key, value in kwargs.items():
        student[key] = value
    return student

def save(new_data):
    with open('data.json', 'w') as f:
        json.dump(new_data, f)
