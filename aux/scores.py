from aux.utils import SCORES_FILE_NAME


def add_score(difficulty: int) -> None:
    """
    The function will try to read the current score in the scores file,
    if it fails it will create a new one and will use it to save the
    current score.

    Args:
        difficulty (int): Used to calculate the additional points for the round.
    """
    # Try to read current score from file:
    current_score = 0
    try:
        current_score = read_score()
    except FileNotFoundError:
        print(f"{SCORES_FILE_NAME} will be created.")
    except Exception as error:
        print(f"Unable to open {SCORES_FILE_NAME} for reading: {str(error)}")
        exit(1)

    # Calculate new score:
    new_score = current_score + (difficulty * 3) + 5
    
    # Write new score to file:
    try:
        write_score(new_score)
    except Exception as error:
        print(f"Unable to open {SCORES_FILE_NAME} for writing: {str(error)}")
        exit(1)
    return


def read_score() -> int:
    """
    Read the current score form score file.

    Returns:
        int: Current score.
    """
    with open(SCORES_FILE_NAME, "r") as db:
        current_score = int(db.readline())
    return current_score


def write_score(new_sore: int) -> None:
    """
    Write the a new score to score file.

    Args:
        new_sore (int): Value to save in the score file.
    """
    with open(SCORES_FILE_NAME, "w") as db:
        db.write(str(new_sore))
    return