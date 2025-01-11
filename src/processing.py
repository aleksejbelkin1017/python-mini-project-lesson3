from typing import Dict, List


def filter_by_state(dict_with_state: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    return [item for item in dict_with_state if item["state"] == state]


def sort_by_date(list_dict: List[Dict], arg_for_sort: bool = True) -> List[Dict]:
    """Принимает список словарей и параметр сортировки(по умолчанию "True" — 'CANCELED').
    Функция возвращает новый список, отсортированный по дате(date)"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict["date"], reverse=arg_for_sort)
    return sort_list


# Пример использования функций
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
# Вывод со статусом по умолчанию 'EXECUTED'
print(filter_by_state(data))
# Вывод со статусом 'CANCELED'
print(filter_by_state(data, "CANCELED"))
# Вывод со сортировкой по убыванию (сначала самые последние операции)
print(sort_by_date(data))
# Вывод со сортировкой по возрастанию (сначала первые операции)
print(sort_by_date(data, False))
