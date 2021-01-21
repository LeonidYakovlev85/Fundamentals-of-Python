class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    inventory = {}
    seq_num = 0

    @classmethod
    def get_warehouse_dict(cls):
        if cls.inventory == {}:
            print('Склад пуст')
        else:
            print('В наличии на складе:')
            for key, value in cls.inventory.items():
                print(key)
                for i_key, i_value in value.items():
                    print(f'\tНомер хранения {i_key}. {i_value}')

    @classmethod
    def receipt(cls, device):
        key = device.__class__.__name__
        value = [device.name, device.param]
        if key in cls.inventory.keys():
            cls.seq_num += 1
            cls.inventory[key][cls.seq_num] = value
        else:
            cls.seq_num += 1
            cls.inventory[key] = {cls.seq_num: value}
        print(f'Принято на склад: {value}; номер хранения -- {cls.seq_num}')

    @classmethod
    def delivery(cls, storage_number):
        stock_availability = ''
        material = ''
        for key, value in cls.inventory.items():
            if storage_number in value.keys():
                stock_availability = 'in stock'
                material = value[storage_number]
                del value[storage_number]
                if cls.inventory[key] == {}:
                    del cls.inventory[key]
                break
        if stock_availability == 'in stock':
            print(f'Выдано в работу: {material}')
        else:
            print('Оборудования с таким номером хранения на складе нет')


class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, param):
        super().__init__(name)
        while True:
            try:
                if param == 'b/w' or param == 'color':
                    self.param = param
                    break
                else:
                    raise OwnError('Принтер может быть только цветным (color) или черно-белым (b/w)')
            except OwnError as err:
                print(err)
            param = input('Введите корректное значение: ')


class Scanner(OfficeEquipment):
    def __init__(self, name, param):
        super().__init__(name)
        while True:
            try:
                if param == '600dpi' or param == '1200dpi':
                    self.param = param
                    break
                else:
                    raise OwnError('Сканер может иметь только разрешение 600dpi или 1200dpi')
            except OwnError as err:
                print(err)
            param = input('Введите корректное значение: ')


class Xerox(OfficeEquipment):
    def __init__(self, name, param):
        super().__init__(name)
        while True:
            try:
                if param == 'A4' or param == 'A3':
                    self.param = param
                    break
                else:
                    raise OwnError('Копировальный аппарат может иметь максимальный размер A4 или A3 (!: A - латинская)')
            except OwnError as err:
                print(err)
            param = input('Введите корректное значение: ')


printer_01 = Printer('printer_01', 'b/w')
printer_02 = Printer('printer_02', 'color')
scanner_01 = Scanner('scanner_01', '600dpi')
scanner_02 = Scanner('scanner_02', '1200dpi')
xerox_01 = Xerox('xerox_01', 'A4')
xerox_02 = Xerox('xerox_01', 'A3')
Warehouse.get_warehouse_dict()
Warehouse.receipt(printer_01)
Warehouse.receipt(printer_02)
Warehouse.receipt(scanner_01)
Warehouse.receipt(scanner_02)
Warehouse.receipt(xerox_01)
Warehouse.receipt(xerox_02)
Warehouse.get_warehouse_dict()
Warehouse.delivery(3)
Warehouse.delivery(4)
Warehouse.delivery(13)
Warehouse.get_warehouse_dict()
Warehouse.receipt(Printer('printer_03', 'b/w'))
Warehouse.receipt(Printer('printer_04', 'incorrect value'))
Warehouse.receipt(Scanner('scanner_03', 'incorrect value'))
Warehouse.receipt(Xerox('xerox_03', 'incorrect value'))
