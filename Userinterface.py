
from Root_file import writing_scv, read_date, find_date,  del_date

def option():
    flag = True
    while flag:
        print("\nВас приветствует информационная система для работы с сотрудниками компании!   \n Выберите пункт меню для продолжения")
        while True:
            print("1: Ввoд нового сотрудника")
            print("2: Поиск сотрудника по фамилии")
            print("3: Удаление уволеного сотрудника")
            print("4: Показать все контакты")
            print("5: Выход")
            ch = int(input())
            if ch not in [1,2,3,4,5]:
                print('\nВыбран неверный пункт меню, попробуйте еще раз: ')
                continue
            if ch == 1:
                writing_scv()
                break
            elif ch == 2:
                find_date()
                break
            elif ch == 3:
                del_date()
                break
            elif ch == 5:
                read_date()
            else:
                flag = False
                break
option()