def my_func(list_arg):
    for i, n in enumerate(list_arg):
        if i > 1 and n > list_arg[i - 1]:
            yield n


original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Первый вариант решения:')
print(f'Исходный список: {original_list}')
result_list = []
for num in my_func(original_list):
    result_list.append(num)
print(f'Финальный список: {result_list}')

print('Второй вариант решения:')
print(f'Исходный список: {original_list}')
result_list = [n for i, n in enumerate(original_list) if i > 1 and n > original_list[i - 1]]
print(f'Финальный список: {result_list}')
