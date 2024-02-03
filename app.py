from games import currency_roulette_game
from games import memory_game
from games import guess_game
from aux import messages
from aux import scores


def welcome() -> None:
    """
    This function takes a person's name as input and displays 
    a personalized welcome message.
    """
    user_selected = False

    while not user_selected:
        username = input("Enter username: ")
        if " " in username:
            print("\nUser name can't contain white spaces! please retry.\n")
        else:
            user_selected = True
            
    messages.welcome(username)
    return


def start_play() -> None:
    """
    This function presents a list of available games and dificulty levels to the user.
    """
    games = [
        {
            "id": 1,
            "name": "Memory Game",
            "desc": "a sequence of numbers will appear for 1 second and you have to guess it back.",
            "play": memory_game.play,
        },
        {
            "id": 2,
            "name": "Guess Game",
            "desc": "guess a number and see if you chose like the computer.",
            "play": guess_game.play
        },
        {
            "id": 3,
            "name": "Currency Roulette",
            "desc": "try and guess the value of a random amount of USD in ILS.",
            "play": currency_roulette_game.play
        }
    ]
    play = True
    max_diff = 5
    min_diff = 1
    
    while play:
        # Show available games:
        print("Please choose a game to play:\n")
        for game in games:
            print(f"{game['id']}. {game['name']} - {game['desc']}")

        # Select the game to play:
        game_selected = None
        while not game_selected:
            choice = input(f"\nPlease select game from the list above (choose between 1 and {str(len(games))}): ")
            if choice.isdigit() and (0 < int(choice) <= len(games)):
                game_selected = int(choice)
            else:
                print(f"\nPlease select a number in range of 1-{str(len(games))}")

        # Select the difficulty level:
        diff_level_selected = None
        while not diff_level_selected:
            choice = input(f"\nPlease select difficulty level between ({min_diff} and {max_diff}): ")
            if choice.isdigit() and (min_diff <= int(choice) <= max_diff):
                diff_level_selected = int(choice)
            else:
                print(f"\nPlease select a number in range of {min_diff}-{max_diff}")

        # Acquire selected game data:
        game = next((game for game in games if game["id"] == game_selected))

        # Launch the game:
        messages.launch(game["name"], diff_level_selected)
        game_result = game["play"](diff_level_selected)

        # Print game result:
        if game_result:
            print(f"\nYou Won!")
            scores.add_score(diff_level_selected)
        else:
            print(f"\nComputer Won, Game Over...")
        
        # Conclude or replay the game:
        continue_play_selected = None
        while not continue_play_selected:
            choice = input(f"\nContinue to play (Yes/No): ")
            if choice.lower() == "n" or choice.lower() == "no":
                continue_play_selected = True
                play = False
            elif choice.lower() == "y" or choice.lower() == "yes":
                continue_play_selected = True
            else:
                print(f"\nPlease enter valid choice (Yes or No)")

    return
