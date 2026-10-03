#Shaina Aguon
#10/2/2026
#salary calculator

#request employee info
from typing import override


name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly rate: "))  

#evaluate overtime
if hours > 40:
  #calculate the overtime
 overtime_hours = hours - 40
 #calculate over pay 
 overtime_pay = overtime_hours * rate * (rate * 1.5 )
 #calculate salary for regular hours
 regular_pay = 40 * rate
 #calculate gross pay
 gross_pay = regular_pay + overtime_pay
else:
 overtime_pay = 0
 overtime_hours = 0
 gross_pay = hours * rate
 gross_pay = regular_pay

#display results
print("--------------------------------")
print("Employee Name: ", name)
print('{"hours worked":<15}{"pay rate":<12}{"overtime pay":>12}{"gross pay":>12}{"regular pay":<15}{"gross pay":<12}')
print("--------------------------------")
print(f"{hours:<15}{rate:<12}{overtime_pay:>12}{regular_pay:<15}{gross_pay:<12}")