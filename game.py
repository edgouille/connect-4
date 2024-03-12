from team import Team

class Game:
    def __init__(self):
        self.team1 = Team(1, "team1")
        self.team2 = Team(2, "team2")
        self.board = Board()
        self.turn = 1
    
    def play(self):
        while True:
            if self.turn % 2 == 1:
                self.turn(self.team1)    
            else:
                self.turn(self.team2)  
            if self.board.check_win() != 0:
                print("The winner is team ", self.board.check_win())
                break
            self.turn += 1
            
            
    def turn(self, team):
        while True:
            team_choice = team.play()
            if self.board.check_plays(team_choice):
                self.board.place_piece(team.get_number(), team_choice)
                break
            else:
                print("This column is full, please choose another one.")
            
    