# Используется библиотека Free Google Translate API for Python версии 3.1.0-alpha
from googletrans import Translator

with open('lesson_05_homework_part_04_01.txt', 'r', encoding='utf-8') as readable_file:
    original_word_list = [line.split()[0] for line in readable_file]
    readable_file.seek(0)
    data_list = [line.split()[1:] for line in readable_file]

translated_word_list = []
for word in original_word_list:
    translated_word = Translator().translate(word, src='en', dest='ru')
    translated_word_list.append(translated_word.text)
# Мне кажется, что "развёрнутая" запись в данном случае лучше однострочной:
# translated_word_list = [Translator().translate(word, src='en', dest='ru').text for word in original_word_list]

with open('lesson_05_homework_part_04_02.txt', 'w', encoding='utf-8') as recordable_file:
    for i in range(len(translated_word_list)):
        result_stroke = f'{translated_word_list[i]} {" ".join(data_list[i])}'
        recordable_file.write(f'{result_stroke}\n')
print('Перевод выполнен. Данные записаны в файл lesson_05_homework_part_04_02.txt')
