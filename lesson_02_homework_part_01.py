my_list = [10, 2.5, 'Some text', True, False, ['el_1', 'el_2'], ('el_1', 'el_2'), {'key_1': 10, 'key_2': 20}, '\n']

print(f'Решение № 1: вывод только типа элемента, без указания порядкового номера')
for element in my_list:
    print(f'Элемент списка {element}, его тип - {type(element)}')

print(f'\nРешение № 2.1: вывод и типа элемента и порядкового номера (без использования "enumerate")')
for i in range(len(my_list)):
    print(f'Элемент списка №{i + 1}: {my_list[i]}, его тип - {type(my_list[i])}')

print(f'\nРешение № 2.2: вывод и типа элемента и порядкового номера (с помощью "enumerate")')
for i, element in enumerate(my_list):
    print(f'Элемент списка №{i + 1}: {element}, его тип - {type(element)}')
