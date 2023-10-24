def calculate_avg(number_array):
    sum_elems = 0
    count = 0
    for i in number_array:
        sum_elems += i
        count += 1
    return sum_elems/count


def array_input():
    number_array = []
    is_allright = False
    while not is_allright:
        try:
            size = int(input("Введите количество чисел в массиве: "))
            if size <= 0:
                raise ValueError
            else:
                print("Введите массив чисел: ")
                for i in range(size):
                    is_correct = False
                    while not is_correct:
                        try:
                            number = float(input())
                            number_array.append(number)
                            is_correct = True
                        except ValueError:
                            print("Некорректное значение элемента массива")
                print("Среднее массива:", calculate_avg(number_array))
                is_allright = True
        except ValueError:
            print("Некорректное значение")
