def writing_scv():
    surname = input('Введите фамилию: ')
    if not surname.isalpha():
        print("Ошибка! Фамилию вводить буквами")
        return
    name = input('Введите имя: ')
    if not name.isalpha():
        print("Ошибка! Фамилию вводить буквами")
        return
    age = input('Введите возраст в формате (dd/mm/yyyy): ')
    description = input('Введите описание: ')
    file = 'Namebook.csv'
    with open(file, 'a', encoding='utf-8') as my_f:
        my_f.write(f"{surname}         {name}         {age}     {description}\n")

def read_date():
    file = 'Namebook.csv'
    with open(file, 'r', encoding='utf-8') as my_f:
        print(my_f.read())



def find_date():
    sn = input("Ввeдите фамилию сотрудника, которого нужно найти :  ")
    file = 'Namebook.csv'
    with open(file, 'r', encoding='utf-8') as my_f:
        for line in my_f.readlines():
            if line.startswith(sn):
                print(line)

def del_date():
    sn = input("Ввeдите фамилию сотрудника, которого нужно удалить :  ")
    file = 'Namebook.csv'
    with open(file, 'r+', encoding='utf-8') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if sn not in line:
                f.write(line)
        f.truncate()
