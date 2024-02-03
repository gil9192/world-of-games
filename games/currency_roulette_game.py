from currency_converter import CurrencyConverter
import random


def isfloat(value: str) -> bool:
    """
    Check if input value is a string that
    representing a leagal floating point number.

    Args:
        value (str): Value to check.

    Returns:
        bool: True if leagal floating point number string, else False.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_money_interval(amount: int, difficulty: int) -> tuple:
    """
    Retrieves the current USD to ILS exchange rate and calculates an
    interval for the correct answer based on the game's difficulty level.

    Args:
        amount (int): Amount of USD that should be converted to ILS.
        difficulty (int): Game difficulty level.

    Returns:
        tuple: The minimal accaptable, and maximal accaptable values.
    """
    # Get currency via dedicated package.
    currency = CurrencyConverter().convert(1,"USD","ILS")
    delta = 10 - difficulty
    converted = amount * currency
    # No upper range limitations.
    max = converted + delta
    # Trim the lower range at 0.1, can't get negative values and 0 ILS.
    min = 0.1 if converted - delta < 0.1 else converted - delta
    return min, max


def get_guess_from_user(usd_amount: int) -> float:
    """
    Prompts the user to input a guess for the converted value of a
    specified amount in USD.

    Args:
        usd_amount (int): Amount of USD that user has to convert to ILS.

    Returns:
        float: User's conversion guess.
    """
    user_value_selected = None
    while user_value_selected == None:
        choice = input(f"\nPlease guess a the value of {str(usd_amount)} USD in ILS: ")
        if isfloat(choice) and float(choice) >= 0:
            user_value_selected = float(choice)
        else:
            print(f"\nIllegal value, please try again.")
    return user_value_selected


def compare_results(min: float, max: float, user_guess: float) -> bool:
    """
    Check whether user's guess hit the acceptable USD to ILS
    conversion value range (defined by [min,max]).

    Args:
        min (float): Lower acceptable value in ILS
        max (float): Upper acceptable value in ILS
        user_guess (float): User guess in ILS

    Returns:
        bool: True if user's guess hit the exaptable range, else False.
    """
    return min <= user_guess <= max


def play(difficulty: int) -> bool:
    """
    Initiate the "Currency Roulette" sequence by calling corresponding functions.

    Args:
        difficulty (int): Game difficulty.

    Returns:
        bool: True if the user wins, and False if the user loses.
    """
    usd_amount = random.randint(1,100)
    min, max = get_money_interval(usd_amount, difficulty)
    guess = get_guess_from_user(usd_amount)
    return compare_results(min, max, guess)
