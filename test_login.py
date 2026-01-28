import pytest
import allure
from utils.driver_factory import create_driver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@allure.title("Успешный логин standard_user")
def test_success_login(driver):
    page = LoginPage(driver)
    page.open_page()
    page.login("standard_user", "secret_sauce")

    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_displayed()


@allure.title("Логин с неверным паролем")
def test_invalid_password(driver):
    page = LoginPage(driver)
    page.open_page()
    page.login("standard_user", "wrong_password")

    assert "Username and password do not match" in page.get_error_message()


@allure.title("Логин заблокированного пользователя")
def test_locked_user(driver):
    page = LoginPage(driver)
    page.open_page()
    page.login("locked_out_user", "secret_sauce")

    assert "Sorry, this user has been locked out" in page.get_error_message()


@allure.title("Логин с пустыми полями")
def test_empty_fields(driver):
    page = LoginPage(driver)
    page.open_page()
    page.login("", "")

    assert "Username is required" in page.get_error_message()


@allure.title("Логин performance_glitch_user с задержками")
def test_performance_glitch_user(driver):
    page = LoginPage(driver)
    page.open_page()
    page.login("performance_glitch_user", "secret_sauce")

    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_displayed()
