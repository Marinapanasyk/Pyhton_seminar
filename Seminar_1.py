#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
number=int(input("Введите день недели:"))
if (number == 6) or (number == 7):
    print("Сегодня выходной")
elif (number > 7):
    print("Ошибка, цифра должна быть меньше 7")
else:
    print("Сегодня будний день")
