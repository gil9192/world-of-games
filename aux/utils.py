import os


SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 1


def screan_cleaner() -> None:
    """
    A function to clear the screen.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return
