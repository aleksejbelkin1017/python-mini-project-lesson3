import re
from collections import Counter


def search_transactions(transactions, search_string):
    """
    Функция для поиска транзакций по описанию

    Параметры:
    transactions (list): список словарей с транзакциями
    search_string (str): строка для поиска

    Возвращает:
    list: список словарей с найденными транзакциями
    """
    # Создаем регулярное выражение с учетом нечувствительности к регистру
    pattern = re.compile(rf'{search_string}', re.IGNORECASE)

    # Фильтруем транзакции, проверяя наличие строки в описании
    result = [
        transaction
        for transaction in transactions
        if pattern.search(transaction.get('description', ''))
    ]

    return result


# # Пример использования
# transactions = [
#     {"id": 1, "amount": 100, "description": "Оплата в магазине электроники"},
#     {"id": 2, "amount": 200, "description": "Перевод другу"},
#     {"id": 3, "amount": 50, "description": "Оплата за интернет"},
#     {"id": 4, "amount": 300, "description": "Покупка в магазине электроники"}
# ]
#
# search_term = "электроники"
#
# found_transactions = search_transactions(transactions, search_term)
#
# for transaction in found_transactions:
#     print(transaction)


def count_transaction_categories(transactions, categories):
    """
    Функция для подсчета количества операций по категориям

    Параметры:
    transactions (list): список словарей с транзакциями
    categories (list): список категорий для подсчета

    Возвращает:
    dict: словарь с количеством операций по каждой категории
    """

    # Создаем счетчик для подсчета категорий
    category_counter = Counter()

    # Проходим по всем транзакциям
    for transaction in transactions:
        description = transaction.get('description', '')

        # Проверяем, есть ли описание в списке категорий
        for category in categories:
            if category.lower() in description.lower():
                category_counter[category] += 1
                break  # Если нашли категорию, переходим к следующей транзакции

    # Создаем итоговый словарь с категориями
    result = {category: category_counter[category] for category in categories}

    return result


# # Пример использования
# transactions = [
#     {"id": 1, "amount": 100, "description": "Оплата в магазине электроники"},
#     {"id": 2, "amount": 200, "description": "Перевод другу"},
#     {"id": 3, "amount": 50, "description": "Оплата за интернет"},
#     {"id": 4, "amount": 300, "description": "Покупка в магазине электроники"},
#     {"id": 5, "amount": 150, "description": "Перевод коллеге"},
# ]
#
# categories = ["электроника", "перевод", "интернет"]
#
# result = count_transaction_categories(transactions, categories)
# print(result)  # Вывод: {'электроника': 2, 'перевод': 2, 'интернет': 1}