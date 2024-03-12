from team import Team

class Game:
    def __init__(self):
        self.team1 = Team(1)
        self.team2 = Team(2)
        self.board = Board()
        self.turn = 1
    
    def play(self):
        while True:
            if self.Turn % 2 == 1:
                self.Board.check_plays(self.Team1.play())
            else:
                self.Team2.play()
            self.Turn += 1
            
            
    