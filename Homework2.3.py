#Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
N=int(input("Введите число:"))
L = list()
summ = 0
for i in range(1,N+1):
    L.append(round((1+1/N) ** N),2)
    N+=1
print(L)
print(sum(L))

