import tkinter as tk
from tkinter import messagebox
from team import Team
import numpy as np
from board import Board

class myApp(tk.Tk):
    def __init__(self):
        self.game_state = 0
        self.team1 = Team(1, "team1")
        self.team2 = Team(2, "team2")
        self.board = Board()
        self.turn = 1

        tk.Tk.__init__(self)
        self.configure(bg="light blue")
        self.title("Connect 4")
        self.geometry("1000x700")
        self.button_list = []

        self.border_up = frame(self, 1000, 40, "blue")
        self.border_up.grid(row=0, column=0, columnspan=2)
        self.border_down = frame(self, 1000, 36, "blue")
        self.border_down.grid(row=2, column=0, columnspan=2)

        self.menu_left = frame(self, 270, 620, "light grey")
        self.menu_left.grid(row=1, column=0, rowspan=2, sticky="n")
        self.show_turns = label(self.menu_left, "Turn :", 20)
        self.show_turns.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.show_scores_team1 = label(self.menu_left, "Y :", 20)
        self.show_scores_team1.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.show_scores_team2 = label(self.menu_left, "R :", 20)
        self.show_scores_team2.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.button_play = my_button(self.menu_left,"Play",5,5,"green","black",20,print("coucou"))

        self.frame2 = frame(self, 700, 600)
        self.frame2.grid(row=1, column=1)

        for i in range(6):
            row_buttons = []
            for j in range(7):
                button = Canvas(self.frame2, 100, 100, [i, j])
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.button_list.append(row_buttons)
        self.button_list = np.array(self.button_list)

    def play(self):
        while True:
            if self.turn % 2 == 1:
                self.current_turn(self.team1)
            else:
                self.current_turn(self.team2)
            self.turn += 1
            if self.turn < 8:
                continue
            if self.turn == 43:
                print("It's a draw")
                break
            if self.board.check_win() != 0:
                print("The winner is team ", self.board.check_win())
                break

    def update_board(self):
        for i in range(6):
            for j in range(7):
                if self.board.board[i][j] == 1:
                    self.button_list[i][j].config(bg="yellow")
                if self.board.board[i][j] == 2:
                    self.button_list[i][j].config(bg="red")

    def current_turn(self, team_choice):
        team = 1
        if self.turn % 2 == 1:
            team = 1
        else:
            team = 2
        while True:
            if self.board.check_play(team_choice):
                self.board.place_piece(team, team_choice)
                self.board.display_board()
                return True
            else:
                return False

    def check_win(self):
        if self.board.check_win() != 0:
            if self.board.check_win() == 1:
                print("The winner is team 1")
            if self.board.check_win() == 2:
                print("The winner is team 2")
            messagebox.showinfo("Game Over", f"The winner is team {self.board.check_win()}")
            return True
        return False

    def update_turn(self):
        self.show_turns.config(text=f"Turn : {self.turn}")
        self.turn += 1
        if (self.turn == 43):
            messagebox.showinfo("Game Over", "It's a draw")
            self.game_state = 1

class Canvas(tk.Canvas):
    def __init__(self, master, w, h, index):
        self.position = index
        tk.Canvas.__init__(self, master, width=w, height=h, bg="light green")
        self.grid()
        self.bind("<Button-1>", lambda event: self.action(event, self.position))

    def action(self, event, index=None):
        print("clicked at", index)
        if (self.master.master.game_state == 0):
            if (self.master.master.current_turn(index[1])):
                self.master.master.update_turn()
                self.master.master.update_board()
                if (self.master.master.check_win()):
                    self.master.master.game_state = 1
class my_button(tk.Button):
    def __init__(self, master, text, width, height, bg, fg, size, fonction):
        tk.Button.__init__(self, master, text=text, width=width, height=height,bg=bg,fg=fg,font=('Times New Roman', size), command=fonction)
        self.grid()
class frame(tk.Frame):
    def __init__(self, master, w, h, color=None):
        tk.Frame.__init__(self, master, width=w, height=h, bg=color)
        self.grid()

class label(tk.Label):
    def __init__(self, master, text, size):
        tk.Label.__init__(self, master, text=text, font=("Arial", size))
        self.grid()




window = myApp()
window.mainloop()
