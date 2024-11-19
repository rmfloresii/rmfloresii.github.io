# Selenium Code to Test Freelancer.com Account Sign Up

"""
This Python script automates the process of testing Freelancer's sign-up workflow using Selenium 
WebDriver. It covers everything from opening the homepage to completing account setup, simulating 
user actions like filling out forms and clicking buttons. The script includes checks to make sure 
each step works as expected and uses a combination of time.sleep() pauses with waiting for elements 
to be clickable, fillable, or readable to account for page loading times. It's designed to make 
testing the registration process more efficient and repeatable. Written by Richard "RogueFlotilla" 
Flores, Cybersecurity Research Assistant, Marymount University, Arlington, VA.
"""
# Make sure Firefox and the Selenium WebDriver are installed
# Python code to install WebDriver
'''
try:
    # Run the pip install command for webdriver-manager
    subprocess.run([sys.executable, "-m", "pip", "install", "webdriver-manager"], check=True)
    print("webdriver-manager installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while installing webdriver-manager: {e}")
'''

# Powershell code to install WebDriver
'''
pip install webdriver-manager
'''

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest


class SignUp(unittest.TestCase):

    driver = None

    @classmethod
    # function to setup webdriver
    def setUp(self):
        # Set up the browser driver
        # MAKE SURE FIREFOX IS INSTALLED

        # Configure Firefox options for private browsing
        options = Options()
        options.add_argument('-private')  # Enable private browsing mode

        # Initialize WebDriver with options (private window)
        self.driver = (webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
            options=options))

        # Set site to test
        base_url = 'https://www.freelancer.com/' # target URL for test
        self.driver.get(base_url) # navigate to page
        # self.driver.maximize_window() # Maximize window to frame
        self.driver.fullscreen_window() # Mazimize window to fullscreen

    # function to test sign up form
    def test_sign_up_form(self):
        sleepy_time = 1 # amount of time in seconds to sleep for between steps
        six_digit_time = datetime.now().strftime("%H%M%S") # 6 numbers pulled from time HrMinSec
        wait = WebDriverWait(self.driver, 10)  # wait, w/ max 10-second timeout

        ### FREELANCER HOME PAGE ###
        # Locate the sign up link on the home page
        time.sleep(sleepy_time)  # wait for x sec
        signup_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up")))
            # wait for item to be clickable
        signup_link.click()  # clicking the link        

        ### FREELANCER SIGNUP PAGE ###
        # Test Assertion 1 - new landing page is called "Sign up"
        time.sleep(sleepy_time)  # wait for x sec
        signup_page_title_css_selector = (wait.until(EC.presence_of_element_located( \
            (By.CSS_SELECTOR, 'h1.ng-star-inserted'))))
        signup_page_title = signup_page_title_css_selector.text
        self.assertEqual("Sign up", signup_page_title, 
            f"Expected 'Sign up' but got '{signup_page_title}'")

        # First name text box
        time.sleep(sleepy_time)  # wait for x sec
        fname_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/div[1]/ \
            app-signup/app-details-form/form/div[2]/fl-input[1]/div/div/div/input')
        fname_textbox = wait.until(EC.element_to_be_clickable((By.XPATH, fname_xpath)))
            # wait for item to be clickable
        fname_textbox.send_keys("Bernie")

        # Last name textbox
        time.sleep(sleepy_time)  # wait for x sec
        lname_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/div[1]/ \
            app-signup/app-details-form/form/div[2]/fl-input[2]/div/div/div/input')
        lname_textbox = wait.until(EC.element_to_be_clickable((By.XPATH, lname_xpath)))
            # wait for item to be fillable
        lname_textbox.send_keys("DaDog")

        # Email textbox
        time.sleep(sleepy_time)  # wait for x sec
        email_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/div[1]/ \
            app-signup/app-details-form/form/fl-input/div/div/div/input')
        email_textbox = wait.until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
            # wait for item to be fillable
        email_textbox.send_keys("berniedrools"+six_digit_time+"@gmail.com")

        # Password textbox
        time.sleep(sleepy_time)  # wait for x sec
        password_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/ \
            div[1]/app-signup/app-details-form/form/div[3]/fl-input/div/div/div/input')
        password_textbox = wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
            # wait for item to be fillable
        password_textbox.send_keys("0kP@$$w0rd"+six_digit_time) # replace with any random password

        # Click to check the user-agreement check-box
        time.sleep(sleepy_time)  # wait for x sec
        agreement_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/ \
            div[1]/app-signup/app-details-form/form/div[4]/fl-checkbox/div')
        agreement_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, agreement_xpath)))
            # wait for item to be clickable
        agreement_checkbox.click()

        # Click the join button
        time.sleep(sleepy_time)  # wait for x sec
        join_freelancer_button_xpath = ('/html/body/app-root/app-logged-out-shell/div/ \
            app-signup-page/div/div[1]/app-signup/app-details-form/form/app-login-signup-button')
        join_freelancer_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, join_freelancer_button_xpath))) # wait for item to be clickable
        join_freelancer_button.click()

        ### FREELANCER SLECT USERNAME PAGE ###

        # Test Assertion 2 - new landing page is called "Choose a username"
        time.sleep(sleepy_time)  # wait for x sec
        username_page_title_css_selector = (
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        )
        username_page_title = username_page_title_css_selector.text
        self.assertEqual("Choose a username", username_page_title, 
            f"Expected 'Choose a username' but got '{username_page_title}'")

        # Username textbox
        time.sleep(sleepy_time)  # wait for x sec
        username_value = "StBernard"+six_digit_time
        username_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/ \
            div[1]/app-signup/app-username-select-form/form/fl-input/div/div/div/input')
        username = wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
            # wait for item to be fillable
        username.send_keys(username_value)

        # Click next
        time.sleep(sleepy_time)  # wait for x sec
        next_button_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/ \
            div[1]/app-signup/app-username-select-form/form/app-login-signup-button/fl-button/ \
            button')
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            # wait for item to be clickable
        next_button.click()

        ### FREELANCER SELECT ACCOUNT TYPE PAGE ###
        # Test Assertion 3 - new landing page is called "Select account type"
        time.sleep(sleepy_time)  # wait for x sec
        account_type_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        account_type_title = account_type_title_css_selector.text
        self.assertEqual("Select account type", account_type_title, 
            f"Expected 'Select account type' but got '{account_type_title}'")

        # locate and select the account type link
        time.sleep(sleepy_time)  # wait for x sec
        i_want_to_work_xpath = ('/html/body/app-root/app-logged-out-shell/div/app-signup-page/div/ \
            div[1]/app-signup/app-account-type-form/form/fl-radio-card[1]/fl-card/div/div/div/ \
            fl-grid/fl-col[2]/fl-text/div')
        i_want_to_work = wait.until(EC.element_to_be_clickable((By.XPATH, i_want_to_work_xpath)))
            # wait for item to be clickable
        i_want_to_work.click()  # clicking the link

        ### FREELANCER WELCOME PAGE ###
        # Test Assertion 4 - new landing page is called "Welcome to Freelancer!"
        time.sleep(sleepy_time)  # wait for x sec
        welcome_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        welcome_title = welcome_title_css_selector.text
        self.assertEqual("Welcome to Freelancer!", welcome_title,
            f"Expected 'Welcome to Freelancer!' but got '{welcome_title}'")

        # Ensure welcome page has cleared
        while welcome_title == "Welcome to Freelancer!":
            time.sleep(sleepy_time)  # wait for x sec
            welcome_title = self.driver.find_element(By.CSS_SELECTOR, 'h1.ng-star-inserted').text
                # loop until new page loads

        ### FREELANCER SKILLS PAGE ###
        # Test Assertion 5 - new landing page is called "Skills"
        time.sleep(sleepy_time)  # wait for x sec
        skills_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        skills_title = skills_title_css_selector.text
        self.assertEqual("Skills", skills_title, f"Expected 'Skills' but got '{skills_title}'")

        # Search for 'Software Testing' skill
        time.sleep(sleepy_time)  # wait for x sec
        skill_search_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/app-freelancer-onboarding-skills/fl-container/fl-skills/div/div[1]/ \
            div/fl-search/fl-input/div/div/div/input')
        skill_search = wait.until(EC.element_to_be_clickable((By.XPATH, skill_search_xpath)))
            # wait for item to be fillable
        skill_search.send_keys("Software Testing") 

        # Select 'Software Testing' skill
        time.sleep(sleepy_time)  # wait for x sec
        select_skill_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/app-freelancer-onboarding-skills/fl-container/fl-skills/div/div[2]/ \
            fl-skills-category/fl-scrollable-content/fl-list/fl-list-item/div/div/div[1]/div[1]/ \
            div/fl-text/div')
        select_skill = wait.until(EC.element_to_be_clickable((By.XPATH, select_skill_xpath)))
            # wait for item to be fillable
        select_skill.click()

        # Clear search bar
        time.sleep(sleepy_time)  # wait for x sec
        skill_search.clear()

        # Search for 'Python' skill
        time.sleep(sleepy_time)  # wait for x sec
        skill_search_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/app-freelancer-onboarding-skills/fl-container/fl-skills/div/div[1]/ \
            div/fl-search/fl-input/div/div/div/input')
        skill_search = wait.until(EC.element_to_be_clickable((By.XPATH, skill_search_xpath)))
            # wait for item to be fillable
        skill_search.send_keys("Python") 

        # Select 'Python' skill
        time.sleep(sleepy_time)  # wait for x sec
        select_skill_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/app-freelancer-onboarding-skills/fl-container/fl-skills/div/div[2]/ \
            fl-skills-category/fl-scrollable-content/fl-list/fl-list-item/div/div/div[1]/div[1]/ \
            div/fl-text/div')
        select_skill = wait.until(EC.element_to_be_clickable((By.XPATH, select_skill_xpath)))
            # wait for item to be fillable
        select_skill.click()

        # Click next
        time.sleep(sleepy_time)  # wait for x sec
        next_button_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/app-freelancer-onboarding-skills/fl-container/fl-skills/div/div[3]/ \
            fl-button/button')
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            # wait for item to be clickable
        next_button.click()

        ### FREELANCER LINKED ACCOUNTS PAGE ###
        # Test Assertion 6 - new landing page is called "Linked accounts"
        time.sleep(sleepy_time)  # wait for x sec
        linked_accounts_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        linked_accounts_title = linked_accounts_title_css_selector.text
        self.assertEqual("Linked accounts", linked_accounts_title,
            f"Expected 'Linked accounts' but got '{linked_accounts_title}'")
        
        # Skip linking an account
        time.sleep(sleepy_time)  # wait for x sec
        skip_button_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/app-freelancer-onboarding-linked-accounts/fl-container/div/div[2]/ \
            div/fl-link/button')
        skip_button = wait.until(EC.element_to_be_clickable((By.XPATH, skip_button_xpath)))
            # wait for item to be clickable
        skip_button.click()

        ### FREELANCER PROFILE DETAILS PAGE ###
        # Test Assertion 7 - new landing page is called "Profile details"
        time.sleep(sleepy_time)  # wait for x sec
        profile_details_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        profile_details_title = profile_details_title_css_selector.text
        self.assertEqual("Profile details", profile_details_title,
            f"Expected 'Profile details' but got '{profile_details_title}'")

        # Select next
        time.sleep(sleepy_time)  # wait for x sec
        next_button_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/ng-component/fl-container/div/ng-component/div/ \
            app-freelancer-onboarding-profile-details-footer/div/div/fl-button/button')
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            # wait for item to be clickable
        next_button.click()

        ### FREELANCER MORE PROFILE DETAILS PAGE ###
        # Test Assertion 8 - new landing page is called "Profile details"
        time.sleep(sleepy_time)  # wait for x sec
        more_profile_details_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        more_profile_details_title = more_profile_details_title_css_selector.text
        self.assertEqual("Profile details", more_profile_details_title,
            f"Expected 'Profile details' but got '{more_profile_details_title}'")

        # Tell more about yourself
        time.sleep(sleepy_time)  # wait for x sec
        about_yourself_xpath = '//*[@id="inputHeadline"]'
        about_yourself = self.driver.find_element(By.XPATH, about_yourself_xpath)
        about_yourself.send_keys("Python software tester")

        # Describe yourself
        time.sleep(sleepy_time)  # wait for x sec
        describe_yourself_xpath = '//*[@id="inputSummary"]'
        describe_yourself = wait.until(EC.element_to_be_clickable(
            (By.XPATH, describe_yourself_xpath))) # wait for item to be clickable
        describe_yourself.send_keys("I am just a dog, trying to earn some bones in this life and \
            be as happy as I could hope to be eating bones.")

        # Select next
        time.sleep(sleepy_time)  # wait for x sec
        next_button_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/ng-component/fl-container/div/ng-component/div/ \
            app-freelancer-onboarding-profile-details-footer/div/div/fl-button/button')
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            # wait for item to be clickable
        next_button.click()

        ### FREELANCER MORE, MORE PROFILE DETAILS PAGE ###
        # Test Assertion 9 - new landing page is called "Profile details"
        time.sleep(sleepy_time)  # wait for x sec
        more_more_profile_details_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        more_more_profile_details_title = more_more_profile_details_title_css_selector.text
        self.assertEqual("Profile details", more_more_profile_details_title, 
            f"Expected 'Profile details' but got '{more_more_profile_details_title}'")

        # Enter birthdate
        time.sleep(sleepy_time)  # wait for x sec
        birthdate_xpath = '//*[@id="inputBirthdate"]'
        birthdate = wait.until(EC.element_to_be_clickable((By.XPATH, birthdate_xpath)))
            # wait for item to be clickable
        birthdate.send_keys("02/26/1950")

        # Hit 'ESCAPE' key to close calendar popup (blocks selecting next button)
        time.sleep(sleepy_time)  # wait for x sec
        body_element = self.driver.find_element(By.TAG_NAME, 'body')
        body_element.send_keys(Keys.ESCAPE)

        # Select next
        time.sleep(sleepy_time)  # wait for x sec
        next_button_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/ng-component/fl-container/div/ng-component/div/ \
            app-freelancer-onboarding-profile-details-footer/div/div/fl-button/button')
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            # wait for item to be clickable
        next_button.click()

        ### FREELANCER CONFIRM EMAIL PAGE ###
        # Test Assertion 10 - new landing page is called "Email verification"
        time.sleep(sleepy_time)  # wait for x sec
        email_verification_title_css_selector = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1.ng-star-inserted')))
        email_verification_title = email_verification_title_css_selector.text
        self.assertEqual("Email verification", email_verification_title, 
            f"Expected 'Email verification' but got '{email_verification_title}'")
        
        # navigate to dashboard (abort email confirmation)
        time.sleep(sleepy_time)  # wait for x sec
        dashboard_url = 'https://www.freelancer.com/dashboard'
        self.driver.get(dashboard_url)

        ### FREELANCER DASHBOARD PAGE ###
        # NO THANK YOU to notifications popup
        time.sleep(sleepy_time)  # wait for x sec
        notifications_xpath = ('/html/body/app-root/fl-modal/div/div/div/ng-component/div[2]/ \
            fl-button[1]/button')
        notifications = wait.until(EC.element_to_be_clickable((By.XPATH, notifications_xpath)))
            # wait for item to be clickable
        notifications.click()

        # Exit notifications warning popup
        time.sleep(sleepy_time)  # wait for x sec
        warning_xpath = '//*[@id="modalCloseButton"]'
        warning = wait.until(EC.element_to_be_clickable((By.XPATH, warning_xpath)))
            # wait for item to be clickable
        warning.click()
        
        # Minimize messages chatbox
        time.sleep(sleepy_time)  # wait for x sec
        messages_minimize_xpath = ('/html/body/app-root/app-logged-in-shell/div/app-messaging/ \
            app-messaging-inbox-widget/app-messaging-inbox-widget-header/div/div/fl-icon[2]/div')
        messages_minimize = wait.until(EC.element_to_be_clickable(
            (By.XPATH, messages_minimize_xpath))) # wait for item to be clickable
        messages_minimize.click()

        # Test Assertion 11 - new landing page requires: "Email verification required"
        time.sleep(sleepy_time)  # wait for x 
        email_verification_required_xpath = ('/html/body/app-root/app-logged-in-shell/div/div[1]/ \
            app-global-banner/app-verification-banner/app-email-verification-banner/ \
            fl-banner-announcement/div/fl-container/div[2]/div[1]/fl-text[1]/div')
        email_verification_required = wait.until(EC.presence_of_element_located(
            (By.XPATH, email_verification_required_xpath))).text
        self.assertEqual("Email verification required", email_verification_required, 
            f"Expected 'Email verification required' but got '{email_verification_required}'")
        
        # Test Assertion 12 - Username is correct: "@StBernard"+HHMMSS
        time.sleep(sleepy_time)  # wait for x sec
        username_card_xpath = ('/html/body/app-root/app-logged-in-shell/div/div[1]/div/ \
            app-navigation/app-navigation-primary/div/fl-container/fl-callout[4]/ \
            fl-callout-trigger/fl-button/button/app-user-card/div/div/fl-username/div[2]/fl-text/ \
            span')
        username_card = wait.until(EC.presence_of_element_located(
            (By.XPATH, username_card_xpath))).text
        self.assertEqual("@"+username_value, username_card,
            f"Expected @{username_value} but got '{username_card}'")

        # View profile
        time.sleep(sleepy_time)  # wait for x sec
        view_profile_xpath = ('/html/body/app-root/app-logged-in-shell/div/fl-container/main/div/ \
            ng-component/div/app-dashboard-home/fl-page-layout/fl-container/div/ \
            fl-page-layout-primary/app-dashboard-newsfeed/app-newsfeed-items/fl-pull-refresh/ \
            fl-pull-refresh-drawer/div/app-newsfeed-item-activate-freelancer/app-newsfeed-item/ \
            div/div/div[2]/div/fl-grid[2]/fl-col[2]/fl-grid/fl-col[2]/fl-button/a')
        view_profile = wait.until(EC.element_to_be_clickable((By.XPATH, view_profile_xpath)))
            # wait for item to be clickable
        view_profile.click()
        time.sleep(15)
        
        # Print results
        print(f"Account for {username_value} successfully created!")

    @classmethod
    def tearDown(self):
        self.driver.quit() # close the browser window

# Run the main program in the class
if __name__ == '__main__':
    unittest.main(verbosity=2)  # this outputs the report to the IDE's console
