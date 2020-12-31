class Road:
    _length = 0
    _width = 0

    def __init__(self, length_arg, width_arg):
        # Допустимо ли запрашивать данные через input?
        # self._length = input('Введите длину дороги')
        # self._width = input('Введите ширину дороги')
        # или это -- "дурной тон"?
        self._length = length_arg
        self._width = width_arg

    def asphalt_calculation(self):
        base_amount = 25  # Масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
        roadbed_thickness = 5  # Толщина дорожного полотна
        result = self._length * self._width * base_amount * roadbed_thickness / 1000
        print(f'{result} тонн')


a = Road(1000, 4)
b = Road(1200, 5)
a.asphalt_calculation()
b.asphalt_calculation()
