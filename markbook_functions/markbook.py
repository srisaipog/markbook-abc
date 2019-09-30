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
  option = input("What option would you like to choose?")

