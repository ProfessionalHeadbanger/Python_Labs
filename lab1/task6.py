import threading
import task2
from task5 import time_decorator


result = []


def start_parallel(left, right):
    result.append(task2.calculate_fac(left, right))


@time_decorator
def divide_parallel(number, thread_number):
    try:
        parts_size = number//thread_number
        threads = []
        for i in range(0, thread_number - 1):
            t1 = threading.Thread(target=start_parallel, args=[i * parts_size + 1, (i + 1) * parts_size])
            t1.start()
            threads.append(t1)
        t1 = threading.Thread(target=start_parallel, args=[(i + 1) * parts_size + 1, number])
        t1.start()
        threads.append(t1)
        for i in threads:
            i.join()
        global_result = 1
        for part in result:
            global_result *= part
        result.clear()
        return global_result
    except ValueError:
        print("Некорректное значение")


def input_parallel():
    is_allright = False
    while not is_allright:
        try:
            number = int(input("Высчитать факториал от числа: "))
            if number < 0:
                raise ValueError
            thread_number = int(input("Количество потоков: "))
            if thread_number <= 1:
                raise ValueError
            if thread_number > number:
                raise ValueError
            global_result, execution_time = divide_parallel(number, thread_number)
            print(global_result)
            print(f"Время выполнения: {execution_time} секунд")
            is_allright = True
        except ValueError:
            print("Некорректное значение")
