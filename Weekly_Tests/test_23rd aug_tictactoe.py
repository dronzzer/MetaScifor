import tkinter as tk
from tkinter import messagebox

player1 = 'X'
stop_game = False

def clicked(r, c):
    global player1
    if states[r][c] == 0 and not stop_game:
        b[r][c].configure(text=player1)
        states[r][c] = player1
        player1 = 'O' if player1 == 'X' else 'X'
        check_if_win()

def check_if_win():
    global stop_game

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            stop_game = True
            messagebox.showinfo("Winner", states[i][0] + " Won!")
            return

    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
            messagebox.showinfo("Winner", states[0][i] + " Won!")
            return

    if states[0][0] == states[1][1] == states[2][2] != 0:
        stop_game = True
        messagebox.showinfo("Winner", states[0][0] + " Won!")
        return

    if states[0][2] == states[1][1] == states[2][0] != 0:
        stop_game = True
        messagebox.showinfo("Winner", states[0][2] + " Won!")
        return

    if all(states[i][j] != 0 for i in range(3) for j in range(3)):
        stop_game = True
        messagebox.showinfo("Tie", "It's a Tie!")

window = tk.Tk()
window.title("TicTacToe")
window.resizable(0, 0)

b = [[None, None, None], [None, None, None], [None, None, None]]
states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        b[i][j] = tk.Button(
            height=4, width=8,
            font=("Helvetica", 20),
            command=lambda r=i, c=j: clicked(r, c)
        )
        b[i][j].grid(row=i, column=j)

window.mainloop()
