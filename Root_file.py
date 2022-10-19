#Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах
from User_date import input_date
name, surname, phone_number, description = input_date()
def writing_scv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as my_f:
        my_f.write(f"{name}         {surname}         {phone_number}  {description}\n")

def writing_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as my_f:
        my_f.write(f"{name}         {surname}         {phone_number}  {description}\n")
