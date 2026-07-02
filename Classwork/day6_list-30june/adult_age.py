''' Program to take ages of 18 people, store them in a list,
count how many are eligible for voting, and calculate total age of first 10 people.'''
#---------coding-----------------------

# Step 1: Take input of ages
ages = []
for i in range(18):
    age = int(input(f"Enter age of person {i+1}: "))
    ages.append(age)

# Step 2: Count how many are eligible for voting (age >= 18)
eligible_count = sum(1 for age in ages if age >= 18)

# Step 3: Calculate total age of first 10 people
total_age_first_10 = sum(ages[:10])

# Step 4: Display results
print("\n--- Results ---")
print("List of ages:", ages)
print("Number of people eligible for voting:", eligible_count)
print("Total age of first 10 people:", total_age_first_10)


#----------output-----------------------
'''
Enter age of person 1: 17
Enter age of person 2: 20
Enter age of person 3: 15
Enter age of person 4: 22
Enter age of person 5: 18
Enter age of person 6: 19
Enter age of person 7: 16
Enter age of person 8: 21
Enter age of person 9: 23
Enter age of person 10: 14
Enter age of person 11: 25
Enter age of person 12: 30
Enter age of person 13: 28
Enter age of person 14: 17
Enter age of person 15: 19
Enter age of person 16: 20
Enter age of person 17: 22
Enter age of person 18: 18
--- Results ---
List of ages: [17, 20, 15, 22, 18, 19, 16, 21, 23, 14, 25, 30, 28, 17, 19, 20, 22, 18]
Number of people eligible for voting: 12
Total age of first 10 people: 175
'''
