def user_welcome_and_choice_transactions():
    """ Функция приветствует пользователя на входе в программу
    и предлагает выбрать источник информации о транзакциях.
    После выбора программа сообщает, что выбрал пользователь """
    files_type = {
        1: 'JSON-файл',
        2: 'CSV-файл',
        3: 'XLSX-файл'
    }

    # Создаем строку приветствия с использованием словаря
    welcome_text = (
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
    )

    # Добавляем пункты меню из словаря
    for key, value in files_type.items():
        welcome_text += f"{key}. Получить информацию о транзакциях из {value}а\n"

    print(welcome_text)

    # Создаем бесконечный цикл
    while True:
        try:
            # Получаем ввод пользователя
            user_choice = int(input(""))

            # Проверяем, есть ли выбор пользователя в словаре
            if user_choice not in files_type:
                first_key = min(files_type.keys())
                last_key = max(files_type.keys())
                message = ("\nВведите корректный номер пункта. "
                           f"Пункта {user_choice} нет в меню. "
                           f"Выберите пункт от {first_key} до {last_key}.")
                print(message)
            else:
                message_true = (f"\nДля обработки выбран {files_type[user_choice]}\n")
                print(message_true)
                break  # Выходим из цикла, если выбор корректный

        except ValueError:
            print("Ошибка: Введите корректный номер пункта. Номер пункта должен состоять из цифр.")

    return files_type[user_choice]


def user_choice_status_filter():
    """ Функция предлагает пользователю ввести статус
    по которому должна будет выполниться фильтрация транзакций """
    status_list = ['EXECUTED', 'CANCELED', 'PENDING']

    # Форматируем список статусов для вывода
    formatted_status_list = ', '.join(status_list)

    status_selection_suggestion = (
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        f"Доступные для фильтровки статусы: {formatted_status_list}\n"
    )

    print(status_selection_suggestion)

    while True:
        try:
            # Получаем ввод пользователя
            user_input = input().upper()

            # Проверяем, есть ли введенный статус в списке
            if user_input not in status_list:
                message = (f'Статус "{user_input}" недоступен. '
                           'Введите статус, по которому необходимо выполнить фильтрацию.'
                           f'Доступные для фильтровки статусы: {formatted_status_list}.')
                print(message)
            else:
                message_true = (f"\nВыбран статус: {user_input}\n")
                print(message_true)
                break
        except ValueError:
            print(f'Ошибка: Выберите один из предложенных статусов {formatted_status_list}.')

    return user_input

if __name__ == '__main__':
    print(user_welcome_and_choice_transactions())
    print(user_choice_status_filter())