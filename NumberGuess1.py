import tkinter as tk
import random

# ------------------ Game Logic ------------------ #

def start_game():
    global number, chances, guess_counter

    try:
        lower = int(lower_entry.get())
        upper = int(upper_entry.get())
        chances = int(chances_entry.get())

        number = random.randint(lower, upper)
        guess_counter = 0

        message_label.config(
            text=f"Game started! You have {chances} chances.",
            fg="blue"
        )

        status_label.config(
            text = f"Guesses used: 0/ {chances} | Remaining: {chances}",
            fg="black"
        )

        guess_entry.config(state="normal")
        submit_btn.config(state="normal")

    except ValueError:
        message_label.config(text="Please enter valid numbers!", fg="red")


def submit_guess():
    global guess_counter

    try:
        guess = int(guess_entry.get())
        guess_counter += 1

        remaining = chances - guess_counter

        if guess == number:
            message_label.config(
                text=f"🎉 Correct! You guessed it in {guess_counter} tries.",
                fg="green"
            )
            status_label.config(
                text=f"Guesses used: {guess_counter} / {chances} | Remaining: {remaining}",
                fg="green"
            )
            end_game()
            return

        elif guess > number:
            message_label.config(text="Too high! Try lower.", fg="orange")

        else:
            message_label.config(text="Too low! Try higher.", fg="orange")

        status_label.config(
            text=f"Guesses used: {guess_counter} / {chances} | Remaining: {remaining}",
            fg="black"
        )
        
        if remaining == 0:
            message_label.config(
                text=f"❌ Game Over! The number was {number}.",
                fg="red"
            )
            end_game()

        guess_entry.delete(0, tk.END)

    except ValueError:
        message_label.config(text="Enter a valid number!", fg="red")


def end_game():
    guess_entry.config(state="disabled")
    submit_btn.config(state="disabled")

# ------------------ GUI Setup ------------------ #

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x350")

# Labels & Entries
tk.Label(root, text="Lower Bound").pack()
lower_entry = tk.Entry(root)
lower_entry.pack()

tk.Label(root, text="Upper Bound").pack()
upper_entry = tk.Entry(root)
upper_entry.pack()

tk.Label(root, text="Number of Chances").pack()
chances_entry = tk.Entry(root)
chances_entry.pack()

start_btn = tk.Button(root, text="Start Game", command=start_game)
start_btn.pack(pady=10)

tk.Label(root, text="Your Guess").pack()
guess_entry = tk.Entry(root, state="disabled")
guess_entry.pack()

submit_btn = tk.Button(root, text="Submit Guess", command=submit_guess, state="disabled")
submit_btn.pack(pady=10)

message_label = tk.Label(root, text="", font=("Arial", 11))
message_label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()
