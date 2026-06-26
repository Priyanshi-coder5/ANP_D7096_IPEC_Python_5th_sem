#-----Problem Statement
'''A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 or
more.
Write a Python program to accept the applicant's monthly salary and display whether they are
eligible to apply for the loan.
----------------------------------------
Sample Input 1
Enter your monthly salary: 45000
--------------------------------
Sample Output 1
Congratulations! You are eligible to apply for the loan.
--------------------------------------
Sample Input 2
Enter your monthly salary: 22000
---------------------------------
Sample Output 2
Sorry! You are not eligible to apply for the loan'''
#----------------code-------------------


try:
    salary = float(input("Enter your monthly salary: ₹"))

    # Validation: salary must be non-negative
    if salary < 0:
        print("Invalid input! Salary cannot be negative.")
    else:
        # Eligibility check
        if salary >= 30000:
            print("Congratulations! You are eligible to apply for the loan.")
        else:
            print("Sorry! You are not eligible to apply for the loan.")

except ValueError:
    print("Invalid input! Please enter a numeric value.")

#-----------------output-------------------------------
'''Enter your monthly salary: ₹25000
Sorry! You are not eligible to apply for the loan.'''

'''Enter your monthly salary: ₹35000
Congratulations! You are eligible to apply for the loan.'''