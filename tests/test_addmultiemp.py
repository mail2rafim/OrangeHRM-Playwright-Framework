import pytest
from utilities.json_reader import read_json
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.parametrize("employee", read_json("test_data/employee_data_multi.json"))
def test_add_employee(logged_in_page, employee):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.add_employee(employee["first_name"],employee["last_name"])
    dashboard_page.search_employeebyname(employee["first_name"])