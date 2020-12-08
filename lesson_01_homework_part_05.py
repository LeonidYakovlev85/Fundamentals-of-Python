proceeds = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
if proceeds > costs:
    print("Фирма сработала с прибылью")
    number_of_employees = int(input("Укажите численность сотрудников фирмы: "))
    profit = proceeds - costs
    profitability = profit / proceeds
    profit_per_employee = profit / number_of_employees
    print(f'Прибыль составила: {profit}')
    print(f'Рентабельность выручки: {profitability}')
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_per_employee}')
elif proceeds < costs:
    print("Фирма сработала с убытком")
else:
    print("Фирма сработала в ноль")
