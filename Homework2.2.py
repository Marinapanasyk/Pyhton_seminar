#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# N=int(input("Введите число:"))
# s = list(range(1, N+1))
# print(s)
# factorial = 1
# for i in (s):
#     factorial *= i
# print(factorial)


N=int(input("Введите число:"))
f = 1
while N>1:
    f *= N
    N -= 1
print (f)

