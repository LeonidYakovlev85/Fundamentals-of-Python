def checking_input(prompt):
    """Проверяет вводимое пользователем значение на принадлежность множеству рациональных чисел

    Параметр prompt -- текстовое сообщение, выводимое пользователю
    Возвращает int или float значение аргумента, если аргумент рациональное число.
    Инициирует повторный ввод, если аргумент любой другой символ / набор символов.

    """
    while True:
        a = input(prompt)
        try:
            return int(a)
        except ValueError:
            try:
                return float(a)
            except ValueError:
                print("Введённое значение не является числом. Повторите ввод.")


def my_func(number_1, number_2, number_3):
    """Возвращает сумму наибольших двух аргументов"""
    return sum([number_1, number_2, number_3]) - min([number_1, number_2, number_3])


user_answer_1 = checking_input("Введите первое число: ")
user_answer_2 = checking_input("Введите второе число: ")
user_answer_3 = checking_input("Введите третье число: ")
print(my_func(user_answer_1, user_answer_2, user_answer_3))
