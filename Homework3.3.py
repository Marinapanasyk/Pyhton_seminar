#Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform
def Different(SL):
    mylist=[]
    for i in SL:
            mylist.append(round(i%1,5))
    print(mylist)
    print(f"разница между максимальным и минимальным значением дробной части элементов: {max(mylist) - min(mylist)}")
SL=[]
n =int(input("Введите количество элементов в списке:"))
for i in range (n):
    SL.append(uniform(-10, 10))
print(SL)
Different(SL)

