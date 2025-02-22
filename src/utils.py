import json
import logging

logger = logging.getLogger('utils.py')
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:\n%(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def transactions_list(json_file):
    """ Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой или содержит не список, возвращает пустой список. """
    logger.info('Запущена функция transactions_list')
    try:
        with open(json_file, encoding='utf-8') as file_in:
            data = json.load(file_in)
        logger.info('Загружены данные из JSON-файла')
        # Проверяем, что данные представляют собой список
        if isinstance(data, list):
            logger.info('Данные представляют собой список')
            logger.info('Выполнение функции transactions_list успешно завершено')
            return data
        else:
            logger.info('Данные представляют собой не список')
            return []
    except FileNotFoundError:
        logger.error('Файл не найден')
        logger.debug('Укажите корректный путь к файлу')
        return []
    except json.JSONDecodeError:
        logger.error('Файл неправильного формата')
        logger.debug('Укажите файл правильного формата')
        return []

# if __name__ == '__main__':
#     print(transactions_list('data/operations.json'))
