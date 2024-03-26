import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((6, 7))
        
    def display_board(self):
        print(self.board)
        

    def check_play(self, num_column):
        column = self.board[:, num_column]
        if 0 in column:
            return True
        return False

    def place_piece(self, team, num_column):
        line = 0
        column = self.board[:, num_column]
        if self.check_play(num_column):
            for i in range(len(column)):
                if column[i] == 0:
                    line = i
            self.board[line][num_column] = team
            print(f"l'equipe {team} à mis une piece a la position {line} {num_column}")
        else:
            print("vous ne pouvez pas choisir cette colonne")
            
    def is_column_full(self, num_column):
        column = self.board[:, num_column]
        if 0 in column:
            return False
        return True

    def check_win(self):
        if self.checkline() != 0:
            return self.checkline()
        if self.check_column() != 0:
            return self.check_column()
        if self.check_diagonal() != 0:
            return self.check_diagonal()
        if self.check_diagonal2() != 0:
            return self.check_diagonal2()
        return 0
        
    def checkline(self):
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == 1:
                    if self.board[i][j+1] == 1 and self.board[i][j+2] == 1 and self.board[i][j+3] == 1:
                        return 1
                if self.board[i][j] == 2:
                    if self.board[i][j+1] == 2 and self.board[i][j+2] == 2 and self.board[i][j+3] == 2:
                        return 2
        return 0   

    def check_column(self):
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == 1:
                    if self.board[i+1][j] == 1 and self.board[i+2][j] == 1 and self.board[i+3][j] == 1:
                        return 1
                if self.board[i][j] == 2:
                    if self.board[i+1][j] == 2 and self.board[i+2][j] == 2 and self.board[i+3][j] == 2:
                        return 2
        return 0

    def check_diagonal(self):
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == 1:
                    if self.board[i+1][j+1] == 1 and self.board[i+2][j+2] == 1 and self.board[i+3][j+3] == 1:
                        return 1
                if self.board[i][j] == 2:
                    if self.board[i+1][j+1] == 2 and self.board[i+2][j+2] == 2 and self.board[i+3][j+3] == 2:
                        return 2
        return 0

    def check_diagonal2(self):
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == 1:
                    if self.board[i+1][j-1] == 1 and self.board[i+2][j-2] == 1 and self.board[i+3][j-3] == 1:
                        return 1
                if self.board[i][j] == 2:
                    if self.board[i+1][j-1] == 2 and self.board[i+2][j-2] == 2 and self.board[i+3][j-3] == 2:
                        return 2
        return 0