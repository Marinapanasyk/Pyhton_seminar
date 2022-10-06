#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
from random import randint, choice, uniform

def roots_equ(a, k, sign):

        with open("new.txt", "a", encoding="utf-8") as my_f:
            while k >= 1:
                my_f.write(f"({a}x ** {k})){sign}")
                k=k-1
                a = round(uniform(0, 10), 2)
                sign = choice('+-')
            my_f.write(f" {a}\n")
for i in range(3):
    SL = []
    SL.append(randint(1, 5))
    k = choice(SL)
    sign = choice('+-')
    a = round(uniform(0, 10), 2)
    print(a,k,sign)
    roots_equ(a,k,sign)