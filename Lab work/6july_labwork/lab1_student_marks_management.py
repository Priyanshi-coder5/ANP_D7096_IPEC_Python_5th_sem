#---problem statement------------------
'''Write a program to manage student marks using a dictionary. The program should allow adding new students, updating marks, deleting students, and displaying the student with the highest marks.'''


#---coding----------------------
# Step 1: Create dictionary with 5 students
students = {
    "Priya": 85,
    "Aman": 72,
    "Rohit": 90,
    "Sneha": 78,
    "Karan": 88
}

# Step 2: Display all student names and marks
print("All Students and Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Step 3: Add a new student
new_name = input("\nEnter new student name: ")
new_marks = int(input("Enter marks: "))
students[new_name] = new_marks
print("\nAfter adding new student:", students)

# Step 4: Update marks of an existing student
update_name = input("\nEnter student name to update marks: ")
if update_name in students:
    new_marks = int(input("Enter updated marks: "))
    students[update_name] = new_marks
    print(update_name, "marks updated to", new_marks)
else:
    print("Student not found!")

# Step 5: Delete a student by name
delete_name = input("\nEnter student name to delete: ")
if delete_name in students:
    del students[delete_name]
    print(delete_name, "deleted successfully!")
else:
    print("Student not found!")

print("\nRemaining Students:", students)

# Step 6: Display student with highest marks
highest_student = max(students, key=students.get)
print("\nStudent with highest marks:", highest_student, ":", students[highest_student])



#--------------output---------------------------
'''All Students and Marks:
Priya : 85
Aman : 72
Rohit : 90
Sneha : 78
Karan : 88
-----------------------------
Enter new student name: Anjali
Enter marks: 95
After adding new student: {'Priya': 85, 'Aman': 72, 'Rohit': 90, 'Sneha': 78, 'Karan': 88, 'Anjali': 95}'''
