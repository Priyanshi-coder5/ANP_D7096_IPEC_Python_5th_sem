# Program to calculate remaining bank balance after withdrawal

# Input: Current Balance and Withdrawal Amount
current_balance = float(input("Enter your current balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))


if withdrawal_amount > current_balance:
    print("Insufficient balance! Withdrawal not possible.")
else:
    remaining_balance = current_balance - withdrawal_amount
    print("Remaining Balance:", remaining_balance)

Enter your current balance: 1000000
Enter the withdrawal amount: 500000
Remaining Balance: 500000.0