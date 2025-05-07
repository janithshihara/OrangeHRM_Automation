# Importing the pytest library for test framework functionalities
import pytest
# Importing the webdriver module from Selenium for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By

# Importing the Login class from the Login_pg module under the Pages package
#from PageObjects.Loginpg import Login
from PageObjects.LogoutFunction import Logout
# Importing the time module for time-related operations
import time
#Importing the translator module in case the language of the website has been changed
from deep_translator import GoogleTranslator

# Defining a test class named Test_003_Leave
class Test_004_Logout:
    # Declaring class-level variables for base URL, username, and password
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    # Test method to verify the home page title

    # Test method to perform login functionality
    def test_logout(self):
        # Initiating another Chrome WebDriver instance
        self.driver = webdriver.Chrome()

        # Maximizing the browser window
        self.driver.maximize_window()

        # Navigating to the specified base URL
        self.driver.get(self.base_url)

        # Pausing execution for 3 seconds
        time.sleep(5)

        # Creating an instance of the Login class by passing the driver instance
        self.lp = Logout(self.driver)

        # Setting the username in the login page
        self.lp.setUsername(self.username)

        # Pausing execution for 3 seconds
        time.sleep(5)

        # Setting the password in the login page
        self.lp.setPassword(self.password)

        # Pausing execution for 3 seconds
        time.sleep(5)

        # Clicking the login button in the login page
        self.lp.clickLogin()

        # Pausing execution for 5 seconds
        time.sleep(5)

        # Clicking the Dropdown Menu in the Dashboard page
        self.lp.selectDropdown()

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Clicking the Logout button in the Dropdown Menu
        self.lp.clickLogout()

        time.sleep(5)

        # Getting the title of the current page
        act_title = self.driver.title

        # Getting the heading  of the current page
        act_heading = self.driver.find_element(By.TAG_NAME, 'h5').text

        # Translating to the English
        act_heading_translated = GoogleTranslator(source='auto', target='en').translate(act_heading)


        # Closing the browser session
        self.driver.quit()

        # Checking if the actual title and the heading matches the expected title and the heading on Home page
        if act_title == "OrangeHRM" and act_heading_translated == "Login":
            assert True
            print("Title and Heading match: Logout Test Passed")
        else:
            assert False
            print("Title and Heading doesn't match: Logout Test Failed")
            print(act_heading.text)

