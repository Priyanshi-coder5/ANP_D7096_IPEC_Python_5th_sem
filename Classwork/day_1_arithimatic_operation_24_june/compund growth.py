# Program to calculate compound growth of savings
# Assuming the amount doubles every year

# Input: Initial Amount and Number of Years
initial_amount = float(input("Enter the initial amount: "))
years = int(input("Enter the number of years: "))

# Calculate final amount (doubles every year)
final_amount = initial_amount * (2 ** years)

# Output: Final Amount
print("Final Amount after", years, "years:", final_amount)

Enter the initial amount: 2500
Enter the number of years: 2
Final Amount after 2 years: 10000.0