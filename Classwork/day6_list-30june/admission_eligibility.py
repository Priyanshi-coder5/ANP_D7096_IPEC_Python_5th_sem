#---problem statement-----------------------
'''write a program toccreate alist of masks of 15 students along with there name . display the name of students who are eligibile for the admission  . a students will be eligible if marks is greater than 75'''
 

 #----------coding----------------------------

students = []

print("Enter names and marks of 15 students:")
for i in range(15):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students.append((name, marks))   # store as tuple (name, marks)

print("\nList of students with marks:")
for name, marks in students:
    print(f"{name}: {marks}")

print("\nStudents eligible for admission (marks > 75):")
for name, marks in students:
    if marks > 75:
        print(name)


#---------output-------------------
'''
Enter names and marks of 15 students:
Enter name of student 1: Riya
Enter marks of Riya: 82
Enter name of student 2: Aarav
Enter marks of Aarav: 65
--------------------------------------
Enter name of student 15: Meera
Enter marks of Meera: 90
--------------------------------------
List of students with marks:
Riya: 82
Aarav: 65
----------------------------------
Meera: 90

Students eligible for admission (marks > 75):
Riya
Meera
---------------------------------'''
