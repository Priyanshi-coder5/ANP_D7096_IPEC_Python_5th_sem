#----------problem statement------------------------
'''create a record of 15 person along with there name and salary . Display the name of person and salary .
 display the name of person who are eligible for ews category 
 A person will be considered in ews category if he salary is below 5 lakhs per annum'''

#---------coding----------------------------


persons = []

print("Enter name and salary of 15 persons:")
for i in range(15):
    name = input(f"Enter name of person {i+1}: ")
    salary = int(input(f"Enter salary of {name} (per annum in INR): "))
    persons.append((name, salary))   # store as tuple (name, salary)

print("\nList of persons with salary:")
for name, salary in persons:
    print(f"{name}: ₹{salary}")

print("\nPersons eligible for EWS category (salary < 5,00,000):")
for name, salary in persons:
    if salary < 500000:
        print(name) 
#-----------------output-------------------
'''
----------------------------------
Enter name and salary of 15 persons:
Enter name of person 1: Ramesh
Enter salary of Ramesh (per annum in INR): 600000
Enter name of person 2: Suresh
Enter salary of Suresh (per annum in INR): 400000
Enter name of person 3: Priya
Enter salary of Priya (per annum in INR): 300000
Enter name of person 4: Anil
Enter salary of Anil (per annum in INR): 700000
Enter name of person 15: Meera
Enter salary of Meera (per annum in INR): 450000\
---------------------------------------
List of persons with salary:
Ramesh: ₹600000
Suresh: ₹400000
Priya: ₹300000  
Anil: ₹700000
Meera: ₹450000
-------------------------------
Persons eligible for EWS category (salary < 5,00,000):
Suresh
Priya
Meera
-------------------------'''



