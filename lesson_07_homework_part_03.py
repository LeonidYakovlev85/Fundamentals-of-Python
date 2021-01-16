class Cell:
    def __init__(self, cells_number):
        self.cells_number = cells_number

    # Не понимаю что значит "Данные методы должны применяться только к клеткам",
    # разве переопределённые методы и так, без каких-либо условий,
    # не работают только с экземплярами того класса, для которого их переопределили?

    # Также из текста задания я понял, что с помощью перегрузки мы должны получчать не просто числа,
    # а "клетки", т. е. объекты класса Cell.

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        if self.cells_number - other.cells_number > 0:
            return Cell(self.cells_number - other.cells_number)
        else:
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        if self.cells_number // other.cells_number >= 1:
            return Cell(self.cells_number // other.cells_number)
        else:
            return Cell(0)

    def make_order(self, row_length):
        if self.cells_number == 0:
            return 'пустая строка'
        elif self.cells_number % row_length == 0:
            a = f'{"*" * row_length}\n' * (self.cells_number // row_length - 1)
            b = "*" * row_length
        else:
            a = f'{"*" * row_length}\n' * (self.cells_number // row_length)
            b = '*' * (self.cells_number % row_length)
        return f'{a}{b}'


cell_01 = Cell(5)
cell_02 = Cell(2)
cell_03 = cell_01 + cell_02
print(cell_03.cells_number)
print(cell_03.make_order(5))
cell_03 = cell_01 - cell_02
print(cell_03.cells_number)
print(cell_03.make_order(5))
cell_03 = cell_01 * cell_02
print(cell_03.cells_number)
print(cell_03.make_order(5))
cell_03 = cell_01 / cell_02
print(cell_03.cells_number)
print(cell_03.make_order(5))
