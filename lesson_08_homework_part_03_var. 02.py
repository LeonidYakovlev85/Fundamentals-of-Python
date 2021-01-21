class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def input_validation(message):
    """Проверяет вводимое значение на принадлежность множеству рациональных чисел"""
    while True:
        try:
            input_value = input(message)
            checked_value = input_value[1:] if input_value[0] == '-' else input_value
            for el in checked_value.split('.'):
                if not el.isdigit() and input_value.lower() != 'stop':
                    raise OwnError('Вы ввели не число')
            return input_value
        except OwnError as err:
            print(err)


result_list = []
while True:
    element = input_validation('Введите число, для выхода из программы введите "stop": ')
    if element.lower() == 'stop':
        print(result_list)
        break
    result_list.append(element)
