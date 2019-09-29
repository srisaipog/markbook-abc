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
