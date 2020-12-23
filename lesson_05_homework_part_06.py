with open('lesson_05_homework_part_06.txt', 'r', encoding='utf-8') as readable_file:
    result_dict = {}  # ??? Где его надо создавать до или в with?
    count_of_lines = sum(1 for line in readable_file)  # считает количество строк
    readable_file.seek(0)  # возвращает курсор в начало файла
    for count in range(count_of_lines):  # перебор строк
        line = readable_file.readline()  # возвращает содержимое очередной строки
        if not line.split(':')[0].count('\n'):  # отсекает пустые строки и строки со случайным значением
            key_word = line.split(':')[0]  # определение ключевого слова
            count_of_hours = 0
            for line_member in line.split(' '):  # разбивает строку на отдельные члены
                for el in line_member.split('('):  # отделяет численные значения от значений в скобках
                    if el.isdigit():  # проверка на целочисленность
                        count_of_hours += int(el)  # подсчёт часов
            result_dict.update({key_word: count_of_hours})  # запись данных в словарь
    print(f'Общее количество часов по каждому предмету: {result_dict}')  # ??? Где его надо создавать в with иди после?
