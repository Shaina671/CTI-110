# Shaina Aguon
# September 22, 2026
# P2HW2
# This program asks the user for six grades, stores them in a list, and calculates the lowest, highest, sum, and average.

# Get the grades from the user
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Store the grades in a list
grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Calculate required results
lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average = sum_grades / len(grades)

# Format output to match sample exactly
print()
print("-" * 18 + "Results" + "-" * 18)
print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Sum of Grades: {sum_grades:.1f}")
print(f"Average: {average:.2f}")
print("-" * 43)