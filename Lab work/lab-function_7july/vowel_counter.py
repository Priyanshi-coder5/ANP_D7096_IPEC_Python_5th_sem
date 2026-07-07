'''Problem Statement 5: Vowel Counter using Function
Write a Python program that defines a function count_vowels(text).
The function should:
---------------------
• Accept a string.
• Count the total number of vowels (a, e, i, o, u) irrespective of case.
• Return the total vowel count.
------------------------------------
The main program should:
• Accept a sentence from the user.
• Call the function.
• Display the total number of vowels.
----------------------------------
Sample Output
Enter a sentence:
Python Programming is Fun
Total Vowels: 6'''
#--------------------------coding----------------------
# Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

# Main program
sentence = input("Enter a sentence: ")
total_vowels = count_vowels(sentence)
print("Total Vowels:", total_vowels)
 
#--------------output---------------------------
'''Enter a sentence:
Python Programming is Fun
Total Vowels: 6'''