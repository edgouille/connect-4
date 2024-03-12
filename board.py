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
        line = 0
        column = self.board[:, num_column]
        if self.check_play(num_column):
            for i in range(len(column)):
                if column[i] == 0:
                    line = i
            self.board[line][num_column] = team
            print(f"l'equipe {team} à mis une piece a la position {line} {num_column}")
        else:
            print("vous en pouvez pas choisir cette colonne")
