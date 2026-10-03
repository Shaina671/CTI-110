#Shaina Aguon
CTI-110 - debugging
P3HW1
10/1/2026
collects six module grades from the lowest to the highest and calculates the sum, average, and letter grade of the grades.

def main():
    #collect 6 sepwerate grades from user
    mod1 = float(input("Enter your first grade: "))
    mod2 = float(input("Enter your second grade: "))
    mod3 = float(input("Enter your third grade: "))         
    mod4 = float(input("Enter your fourth grade: "))
    mod5 = float(input("Enter your fifth grade: "))
    mod6 = float(input("Enter your sixth grade: "))

    #store grades in a list to find the lowest, highest, and sum grades = [mod1, mod2, mod3, mod4, mod5, mod6]

    #calculate the lowest, highest, sum and average of the grades
    low_grade = min(grades)
    high_grade = max(grades)    
    sum_grades = sum(grades)
    average_grade = sum_grades / len(grades)

    print("\n-----------results-----------")
    print(f"Lowest grade: {low_grade}")
    print(f"Highest grade: {high_grade}")
    print(f"Sum of grades: {sum_grades}")
    print(f"Average grade: {average_grade}")
print("-------------------------------")

#determine letter grade based on average
    if average_grade >= 90:
        letter_grade = "A"
    elif average_grade >= 80:
        letter_grade = "B"
    elif average_grade >= 70:
        letter_grade = "C"
    elif average_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"your grade is: {letter}")

if __name__ == "__main__":
    main()  