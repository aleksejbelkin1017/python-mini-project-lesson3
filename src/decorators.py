# Декоратор log
def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = (f"{func.__name__} ok")
                if filename:
                    with open(filename, 'a', encoding="utf-8") as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = (f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                if filename:
                    with open(filename, 'a', encoding="utf-8") as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                raise e
        return wrapper
    return decorator

# Пример использования декоратора
# @log(filename=None)
# def my_function(x, y):
#     return x + y
#
# my_function()

# @log(filename="log.txt")
# def my_func(x, y):
#     return x + y
#
# my_func(1,)