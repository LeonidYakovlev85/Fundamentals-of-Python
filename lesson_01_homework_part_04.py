number = int(input("Введите целое положительное число: "))
max_digit = 0
while number != 0:
    verified_digit = number % 10
    if verified_digit > max_digit:
        max_digit = verified_digit
    number = number // 10
print(f'Самая большая цифра в введённом Вами числе: {max_digit}')
