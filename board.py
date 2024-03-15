import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((6, 7))

    def check_play(self, num_column):
        column = self.board[:, num_column]
        if 0 in column:
            return True
        return False

    def place_piece(self, team, num_column):
        num_column -= 1
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

    def check_win(self, board):
        if self.checkline(board) != 0:
            return self.checkline(board)
        if self.check_column(board) != 0:
            return self.check_column(board)
        if self.check_diagonal(board) != 0:
            return self.check_diagonal(board)
        if self.check_diagonal2(board) != 0:
            return self.check_diagonal2(board)
        return 0
        
    def checkline(board):
        for i in range(6):
            for j in range(4):
                if board[i][j] == 1:
                    if board[i][j+1] == 1 and board[i][j+2] == 1 and board[i][j+3] == 1:
                        return 1
                if board[i][j] == 2:
                    if board[i][j+1] == 2 and board[i][j+2] == 2 and board[i][j+3] == 2:
                        return 2
        return 0   

    def check_column(board):
        for i in range(3):
            for j in range(7):
                if board[i][j] == 1:
                    if board[i+1][j] == 1 and board[i+2][j] == 1 and board[i+3][j] == 1:
                        return 1
                if board[i][j] == 2:
                    if board[i+1][j] == 2 and board[i+2][j] == 2 and board[i+3][j] == 2:
                        return 2
        return 0

    def check_diagonal(board):
        for i in range(3):
            for j in range(4):
                if board[i][j] == 1:
                    if board[i+1][j+1] == 1 and board[i+2][j+2] == 1 and board[i+3][j+3] == 1:
                        return 1
                if board[i][j] == 2:
                    if board[i+1][j+1] == 2 and board[i+2][j+2] == 2 and board[i+3][j+3] == 2:
                        return 2
        return 0

    def check_diagonal2(board):
        for i in range(3):
            for j in range(7):
                if board[i][j] == 1:
                    if board[i+1][j-1] == 1 and board[i+2][j-2] == 1 and board[i+3][j-3] == 1:
                        return 1
                if board[i][j] == 2:
                    if board[i+1][j-1] == 2 and board[i+2][j-2] == 2 and board[i+3][j-3] == 2:
                        return 2
        return 0