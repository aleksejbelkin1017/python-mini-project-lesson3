import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_with_correct_data(transactions_to_filter_by_currency_in,
                            transactions_to_filter_by_currency_out_for_rub,
                            transactions_to_filter_by_currency_out_for_usd):
    """Тест принимает корректные исходные данные и фильтрует по указанному заданному пользователем реквизиту currency.
    В тесте рассматриваются два варианта реквизита currency"""
    result_rub = filter_by_currency(transactions_to_filter_by_currency_in, "руб.")
    assert all(transaction == transaction_out for transaction, transaction_out
               in zip(result_rub, transactions_to_filter_by_currency_out_for_rub))
    result_usd = filter_by_currency(transactions_to_filter_by_currency_in, "USD")
    assert all(transaction == transaction_out for transaction, transaction_out
               in zip(result_usd, transactions_to_filter_by_currency_out_for_usd))


def test_filter_by_currency_with_clear_transactions():
    """Тест проверяет вывод ошибки для случаев, когда пользователь не ввел исходные данные"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency(None, "USD")
    assert str(exc_info.value) == "Исходные данные не введены"


def test_filter_by_currency_with_clear_currency(transactions_to_filter_by_currency_in):
    """Тест проверяет вывод ошибки для случаев, когда пользователь не ввел вид валюты"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency(transactions_to_filter_by_currency_in, None)
    assert str(exc_info.value) == "Не выбрана валюта"


def test_transaction_descriptions_with_correct_data(transactions_to_filter_by_currency_in):
    """Тест проверяет для корректно введенных данных значение параметра description для 5 вхождений"""
    result_correct_description = transaction_descriptions(transactions_to_filter_by_currency_in)
    expected_descriptions = (
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    )
    for _ in range(5):
        next_description = next(result_correct_description)
        assert next_description in expected_descriptions


def test_transaction_descriptions_without_any_description(
    transactions_to_transaction_descriptions_without_any_description):
    """Тест проверяет вывод ошибки в случае отсутствия ключа description в транзакции"""
    with pytest.raises(KeyError) as exc_info:
        list(transaction_descriptions(transactions_to_transaction_descriptions_without_any_description))
        assert str(exc_info.value) == "Отсутствует ключ description"


def test_transaction_descriptions_with_clear_transactions():
    """Тест проверяет вывод ошибки в случае отсутствия входных данных"""
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions(None))
    assert str(exc_info.value) == "Исходные данные не введены"