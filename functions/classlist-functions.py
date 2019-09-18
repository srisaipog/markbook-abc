from typing import Dict

def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    classroom = {'Coursecode': course_code,
    'Course name': course_name,
    'Period': period
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