import tkinter as tk
from tkinter import messagebox
from game_client import make_board , check_for_winner
window = tk.Tk()
window.title("Tic Tac Toe")
buttons = []
# Create board
def create_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 50), height=2, width=6, bg="lightblue", command=lambda row=i, col=j: handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")
            button.row = i
            button.col = j
            buttons.append(button)

create_board()
def draw_board(board):
    for button in buttons:
        text=board[button.row][button.col]
        if str(text) == '0':
            text = ""
        button.config(text=text)

# Initialize variables

current_player = 1
pwd = 'password1'

# Handle button clicks
def handle_click(row, col):
    global current_player
    print(row , col)
    board_temp = make_board((row,col,current_player,pwd))
 
    print(board_temp)
    if board_temp != None:
        draw_board(board_temp)

        winner = check_for_winner()
        if winner != None:
            declare_winner(winner)


# Declare the winner and ask to restart the game
def declare_winner(winner):
    if winner == "tie":
        message = "It's a tie!"
    else:
        message = f"Player {winner} wins!"


    answer = messagebox.askyesno("Game Over", message + " Do you want to restart the game?")

    if answer:
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(3):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                button.config(text="")

        global current_player
        current_player = 1
    else:
        window.quit()

window.mainloop()