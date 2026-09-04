import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.json_reader import read_json

from utilities.logger import get_logger
logger = get_logger()

def test_login(page):
        logger.info("Bismillah Starting OrangeHRM ***")

        page.goto("https://opensource-demo.orangehrmlive.com")

        data = read_json("test_data/employee_data.json")
        fname = data["first_name"]
        lname = data["last_name"]
        role = data["role"]
        status = data["status"]
        emp_name = data["employee_name"]
        username = data["username"]
        password = data["password"]
        login_user = "Admin" #data["login_user"]
        login_password = "admin123" #data["login_password"]


        login_page=LoginPage(page)
        dashboard_page=DashboardPage(page)

        login_page.login(login_user,login_password)
        assert dashboard_page.is_login_successful()
        # dashboard_page.employee_table()

        dashboard_page.add_employee(fname,lname)
        dashboard_page.search_employeebyname(fname)
        dashboard_page.add_user(role,status,emp_name,username,password)
        dashboard_page.logout()
        if login_page.is_logged_out():
            logger.info("Application logged out successfully")
        else:
            logger.info("Application logged out Failed")





        # login_page.login("xyz", "admin123")
        # if (login_page.validate_invalidcredentials()):
        #     print("********  Login attempt was failed, Successfully Validated ********")
        # else:
        #     print("**** User was able to login, Validation Failed ****")
        #

        # assert login_page.validate_invalidcredentials(), \
        #     "Invalid Credentials Validation Failed"


