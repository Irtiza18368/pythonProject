import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create an empty 3x3 grid
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

current_player = 'X'
player_scores = {'X': 0, 'O': 0}


# Function for handling player input

def player_moves(row1, column1, button1):
    if board[row1][column1] == ' ':
        board[row1][column1] = current_player
        button1.config(text=current_player, state='disabled', relief='sunken')
        if check_win(current_player):
            player_scores[current_player] += 1
            winner_name = "Tawsif"
            update_scoreboard()
            messagebox.showinfo("Game Over", f" {winner_name} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "Better luck next time")
            reset_game()
        else:
            switch_player()


def update_scoreboard():
    x_score_label.config(text=f"Player X: {player_scores['X']}")
    o_score_label.config(text=f"Player O: {player_scores['O']}")


x_score_label = tk.Label(root, text="Player X: 0", font=('Arial', 14))
x_score_label.grid(row=3, column=0)
o_score_label = tk.Label(root, text="Player O: 0", font=('Arial', 14))
o_score_label.grid(row=3, column=1)


# Update the game board in the GUI
def display_board():
    for i in range(3):
        for j in range(3):
            cell_label = tk.Label(root, text=board[i][j], font=('Arial', 20), width=8, height=4,
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

# Start the GUI main loop

root.mainloop()
