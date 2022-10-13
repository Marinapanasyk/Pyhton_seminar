# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
from random import randint
SL=[]
n =int(input("Введите количество элементов в списке:"))
for i in range (n):
    SL.append(randint(-10, 10))
print(SL)
result_list = [SL[i] for i in range (1, len(SL)) if SL[i] > SL[i - 1]]
print(result_list)
