def word_input(prompt):
    """Заправшивает у пользователя слово из строчных латинских букв и проверяет ввод на соответствие условию

    Параметр prompt -- текстовое сообщение, выводимое пользователю
    Проверка реализована в два потока специально для проверки методов.
    Можно было всё сделать через ord()

    """
    while True:
        checked_word = input(prompt)
        if checked_word == '':
            print("Вы не ввели ни одного символа. Повторите ввод.")
            continue
        if ord(min(checked_word)) < 65 or 122 < ord(max(checked_word)):
            print("Слово содержит символы кроме латинских букв. Повторите ввод.")
            continue
        elif not checked_word.islower():
            print("Слово содержит прописные ('большие') буквы. Повторите ввод.")
            continue
        return checked_word


def int_func(convertible_word):
    """Возвращает слово с прописной буквы"""
    return convertible_word.title()


print("преобразование строки. Способ первый. Индусский")
source_string = []
while True:
    user_word = word_input('Введите слово из строчных ("маленьких") латинских букв или введите "qqq" для выхода: ')
    if user_word == 'qqq':
        break
    source_string.append(user_word)
source_string = ' '.join(source_string)
print(f'Строка из введённых Вами слов: {source_string}')
source_string = source_string.split()
for word in source_string[:]:
    source_string.remove(word)
    source_string.append(int_func(word))
source_string = ' '.join(source_string)
print(f'Строка из введённых Вами слов, начинающихся с заглавной буквы: {source_string}')

print("Преобразование строки. Способ второй. Короткий")
source_string = []
while True:
    user_word = word_input('Введите слово из строчных ("маленьких") латинских букв или введите "qqq" для выхода: ')
    if user_word == 'qqq':
        break
    source_string.append(int_func(user_word))
source_string = ' '.join(source_string)
print(f'Строка из введённых Вами слов, начинающихся с заглавной буквы: {source_string}')
