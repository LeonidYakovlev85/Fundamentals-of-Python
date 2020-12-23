new_file = open('lesson_05_homework_part_01.txt', 'w', encoding='utf-8')
while True:
    user_data = input('Введите данные (для выхода из программы просто нажмите Enter без ввода): ')
    if user_data == '':
        break
    new_file.writelines([user_data, '\n'])
new_file.close()
print('Ваши данные записаны в файл lesson_05_homework_part_01.txt')
