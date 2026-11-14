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
    def __init__(self):
        #placeholder data for now (currently a dictionary of 60 tricks)
        
        self.tricks = {
            # ========== EASY (50 TRICKS) ==========
            # Points: 3–5

            "Ollie": {"difficulty": "Easy", "points": 3},
            "Kickflip Sex Change": {"difficulty": "Easy", "points": 5},
            "Nollie": {"difficulty": "Easy", "points": 3},
            "Heelflip Sex Change": {"difficulty": "Easy", "points": 5},
            "Frontside 180 Ollie": {"difficulty": "Easy", "points": 3},
            "Backside 180 Ollie": {"difficulty": "Easy", "points": 3},
            "Fakie Frontside 180 Ollie": {"difficulty": "Easy", "points": 4},
            "Fakie Backside 180 Ollie": {"difficulty": "Easy", "points": 4},
            "Nollie Frontside 180": {"difficulty": "Easy", "points": 4},
            "Nollie Backside 180": {"difficulty": "Easy", "points": 4},
            "Switch Frontside 180 Ollie": {"difficulty": "Easy", "points": 4},
            "Switch Backside 180 Ollie": {"difficulty": "Easy", "points": 4},
            "Backside Pop Shove-It": {"difficulty": "Easy", "points": 3},
            "Frontside Pop Shove-It": {"difficulty": "Easy", "points": 3},
            "Fakie Backside Pop Shove-It": {"difficulty": "Easy", "points": 3},
            "Fakie Frontside Pop Shove-It": {"difficulty": "Easy", "points": 3},
            "Nollie Backside Pop Shove-It": {"difficulty": "Easy", "points": 4},
            "Nollie Frontside Pop Shove-It": {"difficulty": "Easy", "points": 4},
            "Switch Backside Pop Shove-It": {"difficulty": "Easy", "points": 4},
            "Switch Frontside Pop Shove-It": {"difficulty": "Easy", "points": 4},
            "Kickflip": {"difficulty": "Easy", "points": 4},
            "Heelflip": {"difficulty": "Easy", "points": 4},
            "Fakie Kickflip": {"difficulty": "Easy", "points": 4},
            "Fakie Heelflip": {"difficulty": "Easy", "points": 4},
            "Nollie Kickflip": {"difficulty": "Easy", "points": 4},
            "Nollie Heelflip": {"difficulty": "Easy", "points": 4},
            "Switch Kickflip": {"difficulty": "Easy", "points": 5},
            "Switch Heelflip": {"difficulty": "Easy", "points": 5},
            "Varial Kickflip": {"difficulty": "Easy", "points": 4},
            "Fakie Varial Kickflip": {"difficulty": "Easy", "points": 4},
            "Nollie Varial Kickflip": {"difficulty": "Easy", "points": 5},
            "360 Flip": {"difficulty": "Easy", "points": 5},
            "Frontside 180 Kickflip": {"difficulty": "Easy", "points": 4},
            "Backside 180 Kickflip": {"difficulty": "Easy", "points": 4},
            "Inward Heelflip": {"difficulty": "Easy", "points": 5},
            "Fakie Backside 180 Kickflip": {"difficulty": "Easy", "points": 5},
            "Frontside 180 Heelflip": {"difficulty": "Easy", "points": 5},
            "Backside 180 Heelflip": {"difficulty": "Easy", "points": 5},
            "Fakie 360 Flip": {"difficulty": "Easy", "points": 5},
            "Hardflip": {"difficulty": "Easy", "points": 5},
            "Backside Bigspin": {"difficulty": "Easy", "points": 4},
            "Frontside Bigspin": {"difficulty": "Easy", "points": 5},
            "Fakie Backside Bigspin": {"difficulty": "Easy", "points": 4},
            "Fakie Frontside Bigspin": {"difficulty": "Easy", "points": 5},
            "Ollie North": {"difficulty": "Easy", "points": 4},
            "Fakie Kickflip Sex Change": {"difficulty": "Easy", "points": 5},
            "Fakie Heelflip Sex Change": {"difficulty": "Easy", "points": 5},
            "Fakie Varial Heelflip": {"difficulty": "Easy", "points": 5},
            "Fakie Backside 180 Heelflip": {"difficulty": "Easy", "points": 5},
            "Fakie Frontside 180 Kickflip": {"difficulty": "Easy", "points": 5},

            # ========== MEDIUM (50 TRICKS) ==========
            # Points: 10–15

            "Nollie Frontside 180 Kickflip": {"difficulty": "Medium", "points": 12},
            "Nollie Backside 180 Kickflip": {"difficulty": "Medium", "points": 12},
            "Nollie Frontside 180 Heelflip": {"difficulty": "Medium", "points": 12},
            "Nollie Backside 180 Heelflip": {"difficulty": "Medium", "points": 12},
            "Switch Frontside 180 Kickflip": {"difficulty": "Medium", "points": 13},
            "Switch Backside 180 Kickflip": {"difficulty": "Medium", "points": 13},
            "Switch Frontside 180 Heelflip": {"difficulty": "Medium", "points": 13},
            "Switch Backside 180 Heelflip": {"difficulty": "Medium", "points": 14},
            "Nollie Backside Bigspin": {"difficulty": "Medium", "points": 10},
            "Nollie Frontside Bigspin": {"difficulty": "Medium", "points": 11},
            "Switch Backside Bigspin": {"difficulty": "Medium", "points": 12},
            "Switch Frontside Bigspin": {"difficulty": "Medium", "points": 12},
            "Varial Heelflip": {"difficulty": "Medium", "points": 10},
            "Casper Flip": {"difficulty": "Medium", "points": 12},
            "Nollie Varial Heelflip": {"difficulty": "Medium", "points": 12},
            "Switch Varial Heelflip": {"difficulty": "Medium", "points": 13},
            "Fakie Casper Flip": {"difficulty": "Medium", "points": 13},
            "Fakie Hardflip": {"difficulty": "Medium", "points": 11},
            "Nollie Hardflip": {"difficulty": "Medium", "points": 12},
            "Switch Hardflip": {"difficulty": "Medium", "points": 14},
            "Hospital Flip": {"difficulty": "Medium", "points": 14},
            "Fakie Inward Heelflip": {"difficulty": "Medium", "points": 11},
            "Nollie Inward Heelflip": {"difficulty": "Medium", "points": 12},
            "Switch Inward Heelflip": {"difficulty": "Medium", "points": 14},
            "Switch Varial Kickflip": {"difficulty": "Medium", "points": 12},
            "Fakie Frontside 180 Heelflip": {"difficulty": "Medium", "points": 12},
            "Nollie 360 Flip": {"difficulty": "Medium", "points": 14},
            "Switch 360 Flip": {"difficulty": "Medium", "points": 15},
            "Backside 360 Pop Shove-It": {"difficulty": "Medium", "points": 10},
            "Frontside 360 Pop Shove-It": {"difficulty": "Medium", "points": 11},
            "Fakie Backside 360 Pop Shove-It": {"difficulty": "Medium", "points": 11},
            "Fakie Frontside 360 Pop Shove-It": {"difficulty": "Medium", "points": 12},
            "Nollie Backside 360 Pop Shove-It": {"difficulty": "Medium", "points": 12},
            "Nollie Frontside 360 Pop Shove-It": {"difficulty": "Medium", "points": 13},
            "Switch Backside 360 Pop Shove-It": {"difficulty": "Medium", "points": 13},
            "Switch Frontside 360 Pop Shove-It": {"difficulty": "Medium", "points": 14},
            "Impossible": {"difficulty": "Medium", "points": 11},
            "Fakie Impossible": {"difficulty": "Medium", "points": 11},
            "Nollie Impossible": {"difficulty": "Medium", "points": 12},
            "Switch Impossible": {"difficulty": "Medium", "points": 14},
            "Pressure Flip": {"difficulty": "Medium", "points": 11},
            "Fakie Pressure Flip": {"difficulty": "Medium", "points": 12},
            "Nollie Pressure Flip": {"difficulty": "Medium", "points": 13},
            "Switch Pressure Flip": {"difficulty": "Medium", "points": 14},
            "Double Kickflip": {"difficulty": "Medium", "points": 13},
            "Fakie Double Kickflip": {"difficulty": "Medium", "points": 13},
            "Backside Bigflip": {"difficulty": "Medium", "points": 14},
            "Fakie Backside Bigflip": {"difficulty": "Medium", "points": 15},
            "Late Kickflip": {"difficulty": "Medium", "points": 13},
            "Late Heelflip": {"difficulty": "Medium", "points": 13},

            # ========== HARD (50 TRICKS) ==========
            # Points: 20–30

            "Laser Flip": {"difficulty": "Hard", "points": 20},
            "Fakie Laser Flip": {"difficulty": "Hard", "points": 21},
            "Nollie Laser Flip": {"difficulty": "Hard", "points": 23},
            "Switch Laser Flip": {"difficulty": "Hard", "points": 25},
            "360 Hardflip": {"difficulty": "Hard", "points": 22},
            "Fakie 360 Hardflip": {"difficulty": "Hard", "points": 23},
            "Nollie 360 Hardflip": {"difficulty": "Hard", "points": 25},
            "Switch 360 Hardflip": {"difficulty": "Hard", "points": 27},
            "Double Heelflip": {"difficulty": "Hard", "points": 20},
            "Fakie Double Heelflip": {"difficulty": "Hard", "points": 21},
            "Nollie Double Heelflip": {"difficulty": "Hard", "points": 23},
            "Switch Double Heelflip": {"difficulty": "Hard", "points": 24},
            "Nollie Double Kickflip": {"difficulty": "Hard", "points": 22},
            "Switch Double Kickflip": {"difficulty": "Hard", "points": 24},
            "Triple Kickflip": {"difficulty": "Hard", "points": 24},
            "Fakie Triple Kickflip": {"difficulty": "Hard", "points": 25},
            "Nollie Triple Kickflip": {"difficulty": "Hard", "points": 27},
            "Switch Triple Kickflip": {"difficulty": "Hard", "points": 29},
            "Nollie Backside Bigflip": {"difficulty": "Hard", "points": 25},
            "Switch Backside Bigflip": {"difficulty": "Hard", "points": 27},
            "Frontside Bigflip": {"difficulty": "Hard", "points": 24},
            "Fakie Frontside Bigflip": {"difficulty": "Hard", "points": 25},
            "Nollie Frontside Bigflip": {"difficulty": "Hard", "points": 27},
            "Switch Frontside Bigflip": {"difficulty": "Hard", "points": 29},
            "Backside Bigspin Heelflip": {"difficulty": "Hard", "points": 23},
            "Frontside Bigspin Heelflip": {"difficulty": "Hard", "points": 24},
            "Fakie Backside Bigspin Heelflip": {"difficulty": "Hard", "points": 24},
            "Fakie Frontside Bigspin Heelflip": {"difficulty": "Hard", "points": 25},
            "Nollie Backside Bigspin Heelflip": {"difficulty": "Hard", "points": 26},
            "Nollie Frontside Bigspin Heelflip": {"difficulty": "Hard", "points": 27},
            "Switch Backside Bigspin Heelflip": {"difficulty": "Hard", "points": 28},
            "Switch Frontside Bigspin Heelflip": {"difficulty": "Hard", "points": 29},
            "360 Double Kickflip": {"difficulty": "Hard", "points": 25},
            "Fakie 360 Double Kickflip": {"difficulty": "Hard", "points": 26},
            "Nollie 360 Double Kickflip": {"difficulty": "Hard", "points": 27},
            "Switch 360 Double Kickflip": {"difficulty": "Hard", "points": 29},
            "Biggerflip": {"difficulty": "Hard", "points": 25},
            "Fakie Biggerflip": {"difficulty": "Hard", "points": 26},
            "Nollie Biggerflip": {"difficulty": "Hard", "points": 28},
            "Switch Biggerflip": {"difficulty": "Hard", "points": 30},
            "Biggerspin": {"difficulty": "Hard", "points": 24},
            "Fakie Biggerspin": {"difficulty": "Hard", "points": 25},
            "Nollie Biggerspin": {"difficulty": "Hard", "points": 27},
            "Switch Biggerspin": {"difficulty": "Hard", "points": 29},
            "Ghetto Bird": {"difficulty": "Hard", "points": 25},
            "Dolphin Flip": {"difficulty": "Hard", "points": 23},
            "Dragon Flip": {"difficulty": "Hard", "points": 28},
            "Nightmare Flip": {"difficulty": "Hard", "points": 25},
            "540 Flip": {"difficulty": "Hard", "points": 29},
            "Double Laser Flip": {"difficulty": "Hard", "points": 30},
        }

    def __iter__(self):
        #tells python to iterate over the internal dictionary
        return iter(self.tricks)

    

