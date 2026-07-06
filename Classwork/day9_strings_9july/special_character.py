#-------------problem statement------------------
'''Write a python program to take a string from user and count the number of special characters in it.'''

#-------------input from user------------------
sentence = input("Enter a sentence : ")

#-------------initialize a variable to count special characters------------------
special_char = 0

#-------------iterate through each character in the sentence------------------
for x in sentence:
    if not (x.isalnum()):  # Check if the character is not alphanumeric
        special_char += 1


print("No of special characters in the given sentence is : ", special_char)

#-------------output---------------------------
'''Enter a sentence : Hello@World!
No of special characters in the given sentence is :  2
'''