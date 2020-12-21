def fact(arg):
    from functools import reduce

    for n_gen in range(1, arg + 1):
        yield n_gen
    yield reduce(lambda storage, n_fact: storage * n_fact, range(1, arg + 1))


n = int(input('Введите целое число: '))
for el in fact(n):
    if el == 1:
        print(f'{n}! = {el}', end='')
    elif el <= n:
        print(f' * {el}', end='')
    else:
        print(f' = {el}')
