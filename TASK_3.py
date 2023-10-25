from ColorLibraryOfLabWork_5 import *

'''
3.1	 Работа с графиками и обработка массивов.
Сформировать массив значений функции f(x) на заданном интервале по формуле y = sin(x/3) + 1.2a, x = 3.567, -5 <= a <= 12 
delta a = 2.5.
Вывести на экран значения аргумента и значения функции. Найти в массиве наибольшее, наименьшее, среднее значение, 
определить количество элементов массива, а также отсортировать 
его (чётные варианты – по убыванию, нечётные – по возрастанию). 
+------------------------------------------------------------------------------------------
Построить график изменения значений функции, вывести на экран его с обозначением осей, 
пределов изменения функции и аргумента.
+------------------------------------------------------------------------------------------
На экран также вывести график прямой, значение которой равно среднему значению функции f(x). 
График прямой и функции оформить различными маркерами.
3.2 Построить графики следующих функций, изменения и диапазон аргумента задать самостоятельно:
'''


def task_3_1():
    print('\n' * 100)
    a_values = np.arange(-5, 13, 2.5)
    x = 3.567
    f_values = np.sin(x / 3) + 1.2 * a_values
    print_3_1(a_values, f_values)
    plt.plot(a_values, f_values, marker='o', label='Искомая функция f(x)')
    plt.xlim(-10, 15)
    plt.ylim(-20, 20)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.axhline(max(f_values), color='red', alpha=0.5, label='Границы значения функции')
    plt.axhline(min(f_values), color='red', alpha=0.5)
    plt.axvline(max(a_values), color='orange', alpha=0.5, label='Границы аргумента функции')
    plt.axvline(min(a_values), color='orange', alpha=0.5)
    plt.xlabel('Изменяемая переменная a')
    plt.ylabel(' Значение функции f(x)')
    plt.title('График функции f(x)')
    plt.grid(True)
    # Построим график среднего значения
    average_line = [np.mean(f_values)] * len(f_values)
    plt.plot(a_values, average_line, linestyle='--', marker='x', label='Среднее значение функции f(x)')
    plt.legend()
    plt.show()


def print_3_1(arges, values):
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\n+-------------------------------------------+\n'
                                               '|  Значение функции при разных аргументах:  |\n'
                                               '+-------------------------------------------+\n'
          )
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '+-------+--------------------+\n'
          '|',
          Style.BRIGHT + Fore.LIGHTGREEN_EX +
          '  a  ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Значение функции:',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|\n'
          '+-------+--------------------+')
    for i in range(len(values)):
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
              Style.BRIGHT + Fore.LIGHTGREEN_EX +
              f'{str(arges[i]).ljust(4)} ',
              Style.BRIGHT + Fore.LIGHTWHITE_EX +
              '|',
              Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
              f' {str(round(values[i], 3)).ljust(16)} ',
              Style.BRIGHT + Fore.LIGHTWHITE_EX +
              '|\n'
              '+-------+--------------------+')
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\n Наибольшее значение функции - '
                                              f'\033[4m{round(max(values), 3)}\033[0m'
                                              '\n-----------------------------------------------------------------\n',
          Style.BRIGHT + Fore.LIGHTGREEN_EX + f'Наименьшее значение функции - \033[4m{round(min(values), 3)}\033[0m'
                                              '\n-----------------------------------------------------------------\n',
          Style.BRIGHT + Fore.LIGHTGREEN_EX + f'Количество элементов массива - \033[4m{len(values)}\033[0m'
                                              '\n-----------------------------------------------------------------\n',
          Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Среднее значение функции - \033[4m'
                                              f'{np.round((np.mean(values)), 3)}\033[0m'
                                              '\n-----------------------------------------------------------------\n',
          Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Отсортированный массив по возрастанию - \033[4m'
                                              f'{np.round(values, 3)}\033[0m'
          )


def task_3_2():
    print('\n' * 100)
    x = np.linspace(-5, 5, 100)  # Значения x от -5 до 5
    y = np.linspace(-5, 5, 100)  # Значения y от -5 до 5
    X, Y = np.meshgrid(x, y)
    # +-------------------------------------------------------
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(231, projection='3d')
    ax1.plot_surface(X, Y, X ** 0.25 + Y ** 0.25, cmap='viridis', color='red')
    ax1.set_title('График 1 (x^0.25 + y^0.25)')
    # +-------------------------------------------------------
    ax2 = fig.add_subplot(232, projection='3d')
    ax2.plot_surface(X, Y, X ** 2 - Y ** 2, cmap='viridis', color='orange')
    ax2.set_title('График 2 (x^2 - y^2)')
    # +-------------------------------------------------------
    ax3 = fig.add_subplot(233, projection='3d')
    ax3.plot_surface(X, Y, 2 * X + 3 * Y, cmap='viridis', color='blue')
    ax3.set_title('График 3 (2*x + 3*y)')
    # +-------------------------------------------------------
    ax4 = fig.add_subplot(234, projection='3d')
    ax4.plot_surface(X, Y, X ** 2 + Y ** 2, cmap='viridis', color='black')
    ax4.set_title('График 4 (x^2 + y^2)')
    # +-------------------------------------------------------
    ax5 = fig.add_subplot(235, projection='3d')
    ax5.plot_surface(X, Y, 2 + 2 * X + 2 * Y - X ** 2 - Y ** 2, cmap='viridis', color='green')
    ax5.set_title('График 5 (2 + 2*x + 2*y - x**2 - y**2)')

    plt.show()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '          ГРАФИКИ ЗАДАНИЯ 3.2 УСПЕШНО ОТОБРАЖЕНЫ          ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def choose_func():
    print(Style.BRIGHT + Fore.BLUE + '+---+----------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '           СПИСОК ПОДФУНКЦИЙ ЗАДАНИЯ 3 В ПРОГРАММЕ :        ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+----------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 1.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + " Задание 3.1 ( работа с графиками и обработка массивов )  ",
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 2.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + " Задание 3.2 ( построить графики в пространстве )         ",
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 3.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Выход из подменю.                                        ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '+---+----------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '  Введите номер подзадачи, которую желаете реализовать :    ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+----------------------------------------------------------+')
    return input()


def task_3():
    print('\n' * 100)
    while True:
        your_choice = choose_func()
        match your_choice:
            case '1':
                task_3_1()
            case '2':
                task_3_2()
                pass
            case '3':
                print('\n' * 100)
                print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
                print(Style.BRIGHT + Fore.BLUE + '|',
                      Style.BRIGHT + Fore.RED + '             Осуществляем выход из подменю...             ',
                      Style.BRIGHT + Fore.BLUE + '|')
                print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
                break
        if your_choice not in '123':
            print('\n' * 100)
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')
            print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
                  'Введённый вами номер задачи отсутствует в перечне функций. Повторите свой ввод.',
                  Style.BRIGHT + Fore.BLUE + '|')
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 3 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')
