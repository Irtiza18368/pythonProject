import random

print("Winning rules of the game ROCK PAPER SCISSORS are: ")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins")

while True:

    print("\n Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors ")

    user_choice = int(input("Enter your choice: "))
    computer_choice = random.randint(1, 3)
    result = None

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a valid choice please."))

    if user_choice == 1:
        choice_name = "Rock"
    elif user_choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    print(f"User choice is: {choice_name}")
    print("Now its Computer Turn...")

    if computer_choice == 1:
        choice_name = "Rock"
    elif computer_choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    print(f"Computer Choice is: {choice_name}")
    print(f"{user_choice} vs {computer_choice}")

    if user_choice == computer_choice:
        result = "DRAW"
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1):
        result = "Paper"
    elif (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 2):
        result = "Rock"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        result = "Scissors"

    # Print the result
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    print("Do you want to play again? (Y/N)")
    answer = input().lower()
    if answer == 'n':
        break

print("Thank you for playing")