import random
import time
import threading
from threading import Thread

result6 = 1


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


def task2(left, right):
    if right == left:
        return right
    else:
        return right * task2(left, right - 1)


def task3(mas):
    summ = 0
    number = 0
    for i in mas:
        summ += i
        number += 1
    print("Среднее массива:", summ / number)


def task4(a, b):
    return a + b


def task5(function):
    start_time = time.time()
    num = int(input("Вычислить факториал от числа: "))
    result = function(num)
    end_time = time.time()
    print("Факториал от числа", num, "был посчитан за", end_time - start_time, "секунд и равен", result)


def task6_start(left, right):
    global result6
    result6 *= task2(left, right)


def task6():
    num = int(input("Вычислить факториал от числа: "))
    t1 = threading.Thread(target=task6_start, args=[num // 2 + 1, num])
    t2 = threading.Thread(target=task6_start, args=[1, num // 2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(result6)


restart = True
while (restart):
    menu = int(input("Выберите, что вы хотите запустить: \n1) \"Угадай число\" \n2) Посчитать факториал "
                     "\n3) Посчитать среднее значение в массиве \n4) Сложить два числа "
                     "\n5) Посчитать время выполнения функции \n6) Посчитать факториал (параллельно) \n7) Выход\n"))
    if menu == 1:
        task1()
    elif menu == 2:
        num = int(input("Вычислить факториал от числа: "))
        print(task2(1, num))
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
        task5(task2)
    elif menu == 6:
        task6()
    elif menu == 7:
        restart = False
    else:
        print("Неправильный ввод")
