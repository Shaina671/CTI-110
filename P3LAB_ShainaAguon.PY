# CTI-110
# P3LAB - Vending Machine / Change Counter
# Shaina Aguon

money_float = float(input("Enter the amount of money you have: "))
total_cents = int(round(money_float * 100))

print(f"DEBUG: total_cents = {total_cents}")

if total_cents == 0:
 print("no change")

dollars = total_cents // 100
total_cents %= 100

quarters = total_cents // 25
total_cents %= 25

dimes = total_cents // 10
total_cents %= 10

nickels = total_cents // 5
total_cents %= 5

pennies = total_cents

if dollars == 1:
 print(f"{dollars} dollar")    
elif dollars > 1:
 print(f"{dollars} dollars") 

if quarters == 1:
 print(f"{quarters} quarter")      
elif quarters > 1:
 print(f"{quarters} quarters")

if dimes == 1:
 print(f"{dimes} dime")      
elif dimes > 1:
 print(f"{dimes} dimes") 

if nickels == 1:
 print(f"{nickels} nickel")      
elif nickels > 1:
 print(f"{nickels} nickels") 

if pennies == 1:
 print(f"{pennies} penny")      
elif pennies > 1:
 print(f"{pennies} pennies") 