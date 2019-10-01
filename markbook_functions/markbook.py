"""
Markbook Application
Group members: Matthew, Max, Sarah, Sridhar
"""

import json
import functions

option = ""

option_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
option_functions = [new_classroom(), create_classroom(), add_student_to_classroom(),
                    remove_student_from_classroom(), edit_student(), create_assignment(),
                    drop_lowest_mark(), average_of_marks(), create_student(),
                    calculate_average_mark(), edit_student()]

options = {}

for i in range(len(option_functions)):
    options[option_letters[i]] = option_functions[i]

while True:
    to_leave = None
    option = input("What option would you like to choose? ('done' to exit) ").strip()

    for i in range(len(option_functions)):
        print(option_letters[i] + ": " + str(option_functions[i]))

    if option == "done":
        break

    if option in option_letters:
        if option_letters.index(option) < len(option_functions):
            to_leave = option_functions[option_letters.index(option)]
    else:
        print("Please input a valid option")

    if to_leave is not None:
        with open("data.json", 'w') as u:
            json.dump(to_leave, u)
    else to_leave is None:
        with open("data.json", 'r') as v:
            json.load(to_leave, v)
