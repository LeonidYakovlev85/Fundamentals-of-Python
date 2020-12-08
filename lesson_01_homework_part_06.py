a = float(input("Сколько километров Вы пробежали в первый день? "))
b = float(input("К какому результату Вы стремитесь? "))
day_number = 1
daily_result = a
while daily_result < b:
    day_number += 1
    daily_result *= 1.1
print(f'Вы достигните результата на {day_number}-й день')
