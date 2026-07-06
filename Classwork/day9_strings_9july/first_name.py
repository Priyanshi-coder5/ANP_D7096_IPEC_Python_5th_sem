#--------------------------problem statement------------------
'''write a program to ask the user to input the move and display the first name of it without using the library method '''
 
 #--------------------------coding----------------------
 

# Step 1: Take input from user
full_name = input("Enter your full name: ")

# Step 2: Extract first name manually
first_name = ""
for ch in full_name:
    if ch == " ":   # space मिलने पर loop रोक देंगे
        break
    first_name += ch

# Step 3: Display result
print("First name is:", first_name)

#------------output---------------------------
'''Enter your full name: John Doe
First name is: John
'''
    