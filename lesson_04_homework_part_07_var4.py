def fact(arg):
    from functools import reduce

    for n_gen in range(1, arg + 1):
        if n_gen == 1:
            print(f'{arg}! = {n_gen}', end='')
        else:
            print(f' * {n_gen}', end='')
    yield f' = {reduce(lambda storage, n_fact: storage * n_fact, range(1, arg + 1))}'


n = int(input('Введите целое число: '))
for el in fact(n):
    print(el)
