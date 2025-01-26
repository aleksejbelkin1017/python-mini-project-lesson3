# Модуль masks

# get_mask_card_number:
import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number,expected_result", [
        (4111111111111111, "4111 11** **** 1111"),
        (3782822463100050, "3782 82** **** 0050"),
        (5555555555555550, "5555 55** **** 5550"),
        (5621235686512354, "5621 23** **** 2354")
    ]
)
def test_card_number_positive_cases(card_number, expected_result):
    """Тест проверяет работу функции при вводе корректных данных номера карты"""
    result = get_mask_card_number(card_number)
    assert result == expected_result


def test_card_number_wrong_len():
    """Тест проверяет вызов ошибки при вводе некорректной длины номера карты"""
    with pytest.raises(IndexError) as exc_info:
        get_mask_card_number("1234567890123")
    assert str(exc_info.value) == "Длина номера карты должна быть 16 цифр"


def test_card_number_is_not_digit():
    """Тест проверяет вызов ошибки при вводе букв в значении номера карты"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("abcd1234efgh5678")
    assert str(exc_info.value) == "Номер карты должен состоять только из цифр"


def test_card_number_is_clear():
    """Тест проверяет вызов ошибки при отсутствии номера карты"""
    with pytest.raises(IndexError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Отсутствует обязательный аргумент при вводе номера карты"


# get_mask_account:
@pytest.mark.parametrize(
    "account_number, expected_account_number", [
        (12345678901234567891, "**7891"),
        (37556482822463100050, "**0050"),
        ("abcd12dds34eafgh5678", "**5678"),
        ("SDcs568844sddac53256", "**3256"),
    ]
)
def test_get_mask_account_positive(account_number, expected_account_number):
    """Тест проверяет работу функции при вводе корректных данных номера счёта"""
    result = get_mask_account(account_number)
    assert result == expected_account_number


def test_get_mask_account_wrong_len_account_number():
    """Тест проверяет вызов ошибки при вводе некорректной длины номера счёта"""
    with pytest.raises(IndexError) as exc_info:
        get_mask_account("1234567890123")
    assert str(exc_info.value) == "Длина номера счёта должна быть 20 символов"


def test_get_mask_account_number_is_clear():
    """Тест проверяет вызов ошибки при отсутствии номера счёта"""
    with pytest.raises(IndexError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Отсутствует обязательный аргумент при вводе номера счёта"
