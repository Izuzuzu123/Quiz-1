import tkinter as tk
from tkinter import messagebox

# Game Logic Setup
board = ["-" for _ in range(9)]
currentPlayer = "X"
gameRunning = True

def checkWin():
    # Horizontal
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-"):
        return True
    # Vertical
    if (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-"):
        return True
    # Diagonal
    if (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return True
    return False

# GUI Functions
def button_click(index):
    global currentPlayer, gameRunning

    if board[index] == "-" and gameRunning:
        board[index] = currentPlayer
        buttons[index].config(text=currentPlayer)
        
        # Check for Win
        if checkWin():
            messagebox.showinfo("Tic Tac Toe", f"Player {currentPlayer} wins!")
            gameRunning = False
            root.destroy()
        # Check for Tie
        elif "-" not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            gameRunning = False
            root.destroy()
        else:
            # Switch Player
            currentPlayer = "O" if currentPlayer == "X" else "X"

# Main Window Setup
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)



root.mainloop()