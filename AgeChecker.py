# Prompt the user to enter their age and handle non-integer input
while True:
    try:
        print("Hello! please enter your age bellow")
        age = int(input("Age: "))
        break  # Exit the loop if input is successfully converted to an integer
#This except error will prompt an invalid message to a user if input is not integer
    except ValueError:
        print("Invalid input! Please enter a valid integer age.")

# Compare the user's age to determine eligibility to vote using if...else control statement
if age >= 18:
    print("Congratulations! You are eligible to vote.")
else:
    years_left = 18 - age
    if years_left > 1:
        print(f"Sorry, you are not eligible to vote. You need {years_left} more years.")
    elif years_left == 1:
        print("Sorry, you are not eligible to vote. You need 1 more year.")
    else:
        print("Sorry, you are not eligible to vote. You need to wait until next year.")

