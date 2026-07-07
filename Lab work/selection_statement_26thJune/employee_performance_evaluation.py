#-------employee performance evaluation-------

'''An employee is evaluated using
 Project Score
 Attendance Percentage
 Client Feedback Score
Rules:
 Excellent → All scores above 90
 Good → Scores above 75
 Average → Scores above 60
 Poor → Otherwise
 ---------------------------
Additional Rule:
 Attendance below 70% cannot receive more than Average rating.
----------------------------
Sample Input
Project Score: 95
Attendance: 65
Client Feedback: 95
---------------------------'''
#----------------code-------------------
# Employee Performance Evaluation Program

try:
    # Input
    project_score = int(input("Project Score: "))
    attendance = int(input("Attendance Percentage: "))
    feedback_score = int(input("Client Feedback Score: "))

    # Validation
    if not (0 <= project_score <= 100 and 0 <= attendance <= 100 and 0 <= feedback_score <= 100):
        print("Invalid input! Scores and attendance must be between 0 and 100.")
    else:
        # Step 1: Base Rating
        if project_score > 90 and attendance > 90 and feedback_score > 90:
            rating = "Excellent"
        elif project_score > 75 and attendance > 75 and feedback_score > 75:
            rating = "Good"
        elif project_score > 60 and attendance > 60 and feedback_score > 60:
            rating = "Average"
        else:
            rating = "Poor"

        # Step 2: Attendance Rule
        if attendance < 70 and rating in ["Excellent", "Good"]:
            rating = "Average"
            print("Performance Rating:", rating)
            print("Reason: Attendance below 70%")
        else:
            print("Performance Rating:", rating)

except ValueError:
    print("Invalid input! Please enter numeric values.")

#-----------------------output---------------------------
'''
Project Score: 95
Attendance: 65
Client Feedback: 92
--------------------------
Performance Rating: Average
Reason: Attendance below 70%
---------------------------------'''