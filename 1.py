# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
# -*- coding: utf-8 -*-

flag = True


def division_func(dividend, divider):
    try:
        print(f'Rezult of the division {dividend}/{divider} = {(dividend / divider):.3f}')
    except ZeroDivisionError:
        print("Error. Division by zero")


while flag:
    try:
        one_number = float(input('Input the first number:'))
        flag = False
    except ValueError:
        print('Entered value is not a number!!!')

flag = True

while flag:
    try:
        two_number = float(input('Input the second number:'))
        flag = False
    except ValueError:
        print('Entered value is not a number!!!')

division_func(one_number, two_number)
