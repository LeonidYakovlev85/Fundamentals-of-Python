class Stationery:
    # В условиях задачи не прописано, как именно должен быть определён атрибут,
    # а как его использовать интересно (как Вы сказали сделать в конце урока) я не придумал.
    # Речь ведь не о перегрузке? Её я реализовал в четвёртой задаче )
    title = None

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Ручка рисует линии толщиной 0,5 или 0,7 мм. Их нельзя стереть.')


class Pencil(Stationery):
    def draw(self):
        print('Толщина линии, рисуемой карандашом, зависит от заточки. Её можно стереть с помощью ластика.')


class Handle(Stationery):
    def draw(self):
        print('Толщина линии, рисуемой маркером, зависит от приложения стерджня. Её нельзя стереть.')


def print_attr(object_arg):  # Я правильно понимаю, что в структуре кода функции располагаются после Классов?
    """Выводит на экран атрибуты объекта и их значения."""
    for attr in object_arg.__dict__:
        if not attr.startswith('_'):  # Отсекаем внутренние и служебные атрибуты
            print(f'{attr}: {object_arg.__dict__[attr]}')


pen_01 = Pen()
pencil_01 = Pencil()
handle_01 = Handle()
stationery_list = [pen_01, pencil_01, handle_01]
for el in stationery_list:
    print_attr(el)
    el.draw()
    print('*' * 50)
