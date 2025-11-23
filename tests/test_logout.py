# tests/test_logout.py
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MainPageLocators,
    AuthModalLocators,
    AuthentificatedProfileMenuLocators,
)
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestLogout:

    def test_user_can_logout(self, driver, wait):
        # Логин
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.MODAL_ROOT))

        wait.until(EC.visibility_of_element_located(AuthModalLocators.LOGIN_EMAIL_INPUT)).send_keys(
            EXISTING_USER_EMAIL
        )
        driver.find_element(*AuthModalLocators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthModalLocators.LOGIN_SUBMIT_BUTTON).click()

        # Убедиться, что залогинились
        wait.until(EC.visibility_of_element_located(AuthentificatedProfileMenuLocators.PROFILE_PHOTO_ICON))

        # Нажать "Выйти"
        driver.find_element(*AuthentificatedProfileMenuLocators.LOGOUT_BUTTON).click()

        # Проверка: кнопка "Вход и регистрация" снова видна вместо аватара
        header_login_button = wait.until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON)
        )

        assert header_login_button.is_displayed()
