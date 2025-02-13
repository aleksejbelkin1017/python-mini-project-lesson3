import json

def transactions_list(json_file):
    """ Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой или содержит не список, возвращает пустой список. """
    try:
        with open(json_file, encoding='utf-8') as file_in:
            data = json.load(file_in)

        # Проверяем, что данные представляют собой список
        if isinstance(data, list):
            return data
        else:
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# if __name__ == '__main__':
#     print(transactions_list('data/operations.json'))
