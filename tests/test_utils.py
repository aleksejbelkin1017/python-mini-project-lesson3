import json
from unittest.mock import patch, mock_open
import pytest
from src.utils import transactions_list

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
  }
]
'''

# Тестовый JSON-файл с данными, которые не являются списком
INVALID_JSON_DATA = '''
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
}
'''

# Пустой JSON-файл
EMPTY_JSON_DATA = '[]'

def test_transactions_list_valid_data():
    """
    Тест для валидного JSON-файла с списком транзакций.
    """
    with patch('builtins.open', mock_open(read_data=VALID_JSON_DATA)):
        result = transactions_list('data/operations.json')
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['id'] == 441945886

def test_transactions_list_invalid_data():
    """
    Тест для JSON-файла, который содержит не список.
    """
    with patch('builtins.open', mock_open(read_data=INVALID_JSON_DATA)):
        result = transactions_list('data/operations.json')
        assert result == []

def test_transactions_list_empty_file():
    """
    Тест для пустого JSON-файла.
    """
    with patch('builtins.open', mock_open(read_data=EMPTY_JSON_DATA)):
        result = transactions_list('data/operations.json')
        assert result == []

def test_transactions_list_file_not_found():
    """
    Тест для случая, когда файл не найден.
    """
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = transactions_list('data/operations.json')
        assert result == []

def test_transactions_list_json_decode_error():
    """
    Тест для случая, когда происходит ошибка JSON-декодирования.
    """
    with patch('builtins.open', mock_open(read_data='{invalid json')):
        result = transactions_list('data/operations.json')
        assert result == []