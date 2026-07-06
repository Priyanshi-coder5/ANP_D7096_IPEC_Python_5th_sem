'''ate a nested dictionary to store marks of students in three subjects.
Example:
{
'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
'Priya': {'Math': 78, 'Science': 95, 'English': 82},
'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}
----------------------------------------------
Write a program to:
• Calculate the total marks of each student.
• Calculate the average marks of each student.
• Display the topper based on total marks.
• Display the subject-wise highest marks along with the student's name.
• Display students whose average is greater than or equal to 85.
----------------------------------------------'''

#-----------coding----------------------
# Lab 3: Student Marks Management

# Step 1: Create nested dictionary
students = {
    'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
    'Priya': {'Math': 78, 'Science': 95, 'English': 82},
    'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}

# Step 2: Calculate total and average marks of each student
print("Total and Average Marks of Each Student:")
totals = {}
for name, subjects in students.items():
    total = sum(subjects.values())
    avg = total / len(subjects)
    totals[name] = total
    print(name, "=> Total:", total, ", Average:", avg)

# Step 3: Display topper based on total marks
topper = max(totals, key=totals.get)
print("\nTopper:", topper, "with", totals[topper], "marks")

# Step 4: Display subject-wise highest marks
print("\nSubject-wise Highest Marks:")
subjects = ['Math', 'Science', 'English']
for sub in subjects:
    highest_student = max(students, key=lambda x: students[x][sub])
    print(sub, "=>", highest_student, ":", students[highest_student][sub])

# Step 5: Display students with average >= 85
print("\nStudents with average >= 85:")
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    if avg >= 85:
        print(name, "=> Average:", avg)

#--------------output---------------------------
'''Total and Average Marks of Each Student:
Rahul => Total: 263 , Average: 87.66666666666667
Priya => Total: 255 , Average: 85.0
Ankit => Total: 274 , Average: 91.33333333333333
Topper: Ankit with 274 marks
Subject-wise Highest Marks:
Math => Ankit : 91
Science => Priya : 95
English => Ankit : 94
Students with average >= 85:
Rahul => Average: 87.66666666666667
Ankit => Average: 91.33333333333333
'''
