#
# Task 6.
#


def int_func(word):
    return word.title()


input_word = input('Введите слово: ')
print(int_func(input_word))

input_str = input('Введите строку: ')
titled_words = map(int_func, input_str.split())
print(' '.join(titled_words))
