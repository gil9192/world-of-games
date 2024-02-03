import random


def generate_number(max: int) -> int:
    """
    Generates a random number between 0 and the specified max value (difficulty)
    saving it as the.

    Args:
        max (int): The highest possible value that might be randomly generated.

    Returns:
        int: Randomly generated value.
    """
    return random.randint(0,max)


def get_guess_from_user(max: int) -> int:
    """
    Prompts the user to input a number within the range of 0 to the
    max value (difficulty) and returns the entered number.

    Args:
        max (int): The highest possible value that user can provide.

    Returns:
        int: User's guess value.
    """
    user_value_selected = None
    while user_value_selected == None:
        choice = input(f"\nPlease guess a number between (0 and {str(max)}): ")
        if choice.isdigit() and (0 <= int(choice) <= max):
            user_value_selected = int(choice)
        else:
            print(f"\nPlease select a number in range of 0-{str(max)}")
    return user_value_selected


def compare_results(user_value: int, computer_value: int) -> bool:
    """
    Compares the generated secret number with the user's input and
    determines if they match.

    Args:
        user_value (int): User's guess value.
        computer_value (int): Generated secret number.

    Returns:
        bool: True if both input arguments are equal, otherwise False.
    """
    return user_value == computer_value


def play(difficulty: int) -> bool:
    """
    Initiate the "Guess Game" sequence by calling corresponding functions.

    Args:
        difficulty (int): Game difficulty.

    Returns:
        bool: True if the user wins, and False if the user loses.
    """
    generated_number = generate_number(difficulty)
    guessed_number = get_guess_from_user(difficulty)
    return compare_results(guessed_number, generated_number)
