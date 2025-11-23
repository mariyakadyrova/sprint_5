from selenium.webdriver.common.by import By

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"


class MainPageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Вход и регистрация']")
    TRY_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Применить']")
    PLACE_ADD = (By.XPATH, "//button[@type='button' and normalize-space()='Разместить объявление']")

class AuthModalLocators:
    # Модальное окно авторизации/регистрации
    MODAL_ROOT = (By.XPATH, "//form[contains(@class,'popUp_shell')]")
     # Вкладки/кнопки
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Нет аккаунта']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Войти']")

    # Поля авторизации
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    # Ошибка под полем Email
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[normalize-space()='Логин или пароль неверны']")
    REGISTER_EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[contains(@class,'input_span') and normalize-space()='Ошибка']")

    # Поля регистрации
    REGISTER_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='password']")
    REGISTER_REPEAT_PASSWORD_INPUT = (By.XPATH, "//input[@name='submitPassword']")

    # Кнопки создать акк и есть акк
    REGISTER_TAB_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Создать аккаунт']")
    ALREDY_EXIST_ACCOUNT_TAB_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Уже есть аккаунт']")


class AdFormLocators:
    # страница создания объявления
    #AD_FORM_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Разместить объявление']")

    TITLE_INPUT = (By.XPATH, "//input[@placeholder='Название' and @name='name']")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.XPATH, "//input[@type='title' or @placeholder='Стоимость']")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")

    # выбираю СПБ
    CITY_DROPDOWN_SPB = (By.XPATH, "//span[normalize-space()='Санкт-Петербург']/ancestor::button[1]")
    # выбор садовода
    DROPDOWN_FIRST_OPTION = (By.XPATH, "//span[normalize-space()='Садоводство']/ancestor::button[1]")
    # Радио-кнопки состояния товара (новый & б/у)
    CONDITION_NEW_RADIO = (By.XPATH, "//span[normalize-space()='Новый']/preceding-sibling::div[contains(@class,'radioUnput_inputRegular')]")
    CONDITION_USED_RADIO = (By.XPATH, "//label[normalize-space()='Б/У']"
    "/preceding-sibling::div[contains(@class,'radioUnput_inputRegular')]")

    PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Опубликовать']")



class ProfilePageLocators:
    MY_ADS_BLOCK = (By.XPATH, "//h1[normalize-space()='Мои объявления']")
    # Карточка объявления по названию
    LAST_AD_TITLE = (
        By.XPATH,
        "(//div[contains(@class,'card')]//h2[@class='h2'])[last()]"
    )


class AdAuthModalLocators:
    # алертовая модалка при попытке разместить объявление без авторизации
    AUTH_REQUIRED_MODAL = (By.XPATH, "//form[contains(@class,'popUp_shell')]")
    AUTH_REQUIRED_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']"
    )

## локатор лоя логаута  и иконки аккаунта
class AuthentificatedProfileMenuLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Выйти']")
    PROFILE_PHOTO_ICON = (By.XPATH, "//button[contains(@class,'circleSmall')]")

