from DescriptionOfLabWork_5 import *
from TASK_1 import *
from TASK_2 import *
from TASK_3 import *


def main():
    message()
    name_of_work()
    while True:
        your_choice = menu()
        match your_choice:
            case '1':
                task_1()
            case '2':
                task_2()
            case '3':
                task_3()
            case '4':
                print('\n' * 100)
                print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
                print(Style.BRIGHT + Fore.BLUE + '|',
                      Style.BRIGHT + Fore.RED + '             Осуществляем выход из программы...           ',
                      Style.BRIGHT + Fore.BLUE + '|')
                print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
                exit(0)
            case '5':
                print('\n' * 100)
                info_of_developer()
        if your_choice not in '12345':
            print('\n' * 100)
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')
            print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
                  'Введённый вами номер задачи отсутствует в перечне функций. Повторите свой ввод.',
                  Style.BRIGHT + Fore.BLUE + '|')
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')


main()
