from functools import reduce

result = reduce(lambda storage, number: storage * number, [n for n in range(100, 1001) if n % 2 == 0])
print(result)
