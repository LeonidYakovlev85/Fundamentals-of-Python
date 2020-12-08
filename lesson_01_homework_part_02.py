time = int(input("Введите время в секундах: "))
while time > 86400:
    time = int(input("Вы ввели слишком большое число, попробуйте заново: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time - hours * 3600 - minutes * 60
print(f'Введённое Вами время в формате "чч:мм:сс" - {hours:02}:{minutes:02}:{seconds:02}')
