class Team:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        
    def get_number(self):
        return self.number
    
    def play(self):
        choice = int(input("Choose a column to play in"))
        while choice < 1 or choice > 7:
            user_input = input("Choose a column to play in : \n")
            choice = int(user_input)
            if choice < 1 or choice > 7:
                print("Please choose a number between 1 and 7")
        return choice
    