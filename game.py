from team import Team
from board import Board

class Game:
    def __init__(self):
        self.team1 = Team(1, "team1")
        self.team2 = Team(2, "team2")
        self.board = Board()
        self.turn = 1
        self.play()
    
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
            
            
            
    def current_turn(self, team):
        while True:
            print("It's team ", team.get_number(), " turn")
            team_choice = team.play()
            if self.board.check_play(team_choice):
                self.board.place_piece(team.get_number(), team_choice)
                self.board.display_board()
                break
            else:
                print("This column is full, please choose another one.")
            
    