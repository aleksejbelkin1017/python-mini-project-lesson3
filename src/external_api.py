import os

import requests
from dotenv import load_dotenv

from src.utils import transactions_list


def get_exchange_rate(currency, path):
    """
    Функция для получения текущего курса валют относительно RUB.
    currency: строка с кодом валюты (например, 'USD' или 'EUR').
    """
    load_dotenv('.env')
    api_key = os.getenv('API_KEY_exchangerate-api')
    transactions_rub = []
    transactions_currency = []
    converted_amount = []
    transactions = [t for t in transactions_list(path) if t]

    # Проходим по всем транзакциям
    for transaction in transactions:
        # Проверяем наличие ключа 'operationAmount'
        if not transaction:
            print("Пустая транзакция")
            continue
        if 'operationAmount' in transaction and 'currency' in transaction['operationAmount']:
            # Проверяем, если валюта транзакции RUB
            if transaction['operationAmount']['currency']['code'] == currency and currency == "RUB":
                # Добавляем значение ключа 'amount' в список transactions_rub в формате float
                transactions_rub.append(float(transaction['operationAmount']['amount']))
            elif transaction['operationAmount']['currency']['code'] == currency and currency != "RUB":
                transactions_currency.append(float(transaction['operationAmount']['amount']))
        else:
            print(f"Ошибка: ключ 'operationAmount' или 'currency' отсутствует в транзакции {transaction}")
    if currency == "RUB":
        converted_amount = transactions_rub
    else:
        for amount in transactions_currency:
            url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{currency}/RUB/{amount}"
            response = requests.get(url)
            if response.status_code == 200:
                result = response.json()
                converted_amount.append(round(result['conversion_result'], 2))
            else:
                print("Ошибка при запросе API")

    return converted_amount

# if __name__ == '__main__':
#     print(get_exchange_rate("USD", "data/operations.json"))
