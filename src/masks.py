import logging
from typing import Union

logger = logging.getLogger('masks.py')
file_handler = logging.FileHandler('logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:\n%(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Принимает на вход номер карты и возвращает её маску.
    Видны первые 6 цифр и последние 4 цифры. Остальные символы отображаются *.
    Номер разбит по блокам по 4 цифры."""
    logger.info(f'Запущена функция get_mask_card_number.\nВходные данные: {card_number}')
    # # преобразуем принятый номер карты к строке
    card_number = str(card_number)
    logger.info(f'Входные данные приведены к типу данных str')
    # # наносим маску на номер карты
    # mask_number = card_number.replace(card_number[6:-4], "*" * len(card_number[6:-4]))
    # # разбиваем замаскированный номер на блоки по 4 символа
    # card_blocks = mask_number[:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:]
    # return card_blocks
    if card_number == "":
        logger.error(f'Ошибка: "Отсутствует обязательный аргумент при вводе номера карты"')
        logger.debug(f'Необходимо ввести номер карты')
        raise IndexError("Отсутствует обязательный аргумент при вводе номера карты")
    elif len(card_number) != 16:
        logger.error(f'Ошибка: "Длина номера карты должна быть 16 цифр"')
        logger.debug(f'Необходимо изменить длину номера карты. Фактическая длина номера карты {len(card_number)}')
        raise IndexError("Длина номера карты должна быть 16 цифр")
    elif not card_number.isdigit():
        logger.error(f'Ошибка: "Номер карты должен состоять только из цифр"')
        logger.debug(f'Необходимо исключить символы отличные от цифр из номера карты')
        raise ValueError("Номер карты должен состоять только из цифр")
    logger.info(f'Выполнение функции get_mask_card_number успешно завершено')
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Принимает на вход номер счёта и возвращает его маску.
    Номер счёта возвращается в виде ** и 4 последние цифры."""
    logger.info(f'Запущена функция get_mask_account.\nВходные данные: {account_number}')
    # преобразуем принятый номер счёта к строке
    account_number = str(account_number)
    logger.info(f'Входные данные приведены к типу данных str')
    # наносим маску на номер счёта
    if account_number == "":
        logger.error(f'Ошибка: "Отсутствует обязательный аргумент при вводе номера счёта"')
        logger.debug(f'Необходимо ввести номер счёта')
        raise IndexError("Отсутствует обязательный аргумент при вводе номера счёта")
    elif len(account_number) != 20:
        logger.error(f'Ошибка: "Длина номера счёта должна быть 20 символов"')
        logger.debug(f'Необходимо изменить длину номера счёта. Фактическая длина номера карты {len(account_number)}')
        raise IndexError("Длина номера счёта должна быть 20 символов")
    else:
        mask_number = "**" + account_number[-4:]
        logger.info(f'Выполнение функции get_mask_account успешно завершено')
        return mask_number


# print(get_mask_card_number("1234567sd891234s"))
# print(get_mask_account(12345678901234567891))
