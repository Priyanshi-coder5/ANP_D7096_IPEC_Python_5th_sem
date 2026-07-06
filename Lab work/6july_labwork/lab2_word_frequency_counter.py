#------problem statement------------------
'''Program: Word Frequency Counter'''
#----------------------coding----------------------

# Step 1: Take input from user
sentence = input("Enter a sentence: ")

# Step 2: Split sentence into words manually (without libraries)
words = []
word = ""
for ch in sentence:
    if ch == " ":
        if word != "":
            words.append(word.lower())
            word = ""
    else:
        word += ch
if word != "":
    words.append(word.lower())

# Step 3: Create dictionary for frequency
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

# Step 4: Display frequency dictionary
print("\nWord Frequency Dictionary:")
print(freq)

# Step 5: Display most frequently occurring word
max_word = max(freq, key=freq.get)
print("\nMost frequently occurring word:", max_word, "=>", freq[max_word])

# Step 6: Display all words in alphabetical order
print("\nWords in alphabetical order:")
for w in sorted(freq.keys()):
    print(w, ":", freq[w]) 



#----------------------output---------------------------
'''er a sentence: python is easy and python is powerful

Word Frequency Dictionary:
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
------------------------------------------
Most frequently occurring word: python => 2
--------------------------------------
Words in alphabetical order:
and : 1
easy : 1
is : 2
powerful : 1
python : 2
---------------------------------'''
