import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create an empty 3x3 grid
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

current_player = 'X'
player_scores = {'X': 0, 'O': 0}
total_rounds = 10

player_X_name = "Player Tawsif"
player_O_name = "Player XYZ"

# Timer variables
timer_interval = 10000  # Time in milliseconds (10 seconds)
timer_remaining = tk.StringVar()
timer_id = None


# Function to start the game
def get_player_names():
    global player_X_name, player_O_name
    player_X_name = simpledialog.askstring("Player Names", "Enter Player X's name:")
    player_O_name = simpledialog.askstring("Player Names", "Enter Player O's name:")
    update_scoreboard()


def start_game():
    for button in button_list:
        button.config(state='normal')
    reset_game()
    get_player_names()
    update_scoreboard()
    start_timer()  # Start the timer when the game starts


def ai_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        row, column = random.choice(empty_cells)
        player_moves(row, column, button_list[row * 3 + column])


# Function for handling player input

def player_moves(row1, column1, button1):
    global current_player
    if board[row1][column1] == ' ':
        board[row1][column1] = current_player
        button1.config(text=current_player, state='disabled', relief='sunken')
        if check_win(current_player):
            player_scores[current_player] += 1
            update_scoreboard()
            winner_name = player_X_name if current_player == 'X' else player_O_name
            messagebox.showinfo("Game Over", f" {winner_name} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "Better luck next time")
            reset_game()
        else:
            switch_player()
            if current_player == 'O':
                ai_move()


def update_scoreboard():
    x_score_label.config(text=f"{player_X_name}: {player_scores['X']}")
    o_score_label.config(text=f"{player_O_name}: {player_scores['O']}")


x_score_label = tk.Label(root, text=f"{player_X_name}: 0", font=('Arial', 10))
x_score_label.grid(row=3, column=0)
o_score_label = tk.Label(root, text=f"{player_O_name}: 0", font=('Arial', 10))
o_score_label.grid(row=3, column=1)


# Update the game board in the GUI
def display_board():
    for i in range(3):
        for j in range(3):
            cell_label = tk.Label(root, text=board[i][j], font=('Arial', 20), width=12, height=8,
                                  relief='solid')
            cell_label.grid(row=i, column=j)


def check_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return True

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False


def check_tie():
    for row1 in range(3):
        for column1 in range(3):
            if board[row1][column1] == ' ':
                return False
    return True


def reset_game():
    for row in range(3):
        for column in range(3):
            board[row][column] = ' '
        for button in button_list:
            button.config(text=' ', state='normal', relief='raised')


def switch_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'


button_list = []

# Creating GUI Buttons

for row in range(3):
    for column in range(3):
        button = tk.Button(root, text=' ', font=('Arial', 20), width=8, height=4, relief='raised')
        button.grid(row=row, column=column)
        button.config(command=lambda r=row, c=column, b=button: player_moves(r, c, b))
        button_list.append(button)


def reset_scores():
    global player_scores
    player_scores = {'X': 0, 'O': 0}
    update_scoreboard()


reset_scores_button = tk.Button(root, text="Reset Scores", font=('Arial', 10), command=reset_scores)
reset_scores_button.grid(row=3, column=2)

root.mainloop()
