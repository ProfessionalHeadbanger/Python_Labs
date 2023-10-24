import task1
import task2
import task3
import task4
import task6


restart = True
while restart:
    try:
        menu = int(input("Выберите, что вы хотите запустить: \n1) \"Угадай число\" \n2) Посчитать факториал "
                     "\n3) Посчитать среднее значение в массиве \n4) Сложить два числа "
                     "\n5) Посчитать факториал (параллельно) \n6) Выход\n"))
        if menu == 1:
            task1.game_output()
        elif menu == 2:
            task2.factorial_main()
        elif menu == 3:
            task3.array_input()
        elif menu == 4:
            task4.add_input()
        elif menu == 5:
            task6.input_parallel()
        elif menu == 6:
            restart = False
        else:
            raise ValueError
    except ValueError:
        print("Invalid value")
