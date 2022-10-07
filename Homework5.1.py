# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
Text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {Text}")

def del_some_words(Text):
    Text = list(filter(lambda x: 'абв' not in x, Text.split()))
    return " ".join(Text)

txt = del_some_words(Text)
print(f"Новый текст:{Text}")