# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    while True:
        try:
            letter = input("Enter a letter (a-z or A-Z): ").strip().lower()
            if len(letter) == 1 and letter.isalpha():
                if letter in ("a", "e", "i", "o", "u"):
                    print(f"The letter {letter} is a vowel.")
                else:
                    print(f"The letter {letter} is a consonant.")
                break
            else:
                print("Invalid input.")
        except:
            break

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.


def check_voting_eligibility():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age <= 0:
                print("Age cannot be negative or zero.")
            else:
                break
        except:
            print("Invalid input.")

    if age > 20:
        print(f"You are eligible to vote at the age of {age}.")
    else:
        print("You dont meet the minimum voting age requirement")


# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.


def calculate_dog_years():
    while True:
        try:
            dog_age = int(input("Input a dog's age: "))
            if dog_age <= 0:
                print("Age cannot be negative or zero.")
            else:
                break
        except:
            print("Invalid input.")

    if dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = 20 + (dog_age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")


# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.


def weather_advice():
    while True:
        try:
            cold = input("Is it cold? (yes/no): ").strip().lower()
            if cold not in ["yes", "no"]:
                print("Invalid input.")
                continue

            raining = input("Is it raining? (yes/no): ").strip().lower()
            if raining not in ["yes", "no"]:
                print("Invalid input.")
                continue

            if cold == "yes" and raining == "yes":
                print("Wear a waterproof coat.")

            elif cold == "yes" and raining == "no":
                print("Wear a warm coat.")

            elif cold == "no" and raining == "yes":
                print("Carry an umbrella.")

            elif cold == "no" and raining == "no":
                print("Wear light clothing.")

            break
        except:
            break


# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.


def determine_season():
    months = (
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    )
    while True:
        try:
            month = input("Enter the month of the year (Jan - Dec): ").strip().lower()
            if month not in months:
                print("Invalid input.")
                continue

            while True:
                try:
                    day = int(input("Enter the day of the month: "))
                    if day <= 0:
                        print("day cannot be negative or zero.")
                    else:
                        break
                except:
                    print("Invalid input.")

            if (
                (month == "dec" and day >= 21)
                or (month in ["jan", "feb"])
                or (month == "mar" and day <= 19)
            ):
                season = "Winter"
            elif (
                (month == "mar" and day >= 20)
                or (month in ["apr", "may"])
                or (month == "jun" and day <= 20)
            ):
                season = "Spring"
            elif (
                (month == "jun" and day >= 21)
                or (month in ["jul", "aug"])
                or (month == "sep" and day <= 21)
            ):
                season = "Summer"
            elif (
                (month == "sep" and day >= 22)
                or (month in ["oct", "nov"])
                or (month == "dec" and day <= 20)
            ):
                season = "Fall"

            print(f"{month} {day} is in {season}")
            break
        except:
            break


# Call the function
determine_season()
