#Shaina Aguon
#10/20/2026
#NANCYP4HW2
#salary calculatorwith loop

#request employee info
name = input("Enter employees name or 'done' to finish : ")

#create accumilator variables for overtime pay, regular pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

name = input("Enter employees name or 'Done' to finish : ")

while name != "Done":
    employee_count += 1

    #add employee count plus one
    employee_count += 1 

#ask for employee info
    hours_worked = float(input("how many hours did " + name + " work this week? "))
    rate = float(input("what is " + name + "'s hourly payrate? "))
    
    #evaluate overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours_worked * rate
        gross_pay = regular_pay 
    

    #add to running totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay


        #display results for this employer
    print("---------------------------------")
    print(f"Employee Name: {name}")
    print(f"{'Hours Worked':<15}{'payrate':<15}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
    print("---------------------------------")
    print(f"{hours_worked:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}")

#ask for next employee too continue or loop
    name = input("Enter employees name or 'Done' to finish : ")

    print("total number of employees entered: ", employee_count)
    print("total amount paid for overtime: $", format(overtimepay_total, '.2f'))
    print("total amount paid for regular pay: $", format(regularpay_total, '.2f'))
    print("total amount paid for gross pay: $", format(grosspay_total, '.2f'))