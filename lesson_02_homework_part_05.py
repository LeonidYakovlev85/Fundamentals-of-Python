default_list = [7, 5, 3, 3, 2]
print(f'Имеется рейтинг - не возрастающий набор натуральных чисел: {default_list}')
while True:
    user_number = input("Введите новый элемент рейтинга или нажмите Enter для завершения программы: ")
    if user_number == '':
        break
    else:
        user_number = int(user_number)
        if user_number in default_list:
            entry_index = default_list.index(user_number)
            default_list.insert(entry_index, user_number)
        elif user_number < default_list[-1]:
            default_list.append(user_number)
        else:
            for index, element in enumerate(default_list):
                if user_number > element:
                    default_list.insert(index, user_number)
                    break
        print(f'Обновлённый рейтинг: {default_list}')
