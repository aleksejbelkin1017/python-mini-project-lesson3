def filter_by_currency(transactions, currency):
    """Функция принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает
    транзакции, где валюта операции соответствует заданной (например, USD)"""
    if transactions is None:
        raise ValueError("Исходные данные не введены")
    elif currency is None:
        raise ValueError("Не выбрана валюта")
    else:
        return (transaction for transaction in transactions
                if transaction['operationAmount']['currency']['name'] == currency)


def transaction_descriptions(transactions):
    """Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    if transactions is None or not transactions:
        raise ValueError("Исходные данные не введены")
    for transaction in transactions:
        if 'description' in transaction:
            yield transaction['description']
        else:
            raise KeyError("Отсутствует ключ description")


def card_number_generator(start_number, end_number):
    """выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения
    для генерации диапазона номеров."""
    for i in range(start_number, end_number + 1):
        card_number = f"{i:016d}"  # Форматирование числа с ведущими нулями (до 16 знаков)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
