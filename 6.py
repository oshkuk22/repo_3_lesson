# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word_str):
    return word_str.title()


word_ = input('Input word: ')
print(int_func(word_))

string_ = input('Input string: ')

for i in string_.split():
    print(int_func(i), end=' ')

print(f'\nUse map: {list(map(int_func, string_.split()))}'
      f'\nUse lambda: {list(map(lambda words_: words_.title(), string_.split()))}')

# branch dev 2
