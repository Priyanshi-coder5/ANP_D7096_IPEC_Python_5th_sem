#----------------problem statement------------------
'''Write a python program to take a string from user and count the number of vowels in it.'''

#-------------input from user------------------
# Program to count each vowel separately in a string

# Step 1: Take input from user
text = input("Enter a string: ")

# Step 2: Define vowels
vowels = "aeiouAEIOU"

# Step 3: Dictionary to store counts
vowel_count = {"a":0, "e":0, "i":0, "o":0, "u":0}

# Step 4: Count vowels
for ch in text.lower():   # lowercase में convert ताकि case-sensitive न हो
    if ch in vowel_count:
        vowel_count[ch] += 1

# Step 5: Display result
print("Vowel counts in the string:")
for v, c in vowel_count.items():
    print(v, ":", c)



#----------------output---------------------------
'''Enter a string: Hello World
Vowel counts in the string:
a : 0
e : 1
i : 0
o : 2
u : 0
'''
  


