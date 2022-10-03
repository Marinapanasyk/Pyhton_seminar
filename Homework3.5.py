#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input('Введите число: '))

def Fibonacci(n):
    fibo_line = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_line.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_line.insert(0, a)
        a, b = b, a - b
    return fibo_line
print(Fibonacci(n))

