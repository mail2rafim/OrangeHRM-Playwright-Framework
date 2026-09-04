from playwright.sync_api import expect
import logging

from utilities.logger import get_logger
logger = get_logger()

class LoginPage:
    def __init__(self,page):
        self.page = page

        self.username = page.locator("//input[@name = 'username']")
        self.password = page.locator("//input[@name = 'password']")
        self.login_button = page.locator("//button[@type = 'submit' and text() = ' Login ']")
        self.error_message = page.locator("//p[text() = 'Invalid credentials']")
        self.forgot_password = page.locator("//p[text() = 'Forgot your password? ']")

        logger = logging.getLogger(__name__)


    def login(self,uname, pword):
        logger.info(" Inside login Method ")
        expect(self.username).to_be_visible()
        self.username.fill(uname)
        self.password.fill(pword)
        self.login_button.click()



    def validate_invalidcredentials(self):
        logger.info("Inside validate_invalidcredentials() ")
        expect(self.error_message).to_be_visible()
        return self.error_message.is_visible()



    def is_logged_out(self):
        logger.info("Back to Login-Page, User Logged out successfully")
        return expect(self.username).to_be_visible()





    # def validate_forgotpassword(self):
    #     logger.info(" *** Inside validate_forgotpassword() --- Validation Method **** ")
    #     page.get_by_role("heading", name="Reset Password").click()
    #     page.get_by_role("textbox", name="Username").click()
    #     page.get_by_role("button", name="Cancel").click()
    #     page.get_by_text("Forgot your password?").click()
    #     page.get_by_role("button", name="Reset Password").click()
    #     page.get_by_role("button", name="Reset Password").click()
    #     page.get_by_role("textbox", name="Username").click()
    #     page.get_by_role("textbox", name="Username").click()
    #     page.get_by_role("textbox", name="Username").fill("a")
    #     page.get_by_role("button", name="Reset Password").click()
    #     page.get_by_role("heading", name="Reset Password link sent").click()

        # def __init__(self, page):
    #     self.page = page
    #     self.username = page.locator("//input[@name='username']")
    #     self.password = page.locator("//input[@name='password']")
    #     self.login_button = page.locator("//button[@type='submit' and text() = ' Login ']")
    #
    #
    # # login method
    # def test_login(self, base_url):
    #     logger.info("*** Launching the URL ***")
    #     self.page.goto(base_url)
    #     logger.info("*** Trying to login ***")
    #     self.username.fill("admin")
    #     self.password.fill("admin123")
    #     self.login_button.click()