class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_list(list_arg):
    """Удаляет из списка последний элемент, если он не принадлежит множеству рациональных чисел"""
    try:
        last_element = list_arg[-1][1:] if list_arg[-1][0] == '-' else list_arg[-1]
        for el in last_element.split('.'):
            if not el.isdigit():
                raise OwnError('Вы ввели не число')
    except OwnError as err:
        print(err)
        list_arg.pop()


result_list = []
while True:
    element = input('Введите число, для выхода из программы введите "stop": ')
    if element.lower() == 'stop':
        print(result_list)
        break
    result_list.append(element)
    check_list(result_list)
