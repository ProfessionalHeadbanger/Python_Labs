from task5 import time_decorator


def calculate_fac(left, right):
    if right == left:
        return right
    else:
        return right*calculate_fac(left, right - 1)


@time_decorator
def calculate_fac_time(left, right):
    return calculate_fac(left, right)


def factorial_main():
    try:
        number = int(input("Высчитать факториал от числа: "))
        if number < 0:
            raise ValueError
        else:
            print(calculate_fac_time(1, number))
    except ValueError:
        print("Некорректное значение")
