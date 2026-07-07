#----------Online Examination Analyzer----------
#  A student appears in 5 subjects.
'''Rules:
 Minimum 40 marks in every subject to pass.
 Distinction → Average ≥ 75
 First Division→ Average ≥ 60
 Second Division → Average ≥ 50
 Pass → Average ≥ 40
 Fail if any subject score < 40
 ----------------------------------
Sample Input
Hindi : 85
English : 78
Mathematics : 82
Science : 75
Computer : 90
----------------------------------
Sample Output
Average Marks: 82.0
Result: PASS
Classification: Distinction
-----------------------------------'''
#----------------code-------------------
# Student Result Evaluation Program

# Input marks for 5 subjects
hindi = int(input("Hindi: "))
english = int(input("English: "))
maths = int(input("Mathematics: "))
science = int(input("Science: "))
computer = int(input("Computer: "))

# Store marks in a list
marks = [hindi, english, maths, science, computer]

# Check if any subject is below 40 → Fail
if any(m < 40 for m in marks):
    result = "FAIL"
    classification = "None"
else:
    # Calculate average
    average = sum(marks) / len(marks)

    # Classification based on average
    if average >= 75:
        classification = "Distinction"
    elif average >= 60:
        classification = "First Division"
    elif average >= 50:
        classification = "Second Division"
    elif average >= 40:
        classification = "Pass"
    else:
        classification = "None"

    result = "PASS"

    # Output
    print("Average Marks:", average)
    print("Result:", result)
    print("Classification:", classification)
#--------output------------
'''
Hindi: 85
English: 78
Mathematics: 82
Science: 75
Computer: 90
--------------------
Average Marks: 82.0
Result: PASS
Classification: Distinction
-----------------------------------'''