
'''Problem Statement 3: Password Strength Checker
Write a function check_password(password) that checks whether a password is strong.
A password is considered Strong if:
• It contains at least 8 characters.
• It contains at least one uppercase letter.
• It contains at least one lowercase letter.
• It contains at least one digit.
--------------------------------------
The function should return:
• "Strong Password" or
• "Weak Password"
The main program should accept a password from the user and display the result.
---------------------------'''

#--------------------------coding----------------------
# Function to check password strength
def check_password(password):
    # Condition 1: At least 8 characters
    if len(password) < 8:
        return "Weak Password"

    # Condition 2: At least one uppercase
    has_upper = any(ch.isupper() for ch in password)

    # Condition 3: At least one lowercase
    has_lower = any(ch.islower() for ch in password)

    # Condition 4: At least one digit
    has_digit = any(ch.isdigit() for ch in password)

    # Final check
    if has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"


# Main program
password = input("Enter a password: ")
result = check_password(password)
print("Password Strength:", result)


#----------------------output----------------------------
'''Enter a password: hello123
Password Strength: Weak Password'''
