from math import *

from Log_text import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Добро пожаловать в программу калькулятор\n Выберите действие, которое вам необходимо выполнить и два числа через пробел\n '
                              'Введите номер операции- \n "1" - Сложение +\n"2" - Вычитание -\n "3" - Умножение *\n"4" - Деление / \n"0" - Возврат в главное меню')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')

def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')

def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} / {y} = {x // y}')

def ret_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    return update.message.reply_text(f'Добро пожаловать в программу калькулятор\n Выберите действие, которое вам необходимо выполнить и два числа через пробел\n '
                              'Введите номер операции- \n "1" - Сложение +\n"2" - Вычитание -\n "3" - Умножение *\n"4" - Деление / \n"0" - Возврат в главное меню')

