from datetime import datetime


MIN_MERGE = 32


def calc_min_run(n):
    """
    Расчет мининмального пробега.
    """
    r = 0  # Становится 1, если какой-либо бит сдвинут.
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(array, left, right):
    """
    Сортировка массива вставками. Сортирует пробеги.
    """
    for i in range(left + 1, right + 1):
        j = i
        while j > left and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


def merge(array, l, m, r):
    """
    Сортировка слиянием. Объединяет отсортированные пробеги.
    """
    # Исходный список разбит на две части.
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(array[l + i])
    for i in range(0, len2):
        right.append(array[m + 1 + i])

    i, j, k = 0, 0, l

    # После сравнения происходит слияние двух списков в один.
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    # Копирование элементов левого списка, если они остались.
    while i < len1:
        array[k] = left[i]
        k += 1
        i += 1

    # Копирование элементов правого списка, если они остались.
    while j < len2:
        array[k] = right[j]
        k += 1
        j += 1


def tim_sort(array):
    """
    Сортировка Timsort. Объединяет в себе сортировки вставками и слиянием.
    """
    n = len(array)
    min_run = calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(array, start, end)

    size = min_run
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(array, left, mid, right)

        size = 2 * size


def sort(array):
    """
    Сортировка встроенным методом sort().
    """
    array.sort()


def time_test(func):
    """
    Измерение времени выполнения функций
    """
    start_time = datetime.now()
    array = [85, 31, 44, -27, 31, -31, -27, 0, 3, 100]
    i = 0
    while i in range(10 ** 6):
        func(array)
        array = [85, 31, 44, -27, 31, -31, -27, 0, 3, 100]
        i += 1
    return datetime.now() - start_time


def functional_test(func_1, func_2):
    """
    Проверка равенства результатов выполнения функций.
    """
    array = [85, 31, 44, -27, 31, -31, -27, 0, 3, 100]
    assert func_1(array) == func_2(array), 'Функции выдают разный результат!'
    return True


def main(func, array):
    print('Исходный список:', array)
    func(array)
    print('Отсортированный список:', array)


if __name__ == "__main__":
    array = [85, 31, 44, -27, 31, -31, -27, 0, 3, 100]
    main(tim_sort, array)
    print('Теперь используем встроенную сортировку sort().')
    array = [85, 31, 44, -27, 31, -31, -27, 0, 3, 100]
    main(sort, array)
    functional_test(tim_sort, sort)
    print('Обе функции выдают одинаковый результат.')
    print('Timsort  работает за', time_test(tim_sort))
    print('Sort  работает за', time_test(sort))
