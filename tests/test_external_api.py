from unittest.mock import patch, mock_open
from src.external_api import get_exchange_rate
import os
from dotenv import load_dotenv

# Загрузка переменных окружения для тестирования
load_dotenv()
API_KEY = os.getenv('API_KEY_exchangerate-api')

# Тестовый JSON-файл с валидным списком транзакций
VALID_JSON_DATA = '''
[
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 441945887,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "name": "доллар США",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
]
'''

# Тестовый JSON-файл с транзакциями, не содержащими 'operationAmount'
INVALID_JSON_DATA = '''
[
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
]
'''


def test_get_exchange_rate_rub():
    """
    Тест для валюты "RUB".
    """
    with patch('builtins.open', mock_open(read_data=VALID_JSON_DATA)):
        result = get_exchange_rate("RUB", 'data/operations.json')
        assert result == [31957.58]


def test_get_exchange_rate_usd(mock_api_response):
    """
    Тест для валюты "USD".
    """
    with patch('builtins.open', mock_open(read_data=VALID_JSON_DATA)):
        result = get_exchange_rate("USD", 'data/operations.json')
        assert result == [75.00]
