def filter_by_currency(transactions, currency):
    if transactions == None:
        raise ValueError("Исходные данные не введены")
    elif currency == None:
        raise ValueError("Не выбрана валюта")
    else:
        return (transaction for transaction in transactions if transaction['operationAmount']['currency']['name'] == currency)


def transaction_descriptions(transactions):
    if transactions is None or not transactions:
        raise ValueError("Исходные данные не введены")
    for transaction in transactions:
        if 'description' in transaction:
            yield transaction['description']
        else:
            raise KeyError("Отсутствует ключ description")


def card_number_generator(start_number, end_number):
    for i in range(start_number, end_number + 1):
        card_number = f"{i:016d}"  # Форматирование числа с ведущими нулями (до 16 знаков)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
