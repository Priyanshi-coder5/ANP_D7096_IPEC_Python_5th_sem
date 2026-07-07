# cybersecurity login validation 
'''A login system validates:
 Username
 Password
 OTP
Conditions:
 All correct → Login Successful
 Incorrect OTP → Re-enter OTP
 Incorrect Password after 3 attempts → Account Locked
 Incorrect Username → User Not Found
--------------------------------
Sample Input
Username: admin
Password: admin123
OTP: 4567
---------------------------------
Sample Output
Login Successful
Welcome Admin
----------------------------------'''
#----------------code-------------------


# Predefined correct credentials
correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"

# Input
username = input("Username: ").strip()
if username != correct_username:
    print("User Not Found")
else:
    # Password validation with 3 attempts
    attempts = 0
    while attempts < 3:
        password = input("Password: ").strip()
        if password == correct_password:
            # OTP validation
            otp = input("OTP: ").strip()
            if otp == correct_otp:
                print("Login Successful")
                print("Welcome Admin")
                break
            else:
                print("Incorrect OTP. Please re-enter OTP.")
                otp = input("OTP: ").strip()
                if otp == correct_otp:
                    print("Login Successful")
                    print("Welcome Admin")
                    break
                else:
                    print("Login Failed due to incorrect OTP.")
                    break
        else:
            attempts += 1
            if attempts == 3:
                print("Account Locked")
            else:
                print("Incorrect Password. Try again.")
#----------------------output---------------------------
'''
Username: admin
Password: admin123
OTP: 4567
---------------------
Login Successful
Welcome Admin
------------------'''



