import uuid

# Базовый урл
BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

def generate_unique_email(max_length: int = 20) -> str:
    domain = "@doska.com"
    prefix = "mari_"
    max_unique_len = max_length - len(prefix) - len(domain)
    if max_unique_len <= 0:
        raise ValueError("max_length слишком маленький для такого домена/префикса")

    unique_part = uuid.uuid4().hex[:max_unique_len]
    return f"{prefix}{unique_part}{domain}"

# ДАННЫЕ УЖЕ СУЩЕСТВУЮЩЕГО ПОЛЬЗОВАТЕЛЯ
EXISTING_USER_EMAIL = "mariya_27@gmail.com"
EXISTING_USER_PASSWORD = "111"
