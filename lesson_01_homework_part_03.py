number = int(input("Введите целое число от 1 до 9: "))
while number == 0 or number > 9:
    number = int(input("Вы ввели некорректное число, попробуйте ещё раз: "))
n_1 = number
n_2 = int(f'{number}{number}')
n_3 = int(f'{number}{number}{number}')
result = n_1 + n_2 + n_3
print(result)
