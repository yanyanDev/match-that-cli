from game_brain import Settings, Game
print("Welcome to Match That!")


yes_or_no = input("Play? (y/n): ").lower()
if yes_or_no == "y":
    #Creates a new settings instance
    user_settings = Settings() 
    player_quantity, player_list, is_anonymous, is_long = user_settings.game_settings()

   #Creates new game instance via variables passed from settings class
    new_game = Game(player_quantity, player_list, is_anonymous, is_long)

else: 
    print("good bye")




