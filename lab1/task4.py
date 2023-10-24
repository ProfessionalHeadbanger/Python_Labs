def calculate_add(a):
    def calculate_add_a(b):
        return a+b
    return calculate_add_a


def add_input():
    is_allright = False
    while not is_allright:
        try:
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
            print(f'add({a})({b}) = {calculate_add(a)(b)}')
            is_allright = True
        except ValueError:
            print("Некорректное значение")
