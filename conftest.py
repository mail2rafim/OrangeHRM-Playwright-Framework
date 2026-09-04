import pytest
from playwright.sync_api import sync_playwright

from pages.dashboard_page import logger
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def logged_in_page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=500)
        context = browser.new_context(viewport=None)
        page = context.new_page()
        logger.info("Browser Launched")

        login_page = LoginPage(page)
        page.goto("https://opensource-demo.orangehrmlive.com")
        login_page.login("admin","admin123")

        yield page
        logger.info("Browser Closed")
        browser.close()


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=500)
        context = browser.new_context(viewport=None)
        page = context.new_page()
        logger.info("Browser Launched")

        # login_page = LoginPage(page)
        # page.goto("https://opensource-demo.orangehrmlive.com")
        # login_page.login("admin","admin123")

        yield page
        logger.info("Browser Closed")
        browser.close()