#initialze to start the a game
import game_components
class Game():
    """Start a game that takes the number of players, anonymity, game length, and game difficulty"""
    def __init__(self, player_quantity, player_list, is_anonymous, is_long, difficulty):
        self.player_num = player_quantity #int
        self.player_list = player_list #list
        self.is_anonymous = is_anonymous #bool
        self.is_long = is_long #bool
        self.difficulty = difficulty #int

    


    

