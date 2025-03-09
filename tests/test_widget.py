import pytest

from src.widget import get_date, mask_account_card


# Модуль widget
# mask_account_card:
@pytest.mark.parametrize(
    "type_and_number, expected_positive_result_type_and_number", [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 5694792459608963", "Maestro 5694 79** **** 8963")
    ]
)
def test_mask_account_card_positive(type_and_number, expected_positive_result_type_and_number):
    """Тест проверяет работу маскировки номера карты или счёта при корректно введенных данных"""
    result = mask_account_card(type_and_number)
    assert result == expected_positive_result_type_and_number


def test_mask_account_card_len_card_number_short():
    """Тест проверяет вызов ошибки при вводе номера карты меньше 16 символов"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Visa Platinum 70007922")
    assert str(exc_info.value) == "Длина номера карты должна быть 16 цифр"


def test_mask_account_card_len_card_number_long():
    """Тест проверяет вызов ошибки при вводе номера карты больше 16 символов"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Visa Platinum 70007924564564654654646545643212")
    assert str(exc_info.value) == "Длина номера карты должна быть 16 цифр"


def test_mask_account_card_len_bill_number_short():
    """Тест проверяет вызов ошибки при вводе номера счёта меньше 20 цифр"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет 754")
    assert str(exc_info.value) == "Длина номера счёта должна быть 20 цифр"


def test_mask_account_card_len_bill_number_long():
    """Тест проверяет вызов ошибки при вводе номера счёта больше 20 цифр"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет 754")
    assert str(exc_info.value) == "Длина номера счёта должна быть 20 цифр"


def test_mask_account_card_bill_isdigit():
    """Тест проверяет вызов ошибки при вводе в номере счёта символов отличных от цифр"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет 8754вааgdhfj_)995/ss")
    assert str(exc_info.value) == "Номер должен состоять из цифр"


def test_mask_account_card_card_number_isdigit():
    """Тест проверяет вызов ошибки при вводе в номере карты символов отличных от цифр"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет 85вааgdhfj_)9/ss")
    assert str(exc_info.value) == "Номер должен состоять из цифр"


def test_mask_account_card_clear():
    """Тест проверяет вызов ошибки при вводе в номере карты символов отличных от цифр"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
    assert str(exc_info.value) == "Некорректный формат данных"


# get_data:
# Тестирование правильности преобразования даты.
@pytest.mark.parametrize(
    "user_date, transformation_date", [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-05-26T02:26:18.6714", "26.05.2024"),
        ("2023-11-02T02:26:18.1407", "02.11.2023"),
        ("2005-04-07T02:26:18.671407", "07.04.2005")
    ]
)
def test_get_date_transformation(user_date, transformation_date):
    """Тест проверяет работу функции при вводе корректных значений"""
    result = get_date(user_date)
    assert result == transformation_date


def test_get_date_clear():
    """Тест проверяет работу функции при отсутствии значений"""
    with pytest.raises(TypeError) as exc_info:
        get_date("")
    assert str(exc_info.value) == "Отсутствует обязательный аргумент"


def test_get_date_incorrect_separator():
    """Тест проверяет работу функции при вводе некорректного разделителя даты"""
    with pytest.raises(ValueError) as exc_info:
        get_date("2024/03/11T02:26:18.671407")
    assert str(exc_info.value) == "Некорректный разделитель в дате"
