# Importing the pytest library for test framework functionalities
import pytest
# Importing the webdriver module from Selenium for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LeaveFunction import Leave
# Importing the time module for time-related operations
import time
#Importing the translator module in case the language of the website has been changed
from deep_translator import GoogleTranslator

# Defining a test class named Test_003_Leave
class Test_003_Leave:
    # Declaring class-level variables for base URL, username, and password
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    # Test method to verify the home page title

    # Test method to perform login functionality
    def test_leave(self):
        # Initiating another Chrome WebDriver instance
        self.driver = webdriver.Chrome()

        # Maximizing the browser window
        self.driver.maximize_window()

        # Navigating to the specified base URL
        self.driver.get(self.base_url)

        # Pausing execution for 3 seconds
        time.sleep(5)

        # Creating an instance of the Login class by passing the driver instance
        self.lp = Leave(self.driver)

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

        # Pausing execution for 3 seconds
        time.sleep(5)

        # Clicking the login button in the Dashboard page
        self.lp.clickLeave()

        time.sleep(5)
        # Getting the title of the current page
        act_title = self.driver.title

        # Getting the heading  of the current page
        act_heading = self.driver.find_element(By.TAG_NAME, 'h6').text

        #Translating to the English
        act_heading_translated = GoogleTranslator(source='auto', target='en').translate(act_heading)


        # Closing the browser session
        self.driver.quit()

        # Checking if the actual title matches the expected title on Home page
        #print(act_heading)
        if act_title == "OrangeHRM" and act_heading_translated == "Leave":
            assert True
            print("Title and Heading match: Leave Test Passed")
        else:
            assert False
            print("Title and Heading doesn't match: Leave Test Failed")
            print(act_heading.text)

