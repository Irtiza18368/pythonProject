import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create an empty 3x3 grid
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


# Update the game board in the GUI
def display_board():
    for i in range(3):
        for j in range(3):
            cell_label = tk.Label(root, text=board[i][j], font=('Arial', 14),
                                  width=8, height=4, relief='solid')
            cell_label.grid(row=i, column=j)


# Test the display_board() function
display_board()

# Start the GUI main loop
root.mainloop()


# Function to handle player input
def player_input():
    while True:
        try:
            row = int(input("Enter the row(0,1, or 2):"))
            column = int(input("Enter the row(0,1, or 2):"))
            if row in range(3) and column in range(3) and board[row][column] == ' ':
                return row, column
            else:
                print("Invalid input!")
        except ValueError:
            print("Invalid input")


# Example
row1, column1 = player_input()
print("Player entered row:", row1, "column:", column1)


# Function for updating the game board
def update_board(row2, column2, player):
    board[row2][column2] = player

row = 1
column = 2