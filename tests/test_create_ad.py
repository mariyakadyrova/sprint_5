from selenium.webdriver.support import expected_conditions as EC
import time

from locators import (
    MainPageLocators,
    AuthModalLocators,
    AdFormLocators,
    AdAuthModalLocators,
    ProfilePageLocators,
    AuthentificatedProfileMenuLocators,
)
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestCreateAd:

    def test_create_ad_unauthorized_shows_auth_modal(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.PLACE_ADD)).click()

        modal = wait.until(
            EC.visibility_of_element_located(AdAuthModalLocators.AUTH_REQUIRED_MODAL)
        )
        title = wait.until(
            EC.visibility_of_element_located(AdAuthModalLocators.AUTH_REQUIRED_TITLE)
        )

        assert "Чтобы разместить объявление, авторизуйтесь" in title.text

    def test_create_ad_authorized_user(self, driver, wait):
        # Логин
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.MODAL_ROOT))

        wait.until(EC.visibility_of_element_located(AuthModalLocators.LOGIN_EMAIL_INPUT)).send_keys(
            EXISTING_USER_EMAIL
        )
        driver.find_element(*AuthModalLocators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthModalLocators.LOGIN_SUBMIT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthentificatedProfileMenuLocators.PROFILE_PHOTO_ICON))

        # Открыть форму создания объявления
        wait.until(EC.element_to_be_clickable(MainPageLocators.PLACE_ADD)).click() # далее переход на страницу заполнения надо подождать

        # Данные объявления
        title_text = "Вишневый пирог"
        description_text = "Рецепт вкусный"
        price_text = "5000"

        title_element = wait.until(EC.visibility_of_element_located(AdFormLocators.TITLE_INPUT))
        # скролимся:
        driver.execute_script("arguments[0].scrollIntoView(true);", title_element)
        title_element.send_keys(title_text)

        driver.find_element(*AdFormLocators.DESCRIPTION_TEXTAREA).send_keys(description_text)
        driver.find_element(*AdFormLocators.PRICE_INPUT).send_keys(price_text)

        # Категория
        driver.find_element(*AdFormLocators.CATEGORY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(AdFormLocators.DROPDOWN_FIRST_OPTION)).click()

        # Город
        driver.find_element(*AdFormLocators.CITY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(AdFormLocators.CITY_DROPDOWN_SPB)).click()

        # Состояние товара
        driver.find_element(*AdFormLocators.CONDITION_USED_RADIO).click()

        # Опубликовать
        driver.find_element(*AdFormLocators.PUBLISH_BUTTON).click()
        time.sleep(2)

        # Перейти в профиль пользователя
        photo_element = wait.until(EC.visibility_of_element_located(AuthentificatedProfileMenuLocators.PROFILE_PHOTO_ICON))
        driver.execute_script("arguments[0].scrollIntoView(true);", photo_element)
        photo_element.click()


        # Ожидание блока "Мои объявления" и нашего объявления
        title_text = "5 000 ₽"
        my_ads_block = wait.until(EC.visibility_of_element_located(ProfilePageLocators.MY_ADS_BLOCK))
        driver.execute_script("arguments[0].scrollIntoView(true);", my_ads_block)
        last_title_el = wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.LAST_AD_TITLE)
        )
        assert last_title_el.text == title_text

