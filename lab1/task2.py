def calculate_fac(left, right):
    try:
        if right == 0:
            return 1
        elif right == left:
            return right
        else:
            return right*calculate_fac(left, right - 1)
    except ValueError:
        print("Некорректное значение")


def factorial_main():
    is_allright = False
    while not is_allright:
        try:
            number = int(input("Высчитать факториал от числа: "))
            if number < 0:
                raise ValueError
            else:
                print(calculate_fac(1, number))
                is_allright = True
        except ValueError:
            print("Некорректное значение")
