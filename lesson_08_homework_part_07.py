class ComplexNumber:
    def __init__(self, value_arg):
        value_list = value_arg.split()
        self.x = int(value_list[0])
        if value_list[-1] == 'i':
            y = 1
        else:
            y = int(value_list[-1][0:-1])
        self.y = y if value_list[1] != '-' else -1 * y

    def __mul__(self, other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        if x1 * y2 + y1 * x2 > 0:
            result = f'{x1 * x2 - y1 * y2} + {x1 * y2 + y1 * x2}i'
        else:
            result = f'{x1 * x2 - y1 * y2} - {-1 * (x1 * y2 + y1 * x2)}i'
        return result


a = ComplexNumber('3 + i')
b = ComplexNumber('2 - 3i')
print(a * b)
