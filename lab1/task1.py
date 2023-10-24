import random


def input_borders():
    left_border = 0
    right_border = 0
    is_allright = False
    while not is_allright:
        try:
            left_border = int(input("Левая: "))
            right_border = int(input("Правая: "))
            if left_border > right_border:
                print("Левая граница оказалась больше правой, поменяем их местами")
                left_border, right_border = right_border, left_border
            if left_border == right_border:
                print("Границы оказались равны, придется вводить еще раз")
            else:
                is_allright = True
        except ValueError:
            print("Некорректное значение")
    return left_border, right_border


def game(left_border, right_border):
    number = random.randint(left_border, right_border)
    takes = 1
    guess = None
    while guess != number:
        try:
            guess = int(input())
            if guess < left_border or guess > right_border:
                print("Границы какие были, помнишь? Попытка все равно засчитана")
            elif number > guess:
                print("Не угадал, загаданное число больше")
            elif number < guess:
                print("Не угадал, загаданное число меньше")
            takes += 1
        except ValueError:
            print("Некорректное значение")
            takes -= 1
    return number, takes


def game_output():
    print("Это игра, где тебе нужно отгадать число в заданных границах")
    print("Для начала зададим границы")
    left_border, right_border = input_borders()
    print("А теперь попробуй угадать число от", left_border, "до", right_border)
    number, takes = game(left_border, right_border) #исправить возврат переменных
    print("Угадал, загаданное число было", number, "\nЧисло попыток:", takes)
