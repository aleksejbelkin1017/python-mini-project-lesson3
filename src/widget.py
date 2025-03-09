from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: Union[str]) -> Union[str, None]:
    """Функция, которая маскирует номер счета или карты"""
    if not isinstance(type_and_number, str) or " " not in type_and_number:
        raise ValueError("Некорректный формат данных")

    type_new = type_and_number[:type_and_number.rfind(" ")]
    number = type_and_number[type_and_number.rfind(" ") + 1:]

    # Проверка на пустую строку
    if not number:
        raise ValueError("Номер не может быть пустым")

    if not number.isdigit():
        raise ValueError("Номер должен состоять из цифр")

    if "счет" in type_new.lower() or "счёт" in type_new.lower():
        if len(number) != 20:
            raise ValueError("Длина номера счёта должна быть 20 цифр")
            return f"{type_new} Неверная длина номера счёта"
        return f"{type_new} {get_mask_account(number)}"
    else:
        if len(number) != 16:
            raise ValueError("Длина номера карты должна быть 16 цифр")
            return f"{type_new} Неверная длина номера карты"
        return f"{type_new} {get_mask_card_number(number)}"

    return None


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
