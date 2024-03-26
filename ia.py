import numpy as np
import pandas as pd


class IA:
    def __init__(self, team = 2):
        choice = np.zeros((7, 1))
        team_number = team
    
    
    def clear_choice(self):
        for i in range(7):
            self.choice[i] = 0
    
    
    def play(self, board):
        self.update_score()
        to_play = np.argmax(self.choice)
        self.clear_choice()
        return to_play
        
    
    def update_score(self, board):
        self.is_full(board)
        if (self.winnable_choice(board)):
            return
        if (self.blockable_choice(board)):
            return
        self.avoid_loosing_choice(board)
        #check from older game
        
    def avoid_loosing_choice(self, board):
        if self.team_number == 1:
            opponent = 2 
        else:
            opponent = 1
        board_copy = board
        for i in range(7):
            if self.choice[i] != -1000:
                board_copy.place_piece(self.team_number, i)
                if (board_copy.is_column_full(i) == False):
                    board_copy.place_piece(opponent, i)
                    if board_copy.check_win() == opponent:
                        self.choice[i] -= 100
            board_copy = board

                
                
                
                
        pass
    
    def is_full(self):
        for i in range(7):
            if self.board[0][i] != 0:
                self.choice[i] = -1000
                
                
    def winnable_choice(self, board):
        for i in range(7):
            board_copy = board
            if self.choice[i] != -1000:
                board_copy.place_piece(self.team_number, i)
                if board_copy.check_win() == self.team_number:
                    self.choice[i] = 1000
                    return True
                
    def blockable_choice(self, board):
        if self.team_number == 1:
            opponent = 2 
        else:
            opponent = 1
        for i in range(7):
            board_copy = board
            if self.choice[i] != -1000:
                board_copy.place_piece(opponent, i)
                if board_copy.check_win() == 1:
                    self.choice[i] = 900
                    return True
        return False