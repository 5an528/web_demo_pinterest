from selenium.webdriver.common.by import By


class SignupLoginPageLocators(object):
    LOGIN_BUTTON = (By.XPATH, "//div[@class='tBJ dyH iFc yTZ erh tg7 mWe']")
    SIGN_UP_BUTTON = (By.XPATH, '//div[@class="tBJ dyH iFc yTZ pBj tg7 mWe"]')

    # Login By Email
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    PASS_INPUT = (By.XPATH, "//input[@id='password']")

    # Signup By Email
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SUBMIT_BUTTON = (By.XPATH, "//div[@data-test-id='registerFormSubmitButton']")

    # Login/Signup By Facebook
    FB_BUTTON = (By.XPATH, "//div[@data-test-id='facebook-connect-button']")
    FB_EMAIL = (By.XPATH, "//input[@id='email']")
    FB_PASS = (By.XPATH, "//input[@id='pass']")
    FB_SUBMIT = (By.XPATH, "//input[@name='login']")

    # Login/Signup By Google
    G_BUTTON = (By.XPATH, "//div[@data-test-id='google-connect-button']")


class HomePageLocators(object):
    LOGO_TEXT = (By.XPATH, "//h1[text()='Pinterest']")
    # After Login
    LOGO = (By.XPATH, "//a[@aria-label='Home']")
    HOME = (By.XPATH, "//span[@class='tBJ dyH iFc yTZ erh tg7 mWe']")
    SEARCH = (By.XPATH, "//input[@aria-label='Search']")
    NOTIFICATION = (By.XPATH, "//button[@aria-label='Notifications']")
    MESSAGES = (By.XPATH, "//button[@aria-label='Messages']")
    PROFILE = (By.XPATH, "//div[@class='zI7 iyn Hsu']/ul/div")
    MESSAGES_BOX = (By.XPATH, "//textarea[@id='messageDraft']")
    # Profile
    PROFILE_BUTTON = (By.XPATH, "//div[@data-test-id='header-profile']")
    PROFILE_EDIT_BUTTON = (By.XPATH, "//div[text()='Edit Profile']")
    PROFILE_SHARE_BUTTON = (By.XPATH, "//div[text()='Share']")
    # Help Center
    QUESTION_MARK = (By.XPATH, "//div[@class='JME wc1 zI7 iyn Hsu']/div/button[@aria-label='More']")
    PLUS = (By.XPATH, "//div[@class='JME wc1 zI7 iyn Hsu']/div/button[@aria-label='Add Pin']")
    CREATE_PIN = "//div[@title='Create a Pin']"
    VISIT_HELP_CENTER = (By.XPATH, "//div[@title='Visit the Help Center']")
    GET_OUR_BROWSER = (By.XPATH, "//div[@title='Get our browser button to save ideas even faster']")
    ABOUT = (By.XPATH, "//div[text()='About']")


class AdsPageLocators(object):
    BANNER_TEXT = (By.XPATH, "//p[@class='unauth-homepage-use-case-fashion']")
    PROFILE = (By.XPATH, "//a[@class='Wk9 xQ4 CCY czT INd iyn kVc FTD L4E DI9 BG7']")


class PostPageLocators(object):
    POST_ITEM = (By.XPATH, "//div[@class='Yl- MIw Hb7']")
    POST_DOT = (By.XPATH, "//div[@data-test-id='lego-icon-wrapper']")
    POST_SHARE = (By.XPATH, "//div[@data-test-id='lego-icon-wrapper']")
    POST_LOVE = (By.XPATH, "//div[@data-test-id='reactions-likeWithCountButton']")
    SAVE = (By.XPATH, "//div[@class='tBJ dyH iFc yTZ erh tg7 mWe']")
    FOLLOW = (By.XPATH, "//div[@data-test-id='user-follow-button']")

    COMMENT = (By.XPATH, "//textarea[@data-test-id='communityItemTextBox']")
    REPLY = (By.XPATH, "//div[@data-test-id='reactions-reply']")
