import pandas as pd


def read_csv_transactions(file_path):
    """ Функция считывает финансовые операции из csv-файла """
    df = pd.read_csv(file_path)
    return df


def read_excel_transactions(file_path):
    """ Функция считывает финансовые операции из csv-файла """
    df = pd.read_excel(file_path)
    return df


if __name__ == '__main__':
    # print(read_csv_transactions('data/transactions.csv'))
    # print(read_excel_transactions('data/transactions_excel.xlsx'))