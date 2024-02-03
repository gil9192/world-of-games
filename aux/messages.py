# This module contains auxilary functions to print complex and long masseges.


def welcome(username: str) -> None:
    """
    Welcome messege generator
    
    Args:
        username (str): User to embed in the massege. 
    """
    welcome_msg = f"""
    \r{"~" * 80}
    \rHi {username} and welcome to the World of Games: The Epic Journey
    \r{"~" * 80}
    """
    print(welcome_msg)
    return


def launch(game_name: str, diff_level: int) -> None:
    """
    Launch gmae messege generator
    
    Args:
        game_name (str): Name of the game to embed in the massege. 
        diff_level (int): Difficulty level of the game to embed in the massege.
    """
    lunch_msg = f"""
    \r{"~" * 80}
    \rPlaying: {game_name} (level {str(diff_level)})
    \r{"~" * 80}
    """
    print(lunch_msg)
    return
