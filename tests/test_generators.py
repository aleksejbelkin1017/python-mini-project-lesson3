import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


@pytest.mark.parametrize("start, end, expected_length",
                         [(1000, 1010, 11),
                          (5000, 5010, 11),
                          (9000, 9010, 11)])
def test_card_number_generator_range(start, end, expected_length):
    """Тест на генерацию номеров карт в заданном диапазоне"""
    card_numbers = list(card_number_generator(start, end))
    # количество карт в указанном диапазоне номеров
    assert len(card_numbers) == expected_length
    # 16 цифр и 3 пробела между 4 блоками по 4 цифры
    assert all(len(card_number) == 19 for card_number in card_numbers)


@pytest.mark.parametrize("card_number_input, expected_format", [
    (1234567890123456, "1234 5678 9012 3456"),
    (1234567890123457, "1234 5678 9012 3457"),
    (1234567890123458, "1234 5678 9012 3458"),
    (1234567890123459, "1234 5678 9012 3459"),
    (1234567890123460, "1234 5678 9012 3460")
])
def test_card_number_format(card_number_input, expected_format):
    """Тест на формат номеров карт"""
    generated_cards = list(card_number_generator(card_number_input, card_number_input))
    assert all(generated_card == expected_format for generated_card in generated_cards)
