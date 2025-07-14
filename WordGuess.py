import random

user_input = input("What is your name? ")
print(f"Good Luck! {user_input}")

words = ["rainbow", "computer", "science", "programming", "python"]
word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed_to_guess = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed_to_guess += 1

    if failed_to_guess == 0:
        print("You win")
        print(f"The word is: {word}")
        break

    print()
    user_guess = input("guess a character: ")

    guesses += user_guess

    if user_guess not in word:

        turns -= 1
        print("Wrong")
        print(f"You have {turns} turns more guesses.")

        if turns == 0:
            print("You lose.")
            print(f"The word was: {word}")


    