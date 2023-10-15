import threading
import task2


result = []


def start_parallel(left, right):
    result.append(task2.calculate_fac_time(left, right))


def divide_parallel():
    try:
        number = int(input("Высчитать факториал от числа: "))
        if number < 0:
            raise ValueError
        thread_number = int(input("Количество потоков: "))
        if thread_number < 0:
            raise ValueError
        if thread_number > number:
            raise ValueError
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
        print(global_result)
    except ValueError:
        print("Некорректное значение")