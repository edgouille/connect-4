from team import Team

class Game:
    def __init__(self):
        self.Team1 = Team(1)
        self.Team2 = Team(2)
        self.Board = Board()
        self.Turn = 1
    
    def play(self):
        while True:
            if self.Turn % 2 == 1:
                self.Team1.play()
            else:
                self.Team2.play()
            self.Turn += 1
            
            
    