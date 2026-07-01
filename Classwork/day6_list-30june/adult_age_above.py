#----------problem statement-----------------------
'''Program to input ages of 15 people and display adults'''


#---------coding-----------------------

ages = []
print("Enter ages of 15 people")

for i in range(15):
    age = int(input(f"Enter age of person {i+1}: "))
    ages.append(age)

print("\nAll ages entered:", ages)

print("Adults (age > 18):")
for age in ages:
    if age > 18:
 
        print(age)


#-----------------output-----------------------
'''--------------------
Enter ages of 15 people 
Enter age of person 1: 15
Enter age of person 2: 20
Enter age of person 3: 25
Enter age of person 4: 30
Enter age of person 5: 17
Enter age of person 6: 19
Enter age of person 7: 22
Enter age of person 8: 16
Enter age of person 9: 18
Enter age of person 10: 21
Enter age of person 11: 23  
Enter age of person 12: 14
Enter age of person 13: 26
Enter age of person 14: 28
Enter age of person 15: 29
All ages entered: [15, 20, 25, 30, 17, 19, 22, 16, 18, 21, 23, 14, 26, 28, 29]
Adults (age > 18):
20
25
30
19
22
21
23
26
28
29
---------------------------'''
