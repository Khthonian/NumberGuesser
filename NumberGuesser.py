import random # This is the only module you can import for this task

# Write your function below for guess_my_number 
def guess_my_number():
    # Welcome the player
    print("Hello player. Welcome to the number guessing game. Please think of a number and then a range within which this number lies.")
    # Establish the lower range ant the upper range
    # Determine guess, via random
    lower_range = int(input("What is your lower range: "))
    upper_range = int(input("what is your upper range: "))
    random_guess = random.randint (lower_range, upper_range)
    print('''Let's begin. Answer with either: "higher", "lower" or "yes" ''')
    answer = ''
    
    # Initiate a random number guess
    # If the guess is below the number, lower the upper range to the random number
    # If the guess is above the number, raise the lower range to the random number
    # Loop until the number is found
    while answer != "yes":
        print("Is it ", random_guess, " ?")
        answer = input()
        if answer == "higher":
            lower_range = random_guess + 1   
            random_guess = random.randint(lower_range, upper_range)
        elif answer == "lower":
            upper_range = random_guess - 1
            random_guess = random.randint(lower_range, upper_range)
        elif answer == "yes":
            print ("I have guessed your number! Goodbye.'")
            break
        else:
            print ('This answer was invalid."higher", "lower", or "yes" are valid responses.')

# Program main -- Do not change code below
guess_my_number()
