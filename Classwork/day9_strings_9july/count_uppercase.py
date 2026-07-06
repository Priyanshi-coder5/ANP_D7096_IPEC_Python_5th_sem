#----------------------problem statement------------------
'''Write a python program to take a string from user and count the number of uppercase letters in it.'''

#-------------input from user------------------
sentence = input("Enter a sentence : ")

#-------------initialize a variable to count uppercase letters------------------
uppercase = 0

#-------------iterate through each character in the sentence------------------
for x in sentence:
    if x.isupper():  # Check if the character is uppercase
        uppercase += 1


print("No of uppercase letters in the given sentence is : ", uppercase)


#------------output---------------------------
'''Enter a sentence : Hello World!
No of uppercase letters in the given sentence is :  2
'''