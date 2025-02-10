import time

# Декоратор log
def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = (f"{func.__name__} ok: \n"
                               f"Время начала выполнения в {start_time} \n"
                               f"Время окончания выполнения {end_time} \n"
                               f"Время выполнения функции: {end_time - start_time:.8f}\n"
                               f"Результат: {result} \n")
                if filename:
                    with open(filename, 'a', encoding="utf-8") as f:
                        f.write(log_message + '\n\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                end_time = time.time()
                log_message = (f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                if filename:
                    with open(filename, 'a', encoding="utf-8") as f:
                        f.write(log_message + '\n\n')
                else:
                    print(log_message)
                raise e
        return wrapper
    return decorator

# Пример использования декоратора
@log(filename=None)
def my_function(x, y):
    return x + y

my_function(21,4)