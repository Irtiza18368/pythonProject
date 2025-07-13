import random

print("Welcome to the Number Guessing Game.")

lower_bound = int(input("Enter Lower bound: "))
upper_bound = int(input("Enter Upper Bound: "))

chances = int(input("How many chances to guess: "))

print(f"You've only {chances} chances to guess the integer!")

number = random.randint(lower_bound, upper_bound)

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    number_guess = int(input("Enter your guess: "))

    if number_guess == number:
        print(f"Correct! The number is {number}. You guessed it in {guess_counter} guesses.")
        break

    elif number_guess != number and guess_counter >= chances:
        print(f"Sorry! The number was {number}. Better luck next time.")

    elif number_guess > number:
        print("Too high! Try a lower number.")
    
    elif number_guess < number:
        print("Too low! Try a higher number")
    
    else:
        print("Invalid number")

