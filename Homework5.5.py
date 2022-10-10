# Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#Добавьте игру против бота
#Подумайте как наделить бота "интеллектом"
from random import randint

def Enter_date(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def printer(name, k, counter, value):
    print(f"Ход {name}, взято {k}, теперь у {name} {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = 2021
flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = Enter_date(player1)
        counter1 += k
        value -= k
        flag = False
        printer(player1, k, counter1, value)
    else:
        k = Enter_date(player2)
        counter2 += k
        value -= k
        flag = True
        printer(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")