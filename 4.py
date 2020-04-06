# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение
# в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.


def step_multiply_1(base, step):
    return base ** step


def step_multiply_2(base, step):
    result_2 = 1

    for i in range(abs(step)):
        result_2 = result_2 * base

    if step > 0:
        return result_2
    elif step == 0:
        return 1
    else:
        return 1 / result_2


base = 6
step = -5

print(f'{base} to the power of {step} using the operator ** =  {step_multiply_1(base=base, step=step)}')
print(f'{base} to the power of {step} using the cycle =  {step_multiply_2(base=base, step=step)}')

