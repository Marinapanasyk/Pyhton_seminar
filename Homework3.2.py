#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint, choice

def Multlement(SL):
    mult=[]
    n = len(SL)-1
    a = 0
    if n % 2 != 0:
        l = n // 2 + 1
    else: l=n // 2
    for i in range(l):
        mult.append((SL[a]) * (SL[n]))
        a=a+1
        n=n-1
    print(mult)
SL = []
n = int(input("Введите количество элементов в списке:"))
for i in range(n):
    SL.append(randint(-10, 10))
print(SL)
Multlement(SL)
