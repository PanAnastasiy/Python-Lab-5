from ColorLibraryOfLabWork_5 import *

'''
1.	Импортировать датасет.+
2.	Взять 1000 значений из выбранного датасета.+
3.	Проверить данные на пропуски.+
4.	Проверить на нормальность распределения и выбросы.+ 
Использовать для проверки нормальности распределения ящики с усами (логарифмическую шкалу) и гистограммы.+ 
5.	Заполнить пропуски и обработать аномальные значения.+
6.	Определить сколько в выборке 1, 2, 3 …комнатных квартир.+
7.	Построить сводную таблицу: подписи строк – районы, подписи колонок – комнаты, пересечение строк и столбцов –
 количество квартир в этом районе.
8.	Итоговый обработанный массив без выбросов и пропусков сохраните в файл surname.csv+
9.	Вышлите итоговый вый файл на проверку преподавателю.+

'''


def task_2():
    dataset = pd.read_csv('price_prepared.csv', encoding='UTF-8', sep=';')
    all_data = pd.DataFrame(dataset).head(1000)
    check_values(all_data)
    print_graphics(dataset)
    all_data = change_area(all_data)
    to_count_flats(all_data)
    create_pivot_table(all_data)
    all_data.to_csv('PANfilenko.csv', index=False)
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 2 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def check_values(df):
    if df.isnull().values.any():
        print(Style.BRIGHT + Fore.BLUE + '\n\n+--------------------------------------------------+')
        print(Style.BRIGHT + Fore.BLUE + '| ', end='')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Пропуски в данных ',
              Style.BRIGHT + Fore.LIGHTCYAN_EX + '\033[4mПРИСУТСТВУЮТ.\033[0m                 ', end='')
        print(Style.BRIGHT + Fore.BLUE + '|')
        print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------+')
    else:
        print(Style.BRIGHT + Fore.BLUE + '\n\n+--------------------------------------------------+')
        print(Style.BRIGHT + Fore.BLUE + '| ', end='')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Пропуски в данных ',
              Style.BRIGHT + Fore.LIGHTCYAN_EX + '\033[4mОТСУТСТВУЮТ.\033[0m                  ', end='')
        print(Style.BRIGHT + Fore.BLUE + '|')
        print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------+')


def print_graphics(dataset):
    plt.figure(figsize=(15, 8))
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.subplot(2, 3, 1)
    plt.title('Гистограмма Square')
    sns.histplot(dataset['Square'], color='blue')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 2)
    plt.title('Гистограмма LifeSquare')
    sns.histplot(dataset['LifeSquare'], color='orange')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 3)
    plt.title('Гистограмма KitchenSquare')
    sns.histplot(dataset['KitchenSquare'], color='green')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 4)
    plt.title('Гистограмма m_sq')
    sns.histplot(dataset['m_sq'], color='red')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 5)
    plt.title('Гистограмма Price')
    sns.histplot(dataset['Price'], color='purple')
    # +-------------------------------------------------------
    plt.figure(figsize=(15, 8))
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.subplot(2, 3, 1)
    plt.title('Ящик с усами Square')
    sns.boxplot(y=dataset['Square'], color='blue')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 2)
    plt.title('Ящик с усами LifeSquare')
    sns.boxplot(y=dataset['LifeSquare'], color='orange')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 3)
    plt.title('Ящик с усами KitchenSquare')
    sns.boxplot(y=dataset['KitchenSquare'], color='green')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 4)
    plt.title('Ящик с усами m_sq')
    sns.boxplot(y=dataset['m_sq'], color='red')
    # +-------------------------------------------------------
    plt.subplot(2, 3, 5)
    plt.title('Ящик с усами Price')
    sns.boxplot(y=dataset['Price'], color='purple')
    # +-------------------------------------------------------
    plt.show()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          ' Гистограммы и "ящики с усами" построены!                         ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          ' ПРОВЕРКА НА НОРМАЛЬНОСТЬ РАСПРЕДЕЛЕНИЯ И ВЫБРОСЫ ПРОШЛА УСПЕШНО! ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------------------------+')


def change_area(all_data):
    all_data = all_data.map(abs)
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          ' АНОМАЛЬНЫЕ ЗНАЧЕНИЯ БЫЛИ УСПЕШНО ОБРАБОТАНЫ!                     ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------------------------+')
    return all_data


def to_count_flats(all_data):
    all_data['TotalArea'] = round(all_data['Square'] + all_data['LifeSquare'] + all_data['KitchenSquare'] +
                                  all_data['m_sq'], 1)
    count_5 = len(all_data[all_data['TotalArea'] > 5])
    count_3_5 = len(all_data[(all_data['TotalArea'] > 3) & (all_data['TotalArea'] < 5)])
    count_0_3 = len(all_data[all_data['TotalArea'] < 3])
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          f' Количество квартир с суммарной площадью больше 5:  \033[4m{count_5}\033[0m            ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          f' Количество квартир с суммарной площадью от 3 до 5: \033[4m{count_3_5}\033[0m           ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          f' Количество квартир с суммарной площадью до 3: \033[4m{count_0_3}\033[0m                ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------------------------+')


def create_pivot_table(all_data):
    pivot_table = pd.pivot_table(all_data, index=['TotalArea'], values=['Price'], aggfunc='count')
    pivot_table = pivot_table.sort_values(by='Price', ignore_index=False, ascending=False)
    pivot_table['Count'] = pivot_table['Price']
    pivot_table = pivot_table.drop('Price', axis=1)
    pivot_table.to_csv('Pivot_table.csv', index=True, sep=';')
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+--------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          ' СВОДНАЯ ТАБЛИЦА УСПЕШНО ПОСТРОЕНА И СОХРАНЕНА В ФАЙЛ!            ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+--------------------------------------------------------------------+')
