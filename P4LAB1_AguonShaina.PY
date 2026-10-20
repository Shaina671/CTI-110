#Shaina Aguon
#10/20/2026
#P4HW1
#This program collects the users specified number of scores, validates each score to ensure it is between 0 and 100, drops the lowest score, and calculates the average of the remaining scores, and determines the final letter grade.

#Pseudocode:
#1. initialize a blank list to hold the scores
#2. ask the user for the number of scores they want to enter
#3. convert the input to an integer(lets call it num_scores):
#   a. promt the user to enter score #i.
#   b. convert the entered score to float (or int).
#   c. uise a while loop to validate the score:
#      - while score is less than 0 or greater than 100:
#        - print the error message stating the score is invalid.
#   d. ask the user to re-enter the score again.
#   e. update the score variable.
#   f. once valid, append the score to the list of scores.
#5. find the lowest score in the score_list using the min() function.
#6. make a copy of the score_list or create a modified list. then remove the lowest score.
#7. calculate the average of the modified list (sum divided by length).
#8. determine the letter grade using conditional statements (if-elif-else):
#   A:90-100
#   B:80-89 
#   C:70-79
#   D:60-69
#   F:below 60

#9. display the results mating the required format:
#-LOWEST SCORE:
#-MODIFIED LIST:
#-SCORE AVERAGE:
#-FINAL GRADE:

def main():
    #step 1 & 2 & 3: ask user for the number of scores

    # Step 1: Initialize a blank list to hold the scores
    score_list = []
    num_scores = int(input("how many scores do you want to enter? "))
    print()

    # Step 4: loop to collect scores for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    #validation loop (nested while loop)
    while score < 0 or score > 100:
        print("\nvalid score entered!!!!")
        print("score should be between 0 and 100.")
        score = float(input(f"enter score #{i} again: "))

    #add valid score to the list
    score_list.append(score)

    print()
    print("----------------results----------------")

        #step 5: find the lowest_score = min(score_list)

    #step 6: create a modified list dropping the lowest score 
    modified_list = list(score_list)
    modified_list.remove(lowest_score)

    #step 7: calculate the average of the modified list if len(modified_list) > 0:
    if len(modified_list) > 0:
            score_average = sum(modified_list) / len(modified_list)
    else:
            score_average = 0.0

    #step 8: determine the letter grade
    if score_average >= 90:
            letter_grade = "A"
    elif score_average >= 80:
            letter_grade = "B"
    elif score_average >= 70:
            letter_grade = "C"
    elif score_average >= 60:
            letter_grade = "D"
    else:
            letter_grade = "F"

    #step 9: display the results
    print(f"Lowest Score: {lowest_score}")
    print(f"Modified List: {modified_list}")
    print(f"Score Average: {score_average:.2f}")
    print(f"Final Grade: {letter_grade}")
    print("---------------------------------------")

    if __name__ == "__main__":
        main()  