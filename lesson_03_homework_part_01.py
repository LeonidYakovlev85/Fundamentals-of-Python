def checking_input(prompt):
    """Проверяет вводимое пользователем значение на принадлежность множеству рациональных чисел

    Параметр prompt -- текстовое сообщение, выводимое пользователю
    Возвращает int или float значение аргумента, если аргумент рациональное число.
    Инициирует повторный ввод, если аргумент любой другой символ / набор символов.

    """
    while True:д
        a = input(prompt)
        try:
            return int(a)
        except ValueError:
            try:
                return float(a)
            except ValueError:
                print("Введённое значение не является числом. Повторите ввод.")


def division(number_1, number_2):
    """Выводит на экран результат деления аргументов, округлённый до 5 знаков после запятой"""
    try:
        print(round(number_1 / number_2, 5))
    except ZeroDivisionError:
        print("Вы попытались выполнить деление на ноль")


user_answer_1 = checking_input("Введите первое число: ")
user_answer_2 = checking_input("Введите второе число: ")
division(user_answer_1, user_answer_2)
