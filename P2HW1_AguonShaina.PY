# Shaina Aguon
# September 22, 2026
# P2HW1
# This program calculates and displays travel expenses with neatly formatted alignment.

# Get inputs from the user
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display formatted travel expenses
print("\n------------Travel Expenses------------")
print(f"{'Location:':<18} {destination}")
print(f"{'Initial Budget:':<18} ${budget:,.2f}")
print(f"{'Fuel:':<18} ${gas:,.2f}")
print(f"{'Accomodation:':<18} ${accommodation:,.2f}")
print(f"{'Food:':<18} ${food:,.2f}")
print("---------------------------------------")
print(f"\nRemaining Balance: ${remaining_balance:,.2f}")