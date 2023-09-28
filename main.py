# TODO здесь писать код

from typing import Callable, Any
import functools
from datetime import datetime


def logging_decorator(func: Callable) -> Callable:
    """
    Декоратор, который отвечает за логирование функций.

    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print('Имя функции: {}'.format(func.__name__))
            print('Документация функции {}:\n{}'.format(func.__name__, func.__doc__))
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            error_info = '{} - {}:\t{}\n'.format(datetime.today().strftime("%d.%m.%Y  %H:%M:%S"), func.__name__, error)
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(error_info)

    return wrapped_func


@logging_decorator
def zero_division() -> float:
    """
    Функция для вызова ошибки ZeroDivisionError.
    """
    return 1 / 0


@logging_decorator
def varname() -> Any:
    """
    Функция для вызова ошибки NameError.
    """
    return name


@logging_decorator
def normal() -> str:
    """
    Функция, не вызывающая ошибок.
    """
    return 'Hello, world!'


zero_division()
varname()
normal()






