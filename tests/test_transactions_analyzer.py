import pytest
from src.transactions_analyzer import search_transactions, count_transaction_categories
from collections import Counter

def test_exact_match(transactions):
    """
    Тест на точное совпадение с искомой строкой

    Проверяет:
    - Нахождение всех транзакций с точным совпадением
    - Корректность возвращаемых результатов
    """
    result = search_transactions(transactions, "электроники")
    assert len(result) == 2
    assert {"id": 1, "amount": 100, "description": "Оплата в магазине электроники"} in result
    assert {"id": 4, "amount": 300, "description": "Покупка в магазине электроники"} in result


def test_case_insensitive(transactions):
    """
    Тест на нечувствительность к регистру

    Проверяет:
    - Поиск транзакций с учетом регистра
    - Корректность результатов при разных регистрах
    """
    result = search_transactions(transactions, "ПЕРЕВОД")
    assert len(result) == 2
    assert {"id": 2, "amount": 200, "description": "Перевод другу"} in result
    assert {"id": 5, "amount": 150, "description": "Перевод коллеге"} in result


def test_no_matches(transactions):
    """
    Тест на отсутствие совпадений

    Проверяет:
    - Возвращает пустой список при отсутствии совпадений
    - Корректность обработки несуществующей категории
    """
    result = search_transactions(transactions, "несуществующая категория")
    assert len(result) == 0


def test_partial_match(transactions):
    """
    Тест на частичное совпадение

    Проверяет:
    - Поиск по части строки в описании
    - Корректность результатов при частичном совпадении
    """
    result = search_transactions(transactions, "оплата")
    assert len(result) == 2
    assert {"id": 1, "amount": 100, "description": "Оплата в магазине электроники"} in result
    assert {"id": 3, "amount": 50, "description": "Оплата за интернет"} in result


def test_empty_transactions():
    """
    Тест на пустой список транзакций

    Проверяет:
    - Обработку пустого списка транзакций
    - Возвращает пустой список
    """
    empty_transactions = []
    result = search_transactions(empty_transactions, "электроника")
    assert len(result) == 0


def test_missing_description():
    """
    Тест на транзакции без описания

    Проверяет:
    - Обработку транзакций без поля description
    - Корректность результатов
    """
    transactions_without_description = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200, "description": "Перевод другу"},
    ]
    result = search_transactions(transactions_without_description, "перевод")
    assert len(result) == 1


# Тестовые данные
transactions = [
    {"id": 1, "amount": 100, "description": "Оплата в магазине электроника"},
    {"id": 2, "amount": 200, "description": "Перевод другу"},
    {"id": 3, "amount": 50, "description": "Оплата за интернет"},
    {"id": 4, "amount": 300, "description": "Покупка в магазине электроника"},
    {"id": 5, "amount": 150, "description": "Перевод коллеге"},
]


@pytest.mark.parametrize("categories, expected", [
    (["электроника", "перевод", "интернет"], {"электроника": 2, "перевод": 2, "интернет": 1}),
    (["электроника", "перевод"], {"электроника": 2, "перевод": 2}),
    (["перевод", "интернет"], {"перевод": 2, "интернет": 1}),
    (["электроника"], {"электроника": 2}),
    (["несуществующая"], {"несуществующая": 0}),
    ([], {}),
])
def test_count_transaction_categories(categories, expected):
    """
    Тест проверяет базовое функционирование функции с различными наборами категорий.

    Проверяет:
    - Корректность подсчета для разных комбинаций категорий
    - Обработку несуществующих категорий
    - Обработку пустого списка категорий
    """
    result = count_transaction_categories(transactions, categories)
    assert result == expected


def test_empty_transactions_count():
    """
    Тест проверяет работу функции с пустым списком транзакций.

    Проверяет:
    - Возвращает ли функция словарь с нулями для всех категорий
    - Не вызывает ли это ошибок
    """
    empty_transactions = []
    categories = ["электроника", "перевод", "интернет"]
    expected = {"электроника": 0, "перевод": 0, "интернет": 0}
    result = count_transaction_categories(empty_transactions, categories)
    assert result == expected


def test_case_insensitive_count():
    """
    Тест проверяет корректную работу функции с разными регистрами текста.

    Проверяет:
    - Игнорирование регистра при поиске категорий
    - Корректность подсчета при разных регистрах
    """
    transactions_case = [
        {"id": 1, "amount": 100, "description": "ОПЛАТА В МАГАЗИНЕ ЭЛЕКТРОНИКА"},
        {"id": 2, "amount": 200, "description": "ПЕРЕВОД ДРУГУ"},
    ]
    categories = ["электроника", "перевод"]
    expected = {"электроника": 1, "перевод": 1}
    result = count_transaction_categories(transactions_case, categories)
    assert result == expected


def test_missing_description_count():
    """
    Тест проверяет обработку транзакций без описания.

    Проверяет:
    - Корректную обработку транзакций без ключа 'description'
    - Не влияет ли отсутствие описания на подсчет других транзакций
    """
    transactions_missing = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200, "description": "Перевод другу"},
    ]
    categories = ["перевод"]
    expected = {"перевод": 1}
    result = count_transaction_categories(transactions_missing, categories)
    assert result == expected


def test_invalid_input_count():
    """
    Тест проверяет обработку некорректных входных данных.

    Проверяет:
    - Вызывает ли функция ошибку при неправильном типе данных
    - Корректно ли обрабатываются недопустимые входные параметры
    """
    with pytest.raises(TypeError):
        count_transaction_categories(123, "электроника")
    with pytest.raises(TypeError):
        count_transaction_categories(transactions, 123)
