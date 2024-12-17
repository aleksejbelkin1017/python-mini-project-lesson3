from src.masks import get_mask_card_number, get_mask_account
from typing import Union


def mask_account_card(type_and_number: Union[str]) -> Union[str]:
    """ Функция, которая маскирует номер счета или карты"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for el in type_and_number:
        if el.isalpha() or el.isspace():
            text_result += el
        elif el.isdigit():
            digit_result += el
            digit_count += 1
    if digit_count > 16:
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"


def get_date(user_date: Union[str]) -> Union[str]:
    """Функция, которая получает даты в определенном формате и возвращает в формате ДД.ММ.ГГГГ"""
    # Добавляем импорт библиотеки datetime
    import datetime
    # Преобразуем строку в объект datetime
    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    # Форматируем дату в строку "ДД.ММ.ГГГГ"
    new_date = date_format.strftime("%d.%m.%Y")
    # Возвращаем отформатированную дату
    return new_date


print(mask_account_card("Visa Platinum 1234567891234567"))
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
