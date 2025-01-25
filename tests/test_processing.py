import pytest
from src.processing import filter_by_state, sort_by_date


# Модуль processing
# filter_by_state:
def test_filter_by_state_right_filtration(list_of_dictionaries_for_checking_the_state_1,
                                          list_of_dictionaries_for_checking_the_state_2,
                                          list_of_dictionaries_for_checking_the_state_3,
                                          list_of_dictionaries_for_checking_the_state_4):
    """Тест проверяет фильтрацию словарей с указанным статусом state в списке"""
    # статус state имеет значение по умолчанию "EXECUTED"
    result_1 = filter_by_state(list_of_dictionaries_for_checking_the_state_1)
    assert result_1 == list_of_dictionaries_for_checking_the_state_2
    # статус state имеет значение "CANCELED"
    result_2 = filter_by_state(list_of_dictionaries_for_checking_the_state_3)
    assert result_2 == list_of_dictionaries_for_checking_the_state_4


def test_filter_by_state_not_state(list_of_dictionaries_for_checking_the_state_4):
    """Тест проверяет работу функции при вводе значения state, которое отсутствует в списке словарей"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(list_of_dictionaries_for_checking_the_state_4, "WAITING")
    assert str(exc_info.value) == "Указанное значение статуса state отсутствует в списке словарей"


def test_filter_by_state_clear_dictionary():
    """Тест проверяет работу функции при вводе пустого списка словарей"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([])
    assert str(exc_info.value) == "Исходные данные не введены"


# sort_by_date:
def test_sort_by_date_sorted_up(list_of_dictionaries_for_checking_the_state_1,
                                list_of_dictionaries_result_filter_up):
    """Тест проверяет сортировку по возрастанию"""
    result = sort_by_date(list_of_dictionaries_for_checking_the_state_1, False)
    assert result == list_of_dictionaries_result_filter_up


def test_sort_by_date_sorted_down(list_of_dictionaries_for_checking_the_state_1,
                                  list_of_dictionaries_result_filter_down):
    """Тест проверяет сортировку по убыванию"""
    result = sort_by_date(list_of_dictionaries_for_checking_the_state_1)
    assert result == list_of_dictionaries_result_filter_down
