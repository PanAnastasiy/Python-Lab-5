from ColorLibraryOfLabWork_5 import *
from numpy import *

'''
Найти оценки уравнения регрессии, используя метод наименьших квадратов и матричную форму записи уравнений:
    A=(X^T⋅X)^(-1)⋅(X^T⋅Y)
    Матрица Х имеет 12 строк и 3 столбца. Первый столбец заполнен 1, второй произвольными целыми числами от (N варианта)
     до (N варианта+12), третий – произвольными целыми числами от 60 до 82. 
    Y – вектор-столбец из 12 значений, заполнен произвольными дробными числами от 13,5 до 18,6.
    Найти вектор оценок А (должен получиться вектор-столбец из 3 значений). Проверить вектор А по следующей формуле:
y = a0 +a1*x1+a2*x2
    Полученные значения Y должны быть приблизительно равны значения Y из исходных данных
'''


def task_1():
    print('\n' * 100)
    task_1_1()
    task_1_2()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 1 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def task_1_1():
    a, b = 1.21, 0.371
    y = power(tan(a + b), 2) - cbrt(a+1.5) + a*power(b, 5) - b/log(power(a, 2))
    print_1_1(y)


def task_1_2():
    first_column = np.ones(12)
    second_column = np.random.randint(18, 30, (12, 1))
    third_column = np.random.randint(60, 82, (12, 1))
    X = np.column_stack((first_column, second_column, third_column))
    Y = np.round(random.uniform(13.5, 18.6, (12, 1)), 1)
    A = np.round(linalg.inv(X.T @ X) @ (X.T @ Y), 3)
    new_Y = np.round(A[0] + A[1] * second_column + A[2] * third_column, 1)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nМатрица X имеет следующий вид :\n')
    print_matrix(X, 12, 3)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nВектор-оценок A имеет следующий вид :\n')
    print_matrix(A, 3, 1)
    compare_matrix(Y, new_Y, 12, 1)


def compare_matrix(arr_1, arr_2, rows, columns):
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nЗаданный вектор-столбец Y и предсказанные значения вектора-столбца Y '
                                              'имеют следующий вид :\n')
    for t in range(rows):
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '(  ', end='')
        for k in range(columns):
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + str(arr_1[t][k]).ljust(5), end='')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ') ', end='')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' (  ', end='')
        for k in range(columns):
            print(Style.BRIGHT + Fore.LIGHTRED_EX + str(arr_2[t][k]).ljust(5), end='')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ')\n', end='')
    print_color_of_columns()


def print_color_of_columns():
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '\n  Синий',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + ' - цвет',
          Style.BRIGHT + Fore.LIGHTBLUE_EX + ' заданного',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + 'вектора-столбца Y.')
    print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\n\U0001f353Красный',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + ' - цвет',
          Style.BRIGHT + Fore.LIGHTRED_EX + ' предсказанного',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + 'вектора-столбца Y.')


def print_matrix(arr, rows, columns):
    for t in range(rows):
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '(  ', end='')
        for k in range(columns):
            print(str(arr[t][k]).ljust(7), end='')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ')\n', end='')


def print_1_1(value):
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------'
                                     '-------------------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' УСЛОВИЕ ЗАДАНИЯ 1.1:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          "Искомая функция имеет вид : y = (tan(a + b) ** 2) - (a + 1.5) ** (1/3) + a * (b ** 5) - b / log(a ** 2)")
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------'
                                     '-------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '+----------------------------------------------------------------------------'
                                     '---------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' ОТВЕТ ЗАДАНИЯ 1.1:',
          Style.BRIGHT + Fore.RED + 'Значение функции при заданных аргументах ',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + '\033[4ma = 1.21 b = 0.371\033[0m',
          Style.BRIGHT + Fore.RED + ' равно :',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + f' \033[4m{round(value, 3)}\033[0m ')
    print(Style.BRIGHT + Fore.BLUE + '+----------------------------------------------------------------------------'
                                     '---------------------------------------+')
