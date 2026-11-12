#initialze to start the a game
class Settings: 
    def game_settings(self):
        print("GAME SETTINGS")
        cont = True
        while cont:
            player_num = int(input(f"How many players? (2 minimum - 8 maximum): "))
                #decide player number
            if player_num in range(2, 9):
                #take variable
                cont = False
            else: 
                print(f"Please enter a valid input.")
                cont = True
        
        cont = True
        while cont: 
            names_or_no = input(f"Name players? (y/n):").lower()
            if names_or_no == "y":
                players = [input(f"Enter name for Player {i + 1}: ").lower() for i in range(player_num)]
                anonymous = False
                cont = False
            elif names_or_no == "n": 
                players = [f"Guest {i}" for i in range(1, player_num + 1)]
                anonymous = True
                cont = False
            else: 
                print(f"Please enter a valid input.")
                cont = True
    
        # TO PASS TO GAME OBJECT: 
        # now have:
        # - player_quantity
        # - player_list
        # - is_anonymous
    
        #print list of players
    
        cont = True 
        while cont: 
            print("SELECT GAME MODE")
            is_game_long = None
            quick_or_full = int(input(f"1 for Quickplay (10 Tricks),  2 for Full Game (30 Tricks): ").lower())
            if quick_or_full == 1:
                is_game_long = False 
                cont = False
            elif quick_or_full == 2: 
                is_game_long = True
                cont = False
    
        print(f"YOUR GAME SETTINGS:")
        print(f"Players: {player_num} || Player Names: {players} || Game Mode: {"Quickplay" if is_game_long == False else "Full Game"}")

        return player_num, players, anonymous, is_game_long

class Game():
    """Start a game that takes the number of players, anonymity, and game length"""
    def __init__(self, player_quantity, player_list, is_anonymous, is_long):
        self.player_num = player_quantity #int
        self.player_list = player_list #list
        self.is_anonymous = is_anonymous #bool
        self.is_long = is_long #bool

    

