#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Так выглядел код раньше:
#def Summelement(SL):
        # s = 0
        # for i in range(len(SL)):
        #     if i % 2 != 0:
        #         s += SL[i]
        # print(f"Сумма равна: {s}")
from random import randint
def Summelement(SL):
    s= sum(SL[i] for i in range(1,len(SL),2))
    print(f"Сумма равна: {s}")
SL=[]
n =int(input("Введите количество элементов в списке:"))
for i in range (n):
    SL.append(randint(-10, 10))
print(SL)
Summelement(SL)
