from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_scores_service(url: str) -> bool:
    """
    Test for the scores web service.

    Args:
        url (str): url to the scores web service.

    Returns:
        bool: True if passed the test, else False.
    """
    min_score = 1
    max_score = 1000
    try:
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument("--headless")
        driver_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_options)
    except Exception as error:
        print(f"Failed - Couldn't setup selenium webdriver:\n{str(error)}")
        return False

    try:
        driver.get(url)
        result = driver.find_element(By.XPATH, value='//*[@id="score"]')
        score = str(result.text)
    except Exception as error:
        print(f"Failed - Couldn't get desigered resource:\n{str(error)}")
        return False

    if score.isdecimal() and min_score <= int(score) <= max_score:
        print(f"Passed - Score is number in range [{min_score}-{max_score}].")
        return True
    else:
        print(f"Failed - Score isn't number in range [{min_score}-{max_score}].")
        return False


def main_function():
    """
    Run the end 2 end test bench and exit wit apropriate return code.
    """

    print("~" * 80 + "\n" + "Running e2e tests\n" + "~" * 80)
    try:
        assert test_scores_service("http://localhost:8777")
    except AssertionError:
        print("~" * 80 + "\n" + "Some tests failed ...\n" + "~" * 80)
        exit(-1)
    except:
        print("~" * 80 + "\n" + "Encountered runtime error during testing ...\n" + "~" * 80)
        exit(1)

    print("~" * 80 + "\n" + "All tests passed ...\n" + "~" * 80)
    exit(0)


if __name__ == "__main__":
    main_function()
