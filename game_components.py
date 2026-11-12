class Player:
    #since name is optional, pass a guest string for player name
    def __init__(self, name="Guest"): 
        self.name = name
        self.score = 0

class Trick: 
    #maybe difficulty and points can be made into one
    def __init__(self, trick, difficulty, points):
        self.trick = trick
        self.difficulty = difficulty
        self.points = points
        
class TrickLibrary: 
    #dictionary containing all tricks? 
    def __init__(self, tricks):
        #placeholder data for now (currently a dictionary of 60 tricks)
        self.tricks = {
            #trick, difficulty, points

            #easy 
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},

            #medium 
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},

            #hard 
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
            "Kickflip": {"difficulty": "Easy", "points": 5},
        }