'''Problem Statement 1: Student Grade Calculator
Write a Python program that defines a function calculate_grade(marks).
----------------------------------------------------------
The function should:
• Accept marks (0–100) as a parameter.
• Return the grade according to the following criteria:
o 90 and above → A+
o 75–89 → A
o 60–74 → B
o 40–59 → C
o Below 40 → Fail
------------------------------------------------------------
The main program should:
• Accept marks of 5 students.
• Call the function for each student.
• Display the marks and corresponding grade. '''
#--------------------------coding----------------------
# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# Main program
students = 5  # number of students
for i in range(students):
    marks = int(input(f"Enter marks of student {i+1}: "))
    grade = calculate_grade(marks)
    print(f"Student {i+1} - Marks: {marks}, Grade: {grade}")


#--------------output---------------------------
'''Student 1 - Marks: 95, Grade: A+
Student 2 - Marks: 82, Grade: A
Student 3 - Marks: 67, Grade: B
Student 4 - Marks: 45, Grade: C
Student 5 - Marks: 30, Grade: Fail
'''
