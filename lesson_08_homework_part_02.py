class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_01 = input('Введите первое число: ')
num_02 = input('Введите второе число: ')
try:
    num_01 = int(num_01)
    num_02 = int(num_02)
    if num_02 == 0:
        raise OwnError('Вы собираетесь делить на ноль')
except ValueError:
    print('Среди введённых данных присустствует не число')
except OwnError as err:
    print(err)
else:
    print(num_01 / num_02)
