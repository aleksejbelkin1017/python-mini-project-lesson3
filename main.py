import pandas as pd
from src.processing import filter_by_state, sort_by_date
from src.utils import transactions_list
from src.file_reader import read_csv_transactions, read_excel_transactions
from src.user_interaction import user_welcome_and_choice_transactions, user_choice_status_filter
from src.generators import filter_by_currency
from src.transactions_analyzer import search_transactions
from src.widget import mask_account_card, get_date


def main():
    """ Функция отвечает за основную логику проекта
    и связывает функциональности между собой """
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
    elif start == 'XLSX-файл':
        file_reader = read_excel_transactions(f'{files_base[start]}')
        # Пользователь выбирает статус для дальнейшей фильтрации
        status_filter = user_choice_status_filter()
        # Программа формирует список словарей из нужного файла с нужным фильтром
        operation_filtration = file_reader
        filtered_transactions = [t for t in operation_filtration if t['state'] == status_filter]
    else:
        return f"Файла {start} нет в базе."

    # Подготавливаем вопросы пользователю
    question1 = 'Отсортировать операции по дате? Введите: Да / Нет\n'
    question2 = '\nОтсортировать по возрастанию или по убыванию? Введите: по возрастанию / по убыванию\n'
    question3 = '\nВыводить только рублевые транзакции? Введите: Да / Нет\n'
    question4 = '\nОтфильтровать список транзакций по определенному слову в описании? Введите: Да / Нет\n'

    # Подготавливаем списки возможных ответов на вопросы
    may_be_answer_1_3 = ['да', 'нет']
    may_be_answer_2 = ['по возрастанию', 'по убыванию']

    # Подготавливаем матрицы ответов на 1 и 2 вопросы для определения сортировки по дате.
    matrix_answer_1_2_ver_1 = ['да', 'по возрастанию']
    matrix_answer_1_2_ver_2 = ['да', 'по убыванию']

    user_answer_1_2 = []

    # Задаём 1 вопрос и получаем на него ответ
    print(question1)

    while True:

        user_answer_1 = str(input('')).lower()

        try:
            if user_answer_1 not in may_be_answer_1_3:
                raise ValueError('Ответ должен быть "да" или "нет". '
                                 f'Ваш ответ: {user_answer_1}')
            else:
                user_answer_1_2.append(user_answer_1)
                break
        except ValueError:
            print('Ошибка: Введите корректный ответ. '
                  'Ответ должен быть "да" или "нет". '
                  f'Ваш ответ: {user_answer_1}')

    # Проверяем нужно ли задавать 2 вопрос. При необходимости, задаём и получаем на него ответ
    while True:

        if user_answer_1 == 'да':

            print(question2)

            while True:
                user_answer_2 = str(input('')).lower()
                try:
                    if user_answer_2 not in may_be_answer_2:
                        raise ValueError('Ответ должен быть "по возрастанию" или "по убыванию". '
                                         f'Ваш ответ: {user_answer_2}')
                    else:
                        user_answer_1_2.append(user_answer_2)
                        break
                except ValueError:
                    print('Ошибка: Введите корректный ответ. '
                          'Ответ должен быть "по возрастанию" или "по убыванию". '
                          f'Ваш ответ: {user_answer_2}')
            break

        else:
            break

    # Проверяем результаты ответов на 1 и 2 вопросы
    # Сортируем по возрастанию
    if user_answer_1_2 == matrix_answer_1_2_ver_1:
        transactions_by_date = sort_by_date(filtered_transactions, False)
    # Сортируем по убыванию
    elif user_answer_1_2 == matrix_answer_1_2_ver_2:
        transactions_by_date = sort_by_date(filtered_transactions)
    # Не сортируем. Оставляем список полученный на предыдущем шаге
    else:
        transactions_by_date = filtered_transactions

    # Задаём 3 вопрос и получаем на него ответ
    print(question3)

    while True:
        user_answer_3 = str(input('')).lower()
        try:
            if user_answer_3 == 'да':
                transactions_by_currency = list(filter_by_currency(transactions_by_date, 'RUB'))
                break
            elif user_answer_3 == 'нет':
                transactions_by_currency = transactions_by_date
                break
            else:
                raise ValueError(f'Ответ должен быть "Да" или "Нет". Ваш ответ "{user_answer_3}"')
        except ValueError:
            print('Ошибка: Введите корректный ответ. '
                  'Ответ должен быть "Да" или "Нет". '
                  f'Ваш ответ "{user_answer_3}"')

    # Задаём 4 вопрос и получаем на него ответ
    print(question4)

    while True:
        user_answer_4 = input('').strip().lower()
        if user_answer_4 == 'нет':
            transactions_by_word = transactions_by_currency
            break
        elif user_answer_4 == 'да':
            user_answer_word = input('\nВведите слово: ').strip().lower()
            transactions_by_word = search_transactions(transactions_by_currency, user_answer_word)
            # Считаем количество транзакций
            # count_transactions = count_transaction_categories(transactions_by_word, user_answer_word)
            break
        else:
            print('Ошибка: Введите корректный ответ. Ответ должен быть "Да" или "Нет".')

        # Считаем количество транзакций
    count_transactions_by_word = len(transactions_by_word)

    result_text_1 = ('\nРаспечатываю итоговый список транзакций.\n'
                     f'Всего банковских операций в выборке {count_transactions_by_word}\n')
    result_text_2 = ('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.\n')

    # Определяем какое результирующее сообщение выводить
    if count_transactions_by_word == 0:
        print(result_text_2)
    else:
        print(result_text_1)

    # Программа отрабатывает функцию по маскировке номеров счетов и карт
    for transaction in transactions_by_word:

        from_value = transaction.get('from', '')

        if pd.isna(from_value) or not isinstance(from_value, str) or " " not in from_value:
            # print(f"Некорректное значение 'from': {from_value}")
            transaction['from'] = 'Неизвестно'
        else:
            transaction['from'] = mask_account_card(from_value)

        to_value = transaction.get('to', '')

        if pd.isna(to_value):
            # print(f"Некорректное значение 'to': {to_value}")
            transaction['to'] = 'Неизвестно'
        elif isinstance(to_value, str):
            transaction['to'] = mask_account_card(to_value)

    # Программа преобразует формат даты транзакции
    for transaction in transactions_by_word:
        if 'date' in transaction:
            transaction['date'] = get_date(transaction['date'])

    # Подготавливаем входные данные для строки вывода
    for transaction in transactions_by_word:
        date = transaction['date']
        description = transaction['description']
        from_account = transaction.get('from', '')
        to_account = transaction.get('to', '')

        if 'operationAmount' in transaction:
            amount = transaction['operationAmount'].get('amount', 'Неизвестно')
            currency = transaction['operationAmount']['currency'].get('name', 'Неизвестно')
        else:
            amount = transaction.get('amount', 'Неизвестно')
            currency = transaction.get('currency_name', 'Неизвестно')

        # Форматируем строку вывода
        output = f"{date} {description}\n"
        if from_account != 'Неизвестно' and to_account:
            output += f"{from_account} -> {to_account}\n"
        elif from_account != 'Неизвестно':
            output += f"{from_account}\n"
        elif to_account:
            output += f"{to_account}\n"
        output += f"Сумма: {amount} {currency}\n"

        print(output)

    return


if __name__ == '__main__':
    main()
