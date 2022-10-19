#Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах
def input_date():
    name = input('Введите фамилию: ')
    surname = input('Введите имя: ')
    phone_number = ''

    valid = False
    while not valid:
            try:
                phone_number = input('Введите номер телефона: ')
                if len(phone_number) != 11:
                    print('В номере телефона должно быть 11 цифр.')
                else:
                    phone_number = int(phone_number)
                    valid = True
            except:
                print('Номер телефона должен состоять только из цифр.')
    description = input('Введите описание: ')
    return name, surname, phone_number, description
