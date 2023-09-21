import random
import time
import threading


def task1():
    print("Угадай число от 1 до 10")
    number = random.randint(1, 10)
    guess = int(input())
    take = 1
    while guess != number:
        if number > guess:
            print("Не угадал, загаданное число больше")
        elif number < guess:
            print("Не угадал, загаданное число меньше")
        take += 1
        guess = int(input())
    print("Хорош, ты угадал, загаданное число было", number, "\nЧисло попыток:", take)


def task2(n):
    if n == 1:
        return n
    else:
        return n*task2(n-1)


def task3(mas):
    summ = 0
    number = 0
    for i in mas:
        summ += i
        number += 1
    print("Среднее массива:", summ/number)


def task4(a, b):
    return a + b


def task5(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res

    return wrapped


@task5
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


def task6():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2, args=[int(input("S"))])
    t1.start()
    t2.start()
    t1.join()
    t2.join()


restart = True
while (restart):
    menu = int(input("Выберите, что вы хотите запустить: \n1) \"Угадай число\" \n2) Посчитать факториал "
                     "\n3) Посчитать среднее значение в массиве \n4) Сложить два числа "
                     "\n5) Посчитать время выполнения функции \n6) Посчитать факториал (параллельно) \n7) Выход\n"))
    if menu == 1:
        task1()
    elif menu == 2:
        num = int(input("Вычислить факториал от числа: "))
        task2(num)
    elif menu == 3:
        mas = []
        count = int(input("Введите количество чисел в массиве: "))
        print("Введите массив целых чисел: ")
        for i in range(count):
            mas.append(int(input()))
        task3(mas)
    elif menu == 4:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        print("Сумма:", task4(a, b))
    elif menu == 5:
        print(task5(func("111", "0000")))
    elif menu == 6:
        task6()
    elif menu == 7:
        restart = False
    else:
        print("Неправильный ввод")