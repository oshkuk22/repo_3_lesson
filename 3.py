# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


# first way


def sum_max_1(one, two, three):
    list_for_sort = [one, two, three]
    list_for_sort.sort(reverse=True)
    return sum(list_for_sort[:2])


print(f'Sum of the two maximal elements on list (first way) = {sum_max_1(4, 9, 5)}')


# second way


def sum_max_2(one, two, three):
    list_for_sort = [one, two, three]
    max_one = max(list_for_sort)
    list_for_sort.remove(max_one)
    max_two = max(list_for_sort)
    return max_one + max_two


print(f'Sum of the two maximal elements on list (second way) = {sum_max_2(3, 9, 4)}')

