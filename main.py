import game_brain, game_components, random
print("Welcome to Match That!")

# todo: initialize game
yes_or_no = input("Play? (y/n): ").lower()
if yes_or_no == "y":
    #GAME INITIALIZATION
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
        else: 
            players = [f"Guest {i}" for i in range(1, player_num + 1)]
            anonymous = True
            cont = False

    # TO PASS TO GAME OBJECT: 
    # now have:
    # - player_quantity
    # - player_list
    # - is_anonymous
    


else: 
    print("good bye")




