import random
import time
import aux


def generate_sequence(difficulty: int, min: int, max: int) -> list:
    """
    Generates a list of random numbers between 1 and 101, with a length
    equal to the difficulty.

    Args:
        length (int): Lenght of random numbers list.
        min (int): Lowest possible random value.
        max (int): Highest possible random value.

    Returns:
        list: List of random numbers (int).
    """
    return [random.randint(min, max) for _ in range(difficulty)]


def display_sequence(sequence: list, duration: float) -> None:
    """
    Display a sequence of random numbers for a brief duration.

    Args:
        sequence (list): Sequence of numbers to display.
        duration (float): How long the sequence will be displayed in seconds.
    """
    for i in range(3, 0, -1):
        print(f"Sequnce will appear in:  {str(i)} seconds", end="\r")
        time.sleep(1)
    aux.utils.screan_cleaner()
    print(sequence)
    time.sleep(duration)
    aux.utils.screan_cleaner()
    return


def get_list_from_user(difficulty: int, min: int, max: int) -> list:
    """
    Prompts the user to input a list of numbers matching the length of the
    generated sequence.

    Args:
        difficulty (int): Lenght of user's numbers list.
        min (int): Lowest possible value.
        max (int): Highest possible value.

    Returns:
        list: List of user's numbers (int).
    """
    user_inputs = []
    for i in range(difficulty):
        user_value_selected = None
        while user_value_selected == None:
            choice = input(f"\nPlease enter sequence member \"{i+1}\": ")
            if choice.isdigit() and (min <= int(choice) <= max):
                user_value_selected = int(choice)
            else:
                print(f"\nIllegal value, please try again (allowd values are {min}-{max}).")
        user_inputs.append(user_value_selected)
    return user_inputs


def compare_results(generated_sequence: list, users_sequence: list) -> bool:
    """
    Check whether user attempt to recover sequence is successful.

    Args:
        generated_sequence (list): Generated sequence.
        users_sequence (list): Sequence of values recovered by user.

    Returns:
        bool: True if both lists identical, else False.
    """
    return generated_sequence == users_sequence


def play(difficulty: int) -> bool:
    """
    Initiate the "Memory Game" sequence by calling corresponding functions.

    Args:
        difficulty (int): Game difficulty.

    Returns:
        bool: True if the user wins, and False if the user loses.
    """
    min_value = 1
    max_value = 101
    duration = 0.7
    random_sequnce = generate_sequence(difficulty, min_value, max_value)
    display_sequence(random_sequnce, duration)
    users_sequence = get_list_from_user(difficulty, min_value, max_value)
    return compare_results(random_sequnce, users_sequence)
