import numpy as np
import pandas as pd
import copy
from board import Board


class IA:
    def __init__(self, team = 2):
        self.choice = np.array([0, 0, 0, 0, 0, 0, 0])
        self.team_number = 2
        self.board = Board()
    
    
    def clear_choice(self):
        for i in range(7):
            self.choice[i] = 0
    
    
    def play(self, board):
        self.update_score(board)
        print(self.choice)
        to_play = np.argmax(self.choice)
        print(to_play)
        self.clear_choice()
        return to_play
        
    
    def update_score(self, board):
        #error board est toujours le meme entre chaque check
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
        self.board.change_board(np.copy(board.get_board()))
        for i in range(7):
            if self.choice[i] != -1000:
                self.board.place_piece(self.team_number, i)
                if (self.board.is_column_full(i) == False):
                    self.board.place_piece(opponent, i)
                    if self.board.check_win() == opponent:
                        self.choice[i] -= 100
            self.board.display_board()
            self.board.change_board(np.copy(board.get_board()))
            
    def is_full(self, board):
        for i in range(7):
            if board.is_column_full(i):
                self.choice[i] = -1000
                
                
    def winnable_choice(self, board):
        for i in range(7):
            self.board.change_board(np.copy(board.get_board()))
            if self.choice[i] != -1000:
                self.board.place_piece(self.team_number, i)
                if self.board.check_win() == self.team_number:
                    self.choice[i] = 1000
                    return True
                
    def blockable_choice(self, board):
        if self.team_number == 1:
            opponent = 2 
        else:
            opponent = 1
        for i in range(7):
            self.board.change_board(np.copy(board.get_board()))
            if self.choice[i] != -1000:
                self.board.place_piece(opponent, i)
                if self.board.check_win() == 1:
                    self.choice[i] = 900
                    return True
        return False