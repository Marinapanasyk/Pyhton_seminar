#Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

# text = [random.choice(string.ascii_lowercase + string.digits if i != 10 else string.ascii_uppercase) for i in range(3)]
# print('  '.join(text))
# text1 = [random.choice(text if i != 5 else text) for i in range(3)]
# print('  '.join(text1))
# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
from random import randint

length = int(input('Задайте длину строки: '))
s = list(range(length))

print(f'"Начальный список" {s}')

for i in range(length):
    ran = randint(0, length-1)
    s[i], s[ran] = s[ran], s[i]

print(f'"Перемешаный список" {s}')


