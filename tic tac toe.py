import tkinter as tk
from tkinter import messagebox
import random


BG_COLOR = "#358597"
BUTTON_COLOR = "#F4A896"
TEXT_COLOR = "white"


root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(background=BG_COLOR)

board = [" " for _ in range(9)]
current_turn = "Performer" 


def check_winner():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    
    if " " not in board:
        return "Draw"
    
    return None


def computer_move():
    empty_cells = [i for i, spot in enumerate(board) if spot == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"
        buttons[move].config(text="O", state="disabled", disabledforeground=TEXT_COLOR)
        result = check_winner()
        if result:
            end_game(result)
        else:
            global current_turn
            current_turn = "Performer"


def performer_move(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled", disabledforeground=TEXT_COLOR)
        result = check_winner()
        if result:
            end_game(result)
        else:
            global current_turn
            current_turn = "Computer"
            computer_move()


def end_game(winner):
    if winner == "Draw":
        messagebox.showinfo("Game Over", "It's a Draw!")
    elif winner == "X":
        messagebox.showinfo("Game Over", "Performer Wins!")
    else:
        messagebox.showinfo("Game Over", "Computer Wins!")
    
    reset_board()


def reset_board():
    global board, current_turn
    board = [" " for _ in range(9)]
    current_turn = "Performer"
    for button in buttons:
        button.config(text="", state="normal")


buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                       bg=BUTTON_COLOR, fg=TEXT_COLOR,
                       command=lambda i=i: performer_move(i))
    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)


root.mainloop()