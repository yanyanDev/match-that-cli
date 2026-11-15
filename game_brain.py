from game_components import Player, Trick, TrickLibrary
import random
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

        #pass everthing to Game()
        return player_num, players, anonymous, is_game_long

class Game():
    """Start a game that takes the number of players, anonymity, and game length"""
    def __init__(self, player_quantity, player_list, is_anonymous, is_long):
        self.player_num = player_quantity #int
        self.player_list = player_list #list
        self.is_anonymous = is_anonymous #bool
        self.is_long = is_long #bool

        #create TrickLibrary instance 
        self.trick_library = TrickLibrary()

        
    def pull_trick(self):
        trick = random.choice(list(self.trick_library))
        points = self.trick_library.tricks[trick]["points"]
        return trick, points
       

    def start_game(self):
        """Starts a game using all settings from the Game() constructor."""

        #instantiate Player objects for all players and store in a list to iterate through
        to_play = []
        for player in self.player_list: 
            player_obj = Player()
            player_obj.name = player
            to_play.append(player_obj)

        #pull random trick
        current_trick, points = self.pull_trick()

        game_duration = 30 if self.is_long else 10
        while game_duration > 0:

            #CORE GAME LOOP
            for player in to_play:
                #display names
                for display in to_play:
                    print(f"{display.name}'s score: {display.score}")

                #display current trick and who's turn it is
                print(f"TRICKS LEFT: [{game_duration}/{30 if self.is_long else 10 }]")
                print(f"It's {player.name}'s turn!")
                print(f"the current trick is {current_trick} worth {points} points")
                print(f"GO!")

                #checks if landed, game_duration decrements every turn. 
                landed = int(input(f"Type 1 if landed, 2 if missed: "))
                if landed == 1:
                    print(f"MATCHED!!! {player.name} gets {points} points.")

                    player.score += points
                    current_trick, points = self.pull_trick()
                    game_duration -= 1
                    
                elif landed == 2:
                  print("MISSED!!!")
                  print(f"no points awarded to {player.name}.")

                #space for visibility
                for _ in range(5):
                    print()

                if game_duration == 0:
                    break

        #re-sort player list ordered by number of points accumulated
        sorted_players = sorted(to_play, key=lambda player: -player.score)
        winner = sorted_players[0]
        print(f"TRICKS LEFT: [{game_duration}/{30 if self.is_long else 10 }]")
        print(f"THE WINNER IS {winner.name}!!!")
        print()
        print(f"FINAL SCORES:")

        #display rankings
        rank = 1
        for display in sorted_players:
            print(f"{rank}. {display.name}'s score: {display.score}")
            rank += 1
