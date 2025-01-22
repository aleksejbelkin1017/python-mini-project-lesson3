def filter_by_currency(transactions, currency):
    return (transaction for transaction in transactions if transaction['operationAmount']['currency']['name'] == currency)


def transaction_descriptions(transactions):
    return (transaction['description'] for transaction in transactions)


def card_number_generator(start_number, end_number):
    for i in range(start_number, end_number + 1):
        card_number = f"{i:016d}"  # Форматирование числа с ведущими нулями (до 12 знаков)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

# Пример входных данных
# Для проверки функций filter_by_currency и transaction_descriptions:
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

# usd_transactions = filter_by_currency(transactions, "руб.")
# for _ in range(2):
#     print(next(usd_transactions))
#
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))

# >>> Перевод организации
#     Перевод со счета на счет
#     Перевод со счета на счет
#     Перевод с карты на карту
#     Перевод организации

# Пример использования генератора card_number_generator
# start_number = 1234567898765432  # Начальное значение
# end_number = 9999999999999999  # Конечное значение

# card_gen = card_number_generator(start_number, end_number)
# print(next(card_gen))
# print(next(card_gen))

for card_number in card_number_generator(1, 5):
    print(card_number)
