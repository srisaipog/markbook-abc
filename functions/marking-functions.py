def drop_lowest_mark(student_marks_list):
    lowest_mark = student_marks_list[0]
    for mark in student_marks_list:
        if mark < lowest_mark:
            lowest_mark = mark
    student_marks_list.remove(lowest_mark)
    return student_marks_list
