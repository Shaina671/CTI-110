# Shaina Aguon
# September 22, 2026
# P2LAB2
#using dictionaries

# Create the dictionary with automobile keys and MPG values

car_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

# Get the keys from the dictionary 
car_keys = list(car_mpg.keys())
print(car_keys)

#Get a car from user
selected_car = input("Please select a car from the list above: ")

#Get mpg for the given car 
mpg = car_mpg.get(selected_car)

print(f"the {selected_car} gets {mpg} miles per gallon.")

#Get miles from user 
miles = float(input(f"How many miles did you drive in the {selected_car}? "))
gallons = miles/ mpg

print(f"The {selected_car} uses {gallons:.2f} gallons of gas.")

#calculate
gallons_needed = miles_driven / mpg

#display results
print(f"{gallons_needed} gallon(s) of gas to drive the {selected_car} for {miles_driven} miles.")

gallons = miles / mpg

print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {selected_car} {miles} miles.")



