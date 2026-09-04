from playwright.sync_api import expect
from utilities.logger import get_logger
logger = get_logger()

class DashboardPage:
    def __init__(self, page):
        self.page=page

        self.dashboard = page.locator("//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Dashboard']")
        self.user_menu = page.locator("//p[@class = 'oxd-userdropdown-name']")
        self.user_menu_logout = page.locator("//a[@class = 'oxd-userdropdown-link' and text() = 'Logout']")
        self.admin_menu = page.locator("//span[text() ='Admin']")
        self.add_btn = page.locator("//button[text()=' Add ']")
        self.user_role_dropdown = page.locator("//label[text()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text-input')]")
        self.status_dropdown = page.locator("//label[text() ='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text--active')]")
        self.Employee_name = page.locator("//label[text() ='Employee Name']/ancestor::div[contains(@class,'oxd-input-group')]//input[@placeholder = 'Type for hints...']")
        self.emp_id = page.locator("//label[text() ='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input[@class='oxd-input oxd-input--active']")
        self.username = page.locator("//label[text() ='Username']/ancestor::div[contains(@class,'oxd-input-group oxd-input')]//input[@class= 'oxd-input oxd-input--active']")
        self.password = page.locator("//label[text() ='Password']/ancestor::div[contains(@class,'oxd-input-group oxd-input')]//input[@class= 'oxd-input oxd-input--active']")
        self.confirm_password = page.locator("//label[text() ='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group oxd-input')]//input[@class= 'oxd-input oxd-input--active']")
        self.cancel_btn = page.locator("//button[@type='button' and text()=' Cancel ']")
        self.save_btn = page.locator("//button[@type='submit' and text()=' Save ']")
        self.pim_menu = page.locator("//span[text() ='PIM']")
        self.f_name = page.locator("//input[@placeholder = 'First Name']")
        self.l_name = page.locator("//input[@placeholder = 'Last Name']")
        self.search_btn = page.locator("//button[@type='submit']")

        self.emp_table = page.locator("xpath=//div[@role='table']")
        self.emp_table_rows = page.locator("xpath=.//div[@role='row']")
        self.emp_table_col = page.locator("xpath=.//div[@role='table']")
        self.emp_table_cell = page.locator("xpath=.//div[@role='cell']")
        self.emp_table_header = page.locator("xpath=.//div[contains(@class,'oxd-table-header-cell')]")
        self.no_records_found = page.locator("//span[text() = 'No Records Found']")




    def is_login_successful(self):
        logger.info("Inside Dashboard-Page  Login Successful")
        expect(self.dashboard).to_be_visible()
        logger.info("Page title is: %s", self.page.title())
        return self.dashboard.is_visible()

    def logout(self):
        logger.info("Inside Dashboard-Page, logging out the User")
        expect(self.user_menu).to_be_visible()
        self.user_menu.click()
        self.user_menu_logout.click()

         # role,status,emp_name,uname,pword
    def add_user(self ,role,status,emp_name,username,password):
        logger.info("Inside Add-User()")
        expect(self.admin_menu).to_be_visible()
        self.admin_menu.click()
        self.add_btn.click()
        self.select_user_role(role)
        self.select_status(status)
        self.Employee_name.fill(emp_name)
        self.page.get_by_text(emp_name).first.click()
        self.username.fill(username)
        self.password.fill(password)
        self.confirm_password.fill(password)
        self.save_btn.click()
        # self.page.pause()

    def add_employee(self, fname,lname):
        logger.info("Inside Add-Employee()")
        expect(self.pim_menu).to_be_visible()
        self.pim_menu.click()
        expect(self.add_btn).to_be_visible()
        self.add_btn.click()
        self.f_name.fill(fname)
        self.l_name.fill(lname)
        self.save_btn.click()

    def select_user_role(self, role):
        logger.info("Selecting User Role : %s", role)
        self.user_role_dropdown.click()
        self.page.locator(f"//*[text()='{role}']").click()

    def select_status(self, status):
        logger.info("Selecting Status : %s", status)
        self.status_dropdown.click()
        self.page.locator(f"//*[text()='{status}']").click()

    def search_employeebyname(self,emp_name):
        logger.info(f"Searching Employee : {emp_name}")
        expect(self.pim_menu).to_be_visible()
        self.pim_menu.click()
        self.Employee_name.fill(emp_name)
        self.search_btn.click()
        expect(self.emp_table_rows.first).to_be_visible()

        if self.no_records_found.is_visible():
            logger.info(f"Employee Validation Failed, Not Found : {emp_name}")
            raise AssertionError(f"Employee '{emp_name}' not found"           )
        else:
            row = self.emp_table_rows.nth(1)
            cells = row.locator("xpath=.//div[@role='cell']")
            cell_content = cells.nth(2).text_content().strip()
            logger.info("Expected : %s", emp_name)
            logger.info("Actual : %s", cell_content)
            assert cell_content == emp_name, "User Not Found"
            logger.info("Employee Validation Successful")



    def employee_table(self):
        logger.info("First Table Excercise, Displaying Employee Table Details")
        expect(self.pim_menu).to_be_visible()
        self.pim_menu.click()
        expect(self.emp_table).to_be_visible()
        expect(self.emp_table_rows.first).to_be_visible()
        rows=self.emp_table_rows.count()
        cols=self.emp_table_header.count()

        logger.info(f"No of Rows : {rows}")
        logger.info(f"No of Columns : {cols}")

        for i in range(cols):
            txt= self.emp_table_header.nth(i).text_content()
            logger.info(txt)

        for r in range(1, self.emp_table_rows.count()):
            row = self.emp_table_rows.nth(r)
            cells = row.locator("xpath=.//div[@role='cell']")
            logger.info("========== ROW %s ==========",r)
            for c in range(cells.count()):
                logger.info(cells.nth(c).text_content())



















