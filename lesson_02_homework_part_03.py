user_answer = int(input(f'Введите номер месяца (целое число от 1 до 12: '))

print(f'\nРешение через Списки (вариант 1):')
winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
print("Выбранный Вами месяц относится к зиме") if user_answer in winter_list else None
print("Выбранный Вами месяц относится к весне") if user_answer in spring_list else None
print("Выбранный Вами месяц относится к лету") if user_answer in summer_list else None
print("Выбранный Вами месяц относится к осени") if user_answer in autumn_list else None

print(f'\nРешение через Списки (вариант 2):')
winter_list = [1, 2, 12, 'зиме']
spring_list = [3, 4, 5, 'весне']
summer_list = [6, 7, 8, 'лету']
autumn_list = [9, 10, 11, 'осени']
months_list = winter_list + spring_list + summer_list + autumn_list
list_pos = months_list.index(user_answer)
modulo = list_pos % 4
print(f'Выбранный Вами месяц относится к {months_list[list_pos + 3 - modulo]}')

print(f'\nРешение через Словари:')
months_dict = {(1, 2, 12): 'зиме', (3, 4, 5): 'весне', (6, 7, 8): 'лету', (9, 10, 11): 'осени'}
months_list = list(months_dict.keys())
for i in range(len(months_list)):
    if user_answer in months_list[i]:
        print(f'Выбранный Вами месяц относится к {months_dict.get(months_list[i])}')
        break
