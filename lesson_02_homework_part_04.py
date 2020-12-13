user_stroke = input("Введите строку из нескольких слов, разделённых пробелами: ")
print("Введённая Вами строка состоит из следующих элементов:")
work_list = user_stroke.split()
for i, element in enumerate(work_list):
    print(f'{i + 1}) {element[:10]}')
