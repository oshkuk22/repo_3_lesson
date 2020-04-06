# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

sum_cache = 0
flag = True

def sum_seq(seq):
    sum_list = 0
    flag_sum_seq = True
    for i in seq:
        try:
            element_list = int(i)
            sum_list = sum_list + element_list
        except ValueError:
            if i.upper() == 'X':
                flag_sum_seq = False
                break
            else:
                continue
    return sum_list, flag_sum_seq


while flag:
    numbers = input('Exit - X\nInput a sequence of numbers separated by a space:')
    numbers = numbers.split()
    sum_, flag = sum_seq(seq=numbers)
    sum_cache = sum_cache + sum_
    print(f'Sum of the input sequence = {sum_cache}')





