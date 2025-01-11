from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: Union[str]) -> Union[str]:
    """Функция, которая маскирует номер счета или карты"""
    type = type_and_number[: type_and_number.rfind(" ")]
    number = type_and_number[type_and_number.rfind(" ") + 1 :]
    if type_and_number == "":
        raise ValueError("Данные не введены")
    if not number.isdigit():
        raise ValueError("Номер должен состоять из цифр")
    if "счет" in type.lower() or "счёт" in type.lower():
        if len(number) != 20:
            raise IndexError("Длина номера счёта должна быть 20 цифр")
        elif len(number) == 20:
            return f"{type} {get_mask_account(number)}"
    elif len(number) != 16:
        raise IndexError("Длина номера карты должна быть 16 цифр")
    elif len(number) == 16:
        return f"{type} {get_mask_card_number(number)}"


def get_date(user_date: str) -> str:
    """Функция принимает строку и возвращает в формате ДД.ММ.ГГГГ"""
    if user_date == "":
        raise TypeError("Отсутствует обязательный аргумент")
    if user_date.count("-") == 0:
        raise ValueError("Некорректный разделитель в дате")
    data_slize = user_date[0:10].split("-")
    return ".".join(data_slize[::-1])


# print(mask_account_card("Visa Platinum 7000795555565522"))
# print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
