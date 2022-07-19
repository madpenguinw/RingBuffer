from datetime import datetime
import random


def given_func(value):
    """
    Исходная ф-ия определения четности целого числа.
    """
    return value % 2 == 0


def new_func(value):
    """
    Новая ф-ия определения четности целого числа.
    Проверяет, равен ли 1 последний бит в двоичной записи заданного числа.
    """
    if value & 1:
        return False
    else:
        return True


def time_test(func):
    """
    Измерение времени выполнения функций.
    """
    start_time = datetime.now()
    i = 0
    while i in range(10 ** 6):
        func(i)
        i += 1
    return datetime.now() - start_time


def functional_test(func_1, func_2):
    """
    Проверка равенства результатов выполнения функций.
    """
    var = random.randint(0, 100)
    assert func_1(var) == func_2(var), 'Функции выдают разный результат!'
    return True


if __name__ == '__main__':
    print('Время выполнения исходной функции =', time_test(given_func))
    print('Время выполнения новой функции =', time_test(new_func))
    functional_test(given_func, new_func)
    print('Обе функции выдают одинаковый результат.')
