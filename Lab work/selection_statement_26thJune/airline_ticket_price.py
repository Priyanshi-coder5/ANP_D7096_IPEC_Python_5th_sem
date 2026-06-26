#------Problem Statement----------
'''An airline calculates ticket fare using:
Base Fare = ₹5000
Additional Charges:
• Business Class → +₹3000
• Window Seat → +₹500
• Weekend Travel → +₹1000
Discounts:
• Age below 12 → 50%
• Age above 60 → 20%
Calculate the final ticket fare.
--------------------------------
Sample Input
Enter Passenger Age: 65
Business Class (Y/N): Y
Window Seat (Y/N): Y
Weekend Travel (Y/N): Y
--------------------------------
Sample Output
Base Fare: ₹5000
Additional Charges: ₹4500
Senior Citizen Discount: 20%
Final Ticket Fare: ₹7600.0 
--------------------------------'''
#----------------code-------------------


try:
    age = int(input("Enter Passenger Age: "))
    business_class = input("Business Class (Y/N): ").strip().upper()
    window_seat = input("Window Seat (Y/N): ").strip().upper()
    weekend_travel = input("Weekend Travel (Y/N): ").strip().upper()

    # Step 1: Base fare
    base_fare = 5000
    print("Base Fare: ₹", base_fare)

    # Step 2: Additional charges
    additional_charges = 0
    if business_class == "Y":
        additional_charges += 3000
    if window_seat == "Y":
        additional_charges += 500
    if weekend_travel == "Y":
        additional_charges += 1000

    print("Additional Charges: ₹", additional_charges)

    # Step 3: Total before discount
    total_fare = base_fare + additional_charges

    # Step 4: Discounts
    discount_percent = 0
    if age < 12:
        discount_percent = 50
        print("Child Discount: 50%")
    elif age > 60:
        discount_percent = 20
        print("Senior Citizen Discount: 20%")

    # Apply discount
    discount_amount = (total_fare * discount_percent) / 100
    final_fare = total_fare - discount_amount

    # Step 5: Final output
    print("Final Ticket Fare: ₹", final_fare)

except ValueError:
    print("Invalid input! Please enter numeric values for age.")
#----------------------output---------------------------
'''Enter Passenger Age: 65
Business Class (Y/N): Y
Window Seat (Y/N): Y
Weekend Travel (Y/N): Y
Base Fare: ₹ 5000
Additional Charges: ₹ 4500
Senior Citizen Discount: 20%
Final Ticket Fare: ₹ 7600.0'''
