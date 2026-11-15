from game_brain import Settings, Game
from art import title
from rules_text import text

run = True
while run:
    print(title)
    print("Welcome to \x1B[3mMatch That!\x1B[0m") 
    user_choice = int(input("Type 1 to Play, 2 to read game description, 3 to end program: "))
    if user_choice == 1:
        #Creates a new settings instance
        user_settings = Settings() 
        player_quantity, player_list, is_anonymous, is_long = user_settings.game_settings()

        play = True
        while play: 
            new_game = Game(player_quantity, player_list, is_anonymous, is_long)
            new_game.start_game()
            user_choice = input(f"Play Again? (y/n): ").lower()
            if user_choice != "y":
                play = False

    elif user_choice == 2:
        print(text)
    else: 
        print("Thank you for playing, good bye!")
        run = False
