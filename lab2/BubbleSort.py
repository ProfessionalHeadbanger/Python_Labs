import random
from ProfileDecorator import ProfileDecorator


@ProfileDecorator
def bubble_sort(array):
    size = len(array)

    if size <= 1:
        return array

    for index in range(size - 1):
        if array[index] > array[index + 1]:
            array[index], array[index + 1] = array[index + 1], array[index]

    return bubble_sort(array[:-1]) + [array[-1]]


def bubble_sort_call() -> None:
    array = []

    for count in range(0, 100):
        array.append(random.randint(0, 1000))
    print("Изначальный массив:")
    print(*array, sep=", ")

    sorted_array = bubble_sort(array)

    print("Отсортированный массив:")
    print(*sorted_array, sep=", ")
    print("\n")
    calls, total_time = bubble_sort.get_stats()

    print(f"Количество вызовов: {calls}\n" + f"Время выполнения: {total_time}\n")
    bubble_sort.clear_stats()
