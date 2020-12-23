with open('lesson_05_homework_part_07.txt', 'r', encoding='utf-8') as readable_file:
    print('Исходные данные:')
    for i, el in enumerate(readable_file, 1):
        print(f'{i}) {el}', end='')
    readable_file.seek(0)  # возвращает курсор в начало файла
    result_dict = {}  # ??? Где его надо создавать до или в with?
    count_profitable = 0
    total_profit = 0
    count_of_lines = sum(1 for line in readable_file)  # считает количество строк
    readable_file.seek(0)  # возвращает курсор в начало файла
    for count in range(count_of_lines):  # перебор строк
        line = readable_file.readline()  # возвращает содержимое очередной строки
        line = line.replace('\n', '')  # отсекает \n от последнего числа
        line = line.split(' ')  # разбивает строку на части
        if sum(int(el) for el in line if el.isdigit()) > 0:  # отсекает пустые и случайные строки
            firm_name = f'{line[-3]} {" ".join(line[0:-3])}'  # определение названия фирмы
            firm_profit = int(line[-2]) - int(line[-1])  # определение прибыли фирмы
            result_dict.update({firm_name: firm_profit})  # запись данных в итоговый словарь
            if firm_profit >= 0:  # учёт фирм, сработавших без убытков
                count_profitable += 1
                total_profit += firm_profit
    average_profit = total_profit / count_profitable  # расчёт средней прибыли
    result_dict.update({'average_profit': average_profit})  # запись средней прибыли в итоговый словарь
    print(f'\n{"*" * 154}\nОтчёт по фирмам: {result_dict}')  # ??? Где его надо создавать в with иди после?
