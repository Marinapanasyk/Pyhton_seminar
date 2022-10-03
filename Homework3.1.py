#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
from random import randint, choice

def Summelement(SL):
        s = 0
        for i in range(len(SL)):
            if i % 2 != 0:
                s += SL[i]
        print(f"Сумма равна: {s}")
SL=[]
n =int(input("Введите количество элементов в списке:"))
for i in range (n):
    SL.append(randint(-10, 10))
print(SL)
Summelement(SL)
