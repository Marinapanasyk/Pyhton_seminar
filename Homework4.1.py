#. Вычислить число c заданной точностью d
from decimal import *
import random
d=input("Введите необходимую точность:")
n = (random.uniform(-100,100))
print(n)
number = Decimal(n)
print(number.quantize(Decimal(f"{d}")))