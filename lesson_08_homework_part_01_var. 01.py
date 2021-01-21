class Date:
    def __init__(self, date_arg):
        self.date = date_arg

    @classmethod
    def extraction(cls, obj):
        cls.date = obj.date
        # ввёл атрибут класса, что бы как-то обосновать введение метода с декоратором @classmethod
        print(f'Исходные данные: {cls.date} {type(cls.date)}')
        print('Преобразованные данные: ')
        for el in cls.date.split('-'):
            el = int(el)
            print(el, type(el))

    @staticmethod
    def validation(obj):
        year = obj.date.split('-')[2]
        month = obj.date.split('-')[1]
        day = obj.date.split('-')[0]
        dm_dictionary = {31: ['01', '03', '05', '07', '08', '10', '12'],
                         30: ['04', '06', '09', '11'],
                         28: ['02']}
        dm_dictionary_leap = {31: ['01', '03', '05', '07', '08', '10', '12'],
                              30: ['04', '06', '09', '11'],
                              29: ['02']}
        number_of_days = dm_dictionary_leap if int(year) % 4 == 0 else dm_dictionary
        if len(year) == 4 and int(year) >= 0:  # принимаем только положительные значения
            print('год введён корректно')
        else:
            print('год введён некорректно')
        if len(month) == 2 and 0 <= int(month) <= 12:
            print('месяц введён корректно')
        else:
            print('месяц введён некорректно')
        if len(day) == 2:
            day_value = None
            for key, values in number_of_days.items():
                if month in values and 0 < int(day) <= key:
                    day_value = True
                    break
            print('день введён корректно') if day_value else print('день введён некорректно')
        else:
            print('день введён некорректно')


a = Date('21-01-2021')
Date.extraction(a)
Date.validation(a)
