def my_func(list_arg):
    for n in list_arg:
        if list_arg.count(n) == 1:
            yield n


original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Первый вариант решения:')
print(f'Исходный список: {original_list}')
result_list = []
for num in my_func(original_list):
    result_list.append(num)
print(f'Финальный список: {result_list}')

print('Второй вариант решения:')
print(f'Исходный список: {original_list}')
result_list = [n for n in original_list if original_list.count(n) == 1]
print(f'Финальный список: {result_list}')
