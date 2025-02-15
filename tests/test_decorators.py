import pytest

from src.decorators import log


def test_log_success():
    """Тест на проверку успешного выполнения функции"""
    @log(filename=None)
    def my_func(x):
        return x + 1

    if my_func(1) == 2:
        assert "my_func ok"


def test_log_with_out_any_args():
    """Тест на проверку вызова ошибки при отсутствии хотя бы одного аргумента"""
    @log(filename=None)
    def my_func(x, y):
        return x + y

        with pytest.raises(ValueError) as exc_info:
            my_func(1,)
        assert str(exc_info.value) == ("my_func error: my_func() missing 1 required positional argument: "
                                       "'y'. Inputs: (1,), {}")


def test_log_with_out_args():
    """Тест на проверку вызова ошибки при отсутствии аргументов"""
    @log(filename=None)
    def my_func(x, y):
        return x + y

        with pytest.raises(ValueError) as exc_info:
            my_func()
        assert str(exc_info.value) == ("my_func error: my_func() missing 2 required positional arguments: "
                                       "'x' and 'y'. Inputs: (), {}")


def test_log_with_temp_file(tmpdir):
    """Тест на проверку записи об успешном выполнении декорируемой функции во временный файл"""
    # Создаем временный файл
    temp_file = tmpdir.join("temp_file.txt")

    @log(filename=str(temp_file))
    def my_func(x, y):
        return x + y

    # Вызываем функцию
    my_func(1, 2)

    # Проверяем содержимое временного файла
    assert temp_file.read() == "my_func ok\n"


def test_log_with_temp_file_with_out_args(tmpdir):
    """Тест на проверку записи об ошибке об отсутствии аргументов декорируемой функции во временный файл"""
    # Создаем временный файл
    temp_file = tmpdir.join("temp_file.txt")

    @log(filename=str(temp_file))
    def my_func(x, y):
        return x + y

    # Вызываем функцию без необходимых аргументов
    with pytest.raises(TypeError):
        my_func()

    # Проверяем сообщение об ошибке в лог-файле
    error_message = ("my_func error: test_log_with_temp_file_with_out_args.<locals>.my_func() "
                     "missing 2 required positional arguments: 'x' and 'y'. Inputs: (), {}\n")
    assert temp_file.read() == error_message


def test_log_with_temp_file_with_out_any_args(tmpdir):
    """Тест на проверку записи об ошибке об отсутствии хотя
    бы одного аргумента декорируемой функции во временный файл"""
    # Создаем временный файл
    temp_file = tmpdir.join("temp_file.txt")

    @log(filename=str(temp_file))
    def my_func(x, y):
        return x + y

    # Вызываем функцию без необходимых аргументов
    with pytest.raises(TypeError):
        my_func(1,)

    # Проверяем сообщение об ошибке в лог-файле
    error_message = ("my_func error: test_log_with_temp_file_with_out_any_args.<locals>.my_func() "
                     "missing 1 required positional argument: 'y'. Inputs: (1,), {}\n")
    assert temp_file.read() == error_message
