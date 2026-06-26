# Program to calculate cost contribution per participant

# Input: Total Event Cost and Number of Participants
total_cost = float(input("Enter the total event cost: "))
participants = int(input("Enter the number of participants: "))

# Calculate amount per participant
amount_per_participant = total_cost / participants

# Output: Amount per Participant
print("Each participant should pay:", amount_per_participant)

Enter the total event cost: 25000
Enter the number of participants: 25
Each participant should pay: 1000.0
