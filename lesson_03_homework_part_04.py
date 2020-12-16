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


def checking_integer(prompt):
    """Проверяет вводимое пользователем значение на принадлежность множеству целых чисел

    Параметры:
    prompt -- текстовое сообщение, выводимое пользователю

    """
    while True:
        a = input(prompt)
        try:
            return int(a)
        except ValueError:
            print("Введённое значение не является целым числом. Повторите ввод.")


def my_func(x, y):
    """возводит x в степень y

    округляет результат до 5 знаков после заяптой

    """
    print("Способ первый, с помощью оператора **:")
    answer = x ** y
    print(round(answer, 5))
    print("Способ второй, без оператора **, предусматривающая использование цикла:")
    denominator = 1
    for i in range(abs(y)):
        denominator *= x
    answer = 1 / denominator
    print(round(answer, 5))


while True:
    user_x = checking_input("Введите действительное положительное число: ")
    if user_x > 0:
        break
    print("Число должно быть положительным. Повторите ввод: ")

while True:
    user_y = checking_integer("Введите целое отрицательное число: ")
    if user_y < 0:
        break
    print("Введённое значение не является отрицательным числом. Повторите ввод.")

my_func(user_x, user_y)
