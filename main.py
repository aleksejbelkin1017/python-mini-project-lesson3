import pandas as pd
from src.processing import filter_by_state
from src.utils import transactions_list
from src.file_reader import read_csv_transactions, read_excel_transactions, split_transaction
from src.user_interaction import user_welcome_and_choice_transactions, user_choice_status_filter


def main():
    files_base = {
        'JSON-файл' : 'data/operations.json',
        'CSV-файл' : 'data/transactions.csv',
        'XLSX-файл' : 'data/transactions_excel.xlsx'
    }
    # Пользователь выбирает тип файла с исходными данными
    start = user_welcome_and_choice_transactions()
    # Определяем путь к файлу с исходными данными
    if start == 'JSON-файл':
        file_reader = transactions_list(f'{files_base[start]}')
        # Пользователь выбирает статус для дальнейшей фильтрации
        status_filter = user_choice_status_filter()
        # Программа формирует список словарей из нужного файла с нужным фильтром
        filtered_transactions = filter_by_state(file_reader, status_filter)
        result = filtered_transactions
    elif start == 'CSV-файл':
        file_reader = read_csv_transactions(f'{files_base[start]}')
        # Пользователь выбирает статус для дальнейшей фильтрации
        status_filter = user_choice_status_filter()
        # Извлечение заголовков
        headers = 'id;state;date;amount;currency_name;currency_code;from;to;description'.split(';')
        # Преобразование данных
        transactions = []
        for entry in file_reader:
            # Разделяем строку на части
            values = entry['id;state;date;amount;currency_name;currency_code;from;to;description'].split(';')
            # Создаем словарь, сопоставляя заголовки и значения
            transaction = dict(zip(headers, values))
            transactions.append(transaction)
        # Фильтруем список словарей по ключу 'state'
        filtered_transactions = [t for t in transactions if t['state'] == status_filter]
        result = filtered_transactions
    elif start == 'XLSX-файл':
        file_reader = read_excel_transactions(f'{files_base[start]}')
        # Пользователь выбирает статус для дальнейшей фильтрации
        status_filter = user_choice_status_filter()
        # Программа формирует список словарей из нужного файла с нужным фильтром
        operation_filtration = file_reader
        filtered_transactions = [t for t in operation_filtration if t['state'] == status_filter]
        result = filtered_transactions
    else:
        return f"Файла {start} нет в базе."

    return result


if __name__ == '__main__':
    print(main())
