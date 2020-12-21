def salary_calculation():
    from sys import argv

    try:
        try:
            script_name, hours, rate, prize = argv
            print(f'Решение № 1\n'
                  f'Заработная плата сотрудника составляет: {(int(hours) * int(rate)) + int(prize)}')
            # или можно решить так:
            argv = [int(n) for n in argv[1:]]
            print(f'Решение № 2\n'
                  f'Заработная плата сотрудника составляет: {argv[0] * argv[1] + argv[2]}')
        except ValueError:
            print('Допустимы только целочисленные значения. Повторите ввод. \n'
                  'Введите данные через пробел в следующем порядке: \n'
                  '<выработка в часах> <ставка в час> <премия>')
    except ValueError:
        print('Вы не ввели данные, либо ввели их не полностью. \n'
              'Введите данные через пробел в следующем порядке: \n'
              '<выработка в часах> <ставка в час> <премия>')


salary_calculation()
