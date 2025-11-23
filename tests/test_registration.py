import pytest
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, AuthModalLocators, AuthentificatedProfileMenuLocators
from data import generate_unique_email, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestRegistration:

    def test_successful_registration_new_user(self, driver, wait):
        # Открыть форму регистрации
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.MODAL_ROOT))
        wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()

        # Заполнить форму
        email = generate_unique_email()
        password = "Qq112233"

        wait.until(EC.visibility_of_element_located(AuthModalLocators.REGISTER_EMAIL_INPUT)).send_keys(email)
        driver.find_element(*AuthModalLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthModalLocators.REGISTER_REPEAT_PASSWORD_INPUT).send_keys(password)

        driver.find_element(*AuthModalLocators.REGISTER_TAB_BUTTON).click()
        wait.until(EC.invisibility_of_element_located(AuthModalLocators.MODAL_ROOT))

        # Проверка что на главной видим иконку фото
        wait.until(EC.visibility_of_element_located(AuthentificatedProfileMenuLocators.PROFILE_PHOTO_ICON))


    def test_registration_with_invalid_email_mask(self, driver, wait):
        # Открыть форму регистрации
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.MODAL_ROOT))
        wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()

        # Ввести только неправильный email и нажать "Создать аккаунт"
        invalid_email = "wrong_email"
        password = "1122"
        wait.until(EC.visibility_of_element_located(AuthModalLocators.REGISTER_EMAIL_INPUT)).send_keys(invalid_email)
        driver.find_element(*AuthModalLocators.REGISTER_TAB_BUTTON).click()

        # Проверка: сообщение "Ошибка" под email
        error_element = wait.until(
            EC.visibility_of_element_located(AuthModalLocators.REGISTER_EMAIL_ERROR_MESSAGE)
        )

        assert error_element.text.strip() == "Ошибка"


    def test_registration_existing_user(self, driver, wait):
        # Открыть форму регистрации
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.MODAL_ROOT))
        wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()

        # Заполнить форму существующим пользователем
        wait.until(EC.visibility_of_element_located(AuthModalLocators.REGISTER_EMAIL_INPUT)).send_keys(
            EXISTING_USER_EMAIL
        )
        driver.find_element(*AuthModalLocators.REGISTER_EMAIL_INPUT).send_keys("User")
        driver.find_element(*AuthModalLocators.REGISTER_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthModalLocators.REGISTER_REPEAT_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        driver.find_element(*AuthModalLocators.REGISTER_TAB_BUTTON).click()

        error_element = wait.until(
            EC.visibility_of_element_located(AuthModalLocators.REGISTER_EMAIL_ERROR_MESSAGE)
        )

        assert error_element.text.strip() == "Ошибка"
