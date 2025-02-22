import pandas as pd
from unittest.mock import patch, mock_open
from src.file_reader import read_csv_transactions, read_excel_transactions


@patch('pandas.read_csv')
def test_read_csv_success(mock_read_csv):
    """
        Тест успешной загрузки CSV-файла.

        Проверяет, что функция `read_csv_transactions` корректно вызывает `pd.read_csv`
        и возвращает ожидаемый DataFrame.
    """
    # Подготовка данных для имитации
    mock_df = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})
    mock_read_csv.return_value = mock_df

    # Выполнение функции
    result = read_csv_transactions('mocked_file_path.csv')

    # Проверка результата
    assert mock_read_csv.called
    pd.testing.assert_frame_equal(result, mock_df)


@patch('pandas.read_csv', side_effect=FileNotFoundError)
def test_read_csv_file_not_found(mock_read_csv):
    """
        Тест обработки ошибки FileNotFoundError при загрузке CSV-файла.

        Проверяет, что функция `read_csv_transactions` корректно обрабатывает исключение
        FileNotFoundError и возвращает None.
    """
    # Выполнение функции
    result = read_csv_transactions('non_existent_file.csv')

    # Проверка результата
    assert mock_read_csv.called
    assert result is None


@patch('pandas.read_excel')
def test_read_excel_success(mock_read_excel):
    """
        Тест успешной загрузки Excel-файла.

        Проверяет, что функция `read_excel_transactions` корректно вызывает `pd.read_excel`
        и возвращает ожидаемый DataFrame.
    """
    # Подготовка данных для имитации
    mock_df = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})
    mock_read_excel.return_value = mock_df

    # Выполнение функции
    result = read_excel_transactions('mocked_file_path.xlsx')

    # Проверка результата
    assert mock_read_excel.called
    pd.testing.assert_frame_equal(result, mock_df)


@patch('pandas.read_excel', side_effect=FileNotFoundError)
def test_read_excel_file_not_found(mock_read_excel):
    """
        Тест обработки ошибки FileNotFoundError при загрузке Excel-файла.

        Проверяет, что функция `read_excel_transactions` корректно обрабатывает исключение
        FileNotFoundError и возвращает None.
    """
    # Выполнение функции
    result = read_excel_transactions('non_existent_file.xlsx')

    # Проверка результата
    assert mock_read_excel.called
    assert result is None
