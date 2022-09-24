#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number=input("Введите число:")
number = str(number)
x = (len(number))
number = float(number)
number = number * (10 ** x)
summ_number = 0
while number > 0:
    summ_number +=  number %10
    number //=10
print(summ_number)
