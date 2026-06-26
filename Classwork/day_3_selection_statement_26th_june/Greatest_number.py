'''Program to find the greatest number between two numbers using if-else statement'''
#input of first number from user 
num1 = int(input("Enter first number :"))
#input of second number from user
num2 = int(input("Enter second number :"))
#--------------------------------------------
print("---------------------------------------------")
#finding the greatest number between two numbers
if(num1 > num2):
    print(num1,"is the greatest number")
if(num2 > num1):
    print(num2,"is the greatest number")
else:
    print("Both numbers are equal")
#-------------------------------------------------------------
'''Output :
Enter first number :45
Enter second number :78
---------------------------------------------
78 is the greatest number
'''