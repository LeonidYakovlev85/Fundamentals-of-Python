def gen(arg_gen):
    for n_gen in range(1, arg_gen + 1):
        yield n_gen


def fact(arg_fact):
    from functools import reduce

    return reduce(lambda storage, n_fact: storage * n_fact, range(1, arg_fact + 1))


n = int(input('Введите целое число: '))
for el in gen(n):
    print(f'{n}! = {el}*', end='') if el == 1 else print(f'{el}*', end='') if el != n else print(f'{el} = ', fact(n))
