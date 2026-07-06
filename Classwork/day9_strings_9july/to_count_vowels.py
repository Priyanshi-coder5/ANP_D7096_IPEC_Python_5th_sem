#----------------problem statement------------------
'''Write a python program to take a string from user and count the number of vowels in it.'''
 #input of sentence 
 sentence = input("Enter a sentence : ")

#initialize a variable to count vowels
vowel_count = 0
for x in sentence:
    if (x=='A' or x=='a' or x=='E' or x=='e' or x=='I' or x=='i' or x=='O' or x=='o' or x=='U' or x=='u'):
        vowel_count += 1
        vowel = vowel +1

print("No of vowels in the given sentence is : ",vowel_count)
 



  

#----------output---------------------------
