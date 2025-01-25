from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Принимает на вход номер карты и возвращает её маску.
    Видны первые 6 цифр и последние 4 цифры. Остальные символы отображаются *.
    Номер разбит по блокам по 4 цифры."""

    # # преобразуем принятый номер карты к строке
    card_number = str(card_number)
    # # наносим маску на номер карты
    # mask_number = card_number.replace(card_number[6:-4], "*" * len(card_number[6:-4]))
    # # разбиваем замаскированный номер на блоки по 4 символа
    # card_blocks = mask_number[:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:]
    # return card_blocks
    if card_number == "":
        raise IndexError("Отсутствует обязательный аргумент при вводе номера карты")
    elif len(card_number) != 16:
        raise IndexError("Длина номера карты должна быть 16 цифр")
    elif not card_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Принимает на вход номер счёта и возвращает его маску.
    Номер счёта возвращается в виде ** и 4 последние цифры."""
    # преобразуем принятый номер счёта к строке
    account_number = str(account_number)
    # наносим маску на номер счёта
    if account_number == "":
        raise IndexError("Отсутствует обязательный аргумент при вводе номера счёта")
    elif len(account_number) != 20:
        raise IndexError("Длина номера счёта должна быть 20 символов")
    else:
        mask_number = "**" + account_number[-4:]
        return mask_number


# print(get_mask_card_number("1234567890123"))
# print(get_mask_account(12345678901234567891))
