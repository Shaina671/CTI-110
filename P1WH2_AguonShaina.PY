# Shaina Aguon
# September 22, 2026
#p1HW2 
# Description: This program calculates and displays travel expenses based on user input for budget, destination, fuel, accommodation, and food.

#Ask user to enter their budget
budget = float(input("Enter Budget: "))

#Ask user to enter travel destination
destination = input("Enter your travel destination: ")

#Ask user for amount they will spend on gas
gas = float(input("spend on gas? "))

#Ask user for amount they will spend on accommodation
accommodation = float(input(" how much will you need for accomodation/hotel? "))

#Ask user for amount they will spend on food
food = float(input("how much do you need for food? "))

#Add expenses
total_expenses = gas + accommodation + food

#Subtract expenses from budget
remaining_balance = budget - total_expenses

# 10. Display results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {gas}")
print(f"Accomodation: {accommodation}")
print(f"Food: {food}")
print(f"\nRemaining Balance: {remaining_balance}")