def checking_input(prompt):
    """Проверяет вводимое пользователем значение на принадлежность множеству вещественных чисел

    Параметр prompt -- текстовое сообщение, выводимое пользователю
    Возвращает пустое значение, если введено пустое значение.
    Возвращает значение аргумента, если аргумент может быть преобразован в вещественное число.
    Инициирует повторный ввод, если аргумент любой другой символ / набор символов.

    """
    while True:
        a = input(prompt)
        if a == '':
            return a
        try:
            float(a)
            return a
        except ValueError:
            print("Введённое значение не является числом. Повторите ввод.")


with open('lesson_05_homework_part_05.txt', 'w', encoding='utf-8') as recordable_file:
    while True:
        user_input = checking_input('Введите число (для выхода из программы просто нажмите Enter без ввода): ')
        if user_input == '':
            break
        recordable_file.writelines([user_input, ' '])
print('Ваши числа записаны в файл lesson_05_homework_part_05.txt')

with open('lesson_05_homework_part_05.txt', 'r', encoding='utf-8') as readable_file:
    number_list = readable_file.read().split(' ')

result = 0
for num in number_list:
    if num != '':
        result += float(num)
print(f'Сумма введённых Вами чисел равна: {result}')
