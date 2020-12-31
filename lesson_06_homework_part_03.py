class Worker:
    def __init__(self, name_arg, surname_arg, position_arg, wage_arg, bonus_arg):
        self.name = name_arg
        self.surname = surname_arg
        self.position = position_arg
        self._income = {'wage': wage_arg, 'bonus': bonus_arg}


class Position(Worker):
    def get_full_name(self):
        print(f'Работника зовут: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Общий доход работника составляет: {sum(self._income.values())}')


worker_01 = Position('John', 'Deer', 'Tractor driver', 100, 25)
print(worker_01.name)
print(worker_01.surname)
print(worker_01.position)
print(worker_01._income)  # Для чего мы делаем этот атрибут защищённым?
worker_01.get_full_name()
worker_01.get_total_income()
