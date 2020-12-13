user_list = [input("Введите элемент списка: ")]
while True:
    user_answer = input(f'Ваш список: {user_list};\nВведите новый элемент или нажмите Enter для звершения ввода: ')
    if user_answer == '':
        break
    user_list.append(user_answer)
user_list_copy = user_list.copy()

print(f'\nДлинное решение:')
print(f'Исходный список: {user_list}')
for i in range(len(user_list) - 1):
    if i % 2 == 0:
        odd_element = user_list.pop(i)
        even_element = user_list.pop(i)
        user_list.insert(i, odd_element)
        user_list.insert(i, even_element)
print(f'Итоговый список: {user_list}')

print(f'\nКороткое решение:')
print(f'Исходный список: {user_list_copy}')
for i in range(len(user_list_copy) - 1):
    if i % 2 == 0:
        user_list_copy[i], user_list_copy[i + 1] = user_list_copy[i + 1], user_list_copy[i]
print(f'Итоговый список: {user_list_copy}')
