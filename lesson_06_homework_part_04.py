class Car:
    def __init__(self, speed_arg, color_arg, name_arg, is_police_arg):
        self.name = name_arg
        self.color = color_arg
        self.speed = speed_arg
        self.is_police = is_police_arg

    def go(self):
        print(f'{self.name} started moving')

    def stop(self):
        print(f'{self.name} stopped moving')

    def turn(self):
        from random import randint
        directions_list = ['left', 'right']
        print(f'{self.name} turned {directions_list[randint(0, len(directions_list) - 1)]}')

    def show_speed(self):
        from random import randint
        print(f'{self.name} moves with speed {randint(0, self.speed)}')


class TownCar(Car):
    def __init__(self, name_arg, color_arg, speed_arg=120, is_police_arg=False):
        super().__init__(speed_arg, color_arg, name_arg, is_police_arg)

    def show_speed(self):
        from random import randint
        car_speed = randint(5, self.speed)
        if car_speed < 60:
            print(f'{self.name} moves with speed {car_speed}')
        else:
            print(f'Attention! {self.name} moves with excess speed -- {car_speed}!')


class SportCar(Car):
    def __init__(self, name_arg, color_arg, speed_arg=240, is_police_arg=False):
        super().__init__(speed_arg, color_arg, name_arg, is_police_arg)


class WorkCar(Car):
    def __init__(self, name_arg, color_arg='Orange', speed_arg=90, is_police_arg=False):
        super().__init__(speed_arg, color_arg, name_arg, is_police_arg)

    def show_speed(self):
        from random import randint
        car_speed = randint(5, self.speed)
        if car_speed < 40:
            print(f'{self.name} moves with speed {car_speed}')
        else:
            print(f'Attention! {self.name} moves with excess speed -- {car_speed}!')


class PoliceCar(Car):
    def __init__(self, name_arg, color_arg='White and Blue', speed_arg=180, is_police_arg=True):
        super().__init__(speed_arg, color_arg, name_arg, is_police_arg)


def print_attr(object_arg):  # Я правильно понимаю, что в структуре кода функции располагаются после Классов?
    """Выводит на экран атрибуты объекта и их значения."""
    for attr in object_arg.__dict__:
        if not attr.startswith('_'):  # Если не внутренний и не служебный
            print(f'{attr}: {object_arg.__dict__[attr]}')


town_car_01 = TownCar('Daewoo Matiz', 'Cherry color', 90)
town_car_02 = TownCar('Hyundai Solaris', 'White')
sport_car_01 = SportCar('Mazda Miata', 'Hot red color')
work_car_01 = WorkCar('MAN')
police_car_01 = PoliceCar('Patrol 66')
car_list = [town_car_01, town_car_02, sport_car_01, work_car_01, police_car_01]
for car in car_list:
    print_attr(car)
    car.go()
    car.turn()
    car.show_speed()
    car.stop()
    print('*' * 50)
