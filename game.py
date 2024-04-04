import os
import tkinter as tk
from tkinter import messagebox
from team import Team
import numpy as np
from board import Board
from ia import IA
import pandas as pd

class myApp(tk.Tk):
    def __init__(self):
        self.game_state = 0
        self.team1 = Team(1, "team1")
        self.team2 = Team(2, "team2")
        self.board = Board()
        self.ai = None
        self.turn = 1

        self.log = pd.DataFrame()
        self.moves_team = pd.Series([np.NaN])

        tk.Tk.__init__(self)
        self.configure(bg="light blue")
        self.title("Connect 4")
        self.geometry("1000x700")
        self.button_list = []

        self.border_up = frame(self, 1000, 40, "blue")
        self.border_up.grid(row=0, column=0, columnspan=2)
        self.border_down = frame(self, 1000, 36, "blue")
        self.border_down.grid(row=2, column=0, columnspan=2)

        self.menu_left = frame(self, 270, 620, "light blue")
        self.menu_left.grid(row=1, column=0, rowspan=2, sticky="n")
        self.show_turns = label(self.menu_left, "Turn :", 20)
        self.show_turns.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.show_scores_team1 = label(self.menu_left, "Y :", 20)
        self.show_scores_team1.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.show_scores_team2 = label(self.menu_left, "R :", 20)
        self.show_scores_team2.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.button_play = my_button(self.menu_left, "Play 1 vs 1", 15, 2, "green", "black", 20, self.solo)
        self.button_play_vs_ai = my_button(self.menu_left, "Play VS AI", 15, 2, "green", "black", 20, self.vs_ai)
        self.button_quit = my_button(self.menu_left, "QUIT", 15, 2, "green", "black", 20, self.quit)

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



    def quit(self):
        self.destroy()

    def solo(self):
        replay = messagebox.askyesno("Replay", "Voulez-vous rejouer ?")
        if replay:
            self.reset_game()
            self.ai = None
            
    def vs_ai(self):
        replay = messagebox.askyesno("VS AI", "Play against the AI ?")
        if replay:
            self.ai = IA(2)
            self.reset_game()
            self.current_turn()
        

    def reset_game(self):
        self.turn = 1
        self.game_state = 0
        self.board.clear_board()
        self.clear_visual_board()
        self.log = pd.DataFrame()
        self.moves_team = pd.Series([np.NaN])


    def clear_visual_board(self):
        for i in range(6):
            for j in range(7):
                self.button_list[i][j].config(bg="light green")

    def update_board(self):
        for i in range(6):
            for j in range(7):
                if self.board.board[i][j] == 1:
                    self.button_list[i][j].config(bg="yellow")
                if self.board.board[i][j] == 2:
                    self.button_list[i][j].config(bg="red")


    def current_turn(self, team_choice = None):
        if self.turn % 2 == 1:
            team = 1
        else:
            if self.ai is not None:
                board_copy = np.copy(self.board.get_board())
                team_choice = self.ai.play(Board(board_copy), self.turn)
                self.board.place_piece(2, team_choice)
                self.moves_team.loc[self.turn] = team_choice
                self.update_turn()
                self.update_board()
                if self.check_win():
                    self.game_state = 1
                return False
            else:
                team = 2
        while True:
            if self.board.check_play(team_choice):

                self.moves_team.loc[self.turn] = team_choice
                print(f"team{team} tour = {(self.turn + 1) // 2} choix = {team_choice}")
                print(self.moves_team)

                self.board.place_piece(int(team), team_choice)
                return True
            else:
                return False

    def check_win(self):
        if self.board.check_win() != 0:

            winner = 1 if self.board.check_win() == 1 else 2
            self.moves_team.loc[0] = winner

            if not os.path.isfile("game_logs.csv") or os.stat("game_logs.csv").st_size == 0:
                # Crée un DataFrame vide si le fichier n'existe pas ou s'il est vide
                self.log = pd.DataFrame()
            else:
                # Charge le fichier de journalisation s'il existe et n'est pas vide
                self.log = pd.read_csv("game_logs.csv")

            self.log = pd.concat([self.log, self.moves_team], axis=1)
            self.log.to_csv("game_logs.csv", index=False)


            print(self.log, "test 1")
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
        #print("clicked at", index)

        if (self.master.master.game_state == 0):
            if (self.master.master.current_turn(index[1])):
                self.master.master.update_turn()
                self.master.master.update_board()
                if (self.master.master.check_win()):
                    self.master.master.game_state = 1
                    return
            if (self.master.master.ai is not None):
                self.master.master.current_turn()
                

class my_button(tk.Button):
    def __init__(self, master, text, width, height, bg, fg, size, function):
        tk.Button.__init__(self, master, text=text, width=width, height=height, bg=bg, fg=fg, font=('Times New Roman', size), command=function)
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
