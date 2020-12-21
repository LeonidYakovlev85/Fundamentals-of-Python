from itertools import count, cycle

for el in count(3):
    if el > 10:
        print('')
        break
    print(el, end=' ')

flag = 1
for el in cycle([1, 2, 3]):
    if flag > 15:
        print('')
        break
    print(el, end=' ')
    flag += 1

for el in cycle(n for n in count(3) if n <= 10):
    print(el, end=' ')  # не могу понять, почему перебор через cycle происходит только один раз
