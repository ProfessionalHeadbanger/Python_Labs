def calculate_avg(number_array):
    sum_elems = 0
    count = 0
    for i in number_array:
        sum_elems += i
        count += 1
    return sum_elems/count


def array_input():
    number_array = []
    try:
        size = int(input("Введите количество чисел в массиве: "))
        if size < 0:
            raise ValueError
        else:
            print("Введите массив чисел: ")
            for i in range(size):
                number_array.append(float(input()))
            print("Среднее массива:", calculate_avg(number_array))
    except ValueError:
        print("Некорректное значение")
