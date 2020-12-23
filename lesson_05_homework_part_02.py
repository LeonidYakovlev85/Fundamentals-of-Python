readable_file = open('lesson_05_homework_part_02.txt', 'r', encoding='utf-8')
lines_list = readable_file.readlines()
print(f'Количество строк в файле: {len(lines_list):>8}\n{"*" * 34}')
for i, line in enumerate(lines_list, 1):
    prefix = 'Количество слов в строке №'
    print(f'{prefix} {i}: {len(line.split()):>4}') if i < 10 else print(f'{prefix} {i}: {len(line.split()):>3}')
readable_file.close()
