def coding(txt):
    with open('text_words.txt', 'w') as data:
        data.write(s)
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    with open('text_code_words.txt', 'r') as data:
        my_text = data.read()
    with open('text_code_words.txt', 'w') as data:
        data.write(txt)
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

# with open('text_code_words.txt', 'r') as data:
#     my_text = data.read()
s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
