from typing import Optional

import pandas as pd


def read_csv_transactions(file_path: str) -> Optional[list[dict]]:
    """ Функция считывает финансовые операции из csv-файла """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict('records')
    except FileNotFoundError:
        print(f'Файл по пути "{file_path}" не найден')
        return None


def read_excel_transactions(file_path: str) -> Optional[list[dict]]:
    """ Функция считывает финансовые операции из excel-файла """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except FileNotFoundError:
        print(f'Файл по пути "{file_path}" не найден')
        return None


# if __name__ == '__main__':
#     print(read_csv_transactions('data/transactions.csv'))
#     print(read_excel_transactions('data/transactions_excel.xlsx'))
