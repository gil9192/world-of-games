from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def test_registration(url: str) -> bool:
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
        games_element = driver.find_element(By.XPATH, value='/html/body/nav/ul/li[2]/a')
        games_element.click()
        registratrion_url = driver.find_element(By.XPATH, value='/html/body/div/a')
        registratrion_url.click()
        registratrion_username = driver.find_element(By.XPATH, value='//*[@id="register_username"]')
        registratrion_password = driver.find_element(By.XPATH, value='//*[@id="register_password"]')
        registratrion_verification = driver.find_element(By.XPATH, value='//*[@id="verification_password"]')
        registratrion_username.send_keys("testuser")
        registratrion_password.send_keys("Test12345")
        registratrion_verification.send_keys("Test12345")
        register = driver.find_element(By.XPATH, value='/html/body/div/form/button')
        register.click()
        try:
            response = driver.find_element(By.XPATH, value='/html/body/div/h3')
            if response.text == "User Already Exists..." or response.text == "Passwords Don't Match.":
                return False
        except:
            pass
        return True
    except Exception as error:
        print(f"Failed - Couldn't get desigered resource:\n{str(error)}")
        return False


def test_login(url: str) -> bool:
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
        games_element = driver.find_element(By.XPATH, value='/html/body/nav/ul/li[2]/a')
        games_element.click()
        login_username = driver.find_element(By.XPATH, value='//*[@id="login_username"]')
        login_password = driver.find_element(By.XPATH, value='//*[@id="login_password"]')
        login_button = driver.find_element(By.XPATH, value='/html/body/div/form/button')
        login_username.send_keys("testuser")
        login_password.send_keys("Test12345")
        login_button.click()
        try:
            response = driver.find_element(By.XPATH, value='/html/body/div/h3')
            if response.text == "Invalid Credentials!":
                return False
        except:
            pass
        return True
    except Exception as error:
        print(f"Failed - Couldn't get desigered resource:\n{str(error)}")
        return False


def main_function():
    """
    Run the end 2 end test bench and exit wit apropriate return code.
    """
    print("~" * 80 + "\n" + "Running e2e tests\n" + "~" * 80)
    try:
        assert test_login("http://localhost:8777") == False                     # Unregisterd user should not login
        assert test_registration("http://localhost:8777") == True
        assert test_registration("http://localhost:8777") == False              # Two users with same username should not be registered.
        assert test_login("http://localhost:8777") == True
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