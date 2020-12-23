with open('lesson_05_homework_part_03.txt', 'r', encoding='utf-8') as readable_file:
    low_salaried_employees = []
    total_salary = 0
    employees_number = 0
    print('Данные по всем сотрудникам (фамилия / оклад):')
    for el in readable_file.readlines():
        surname = el.split()[0]
        salary = el.split()[1]
        print(f'{surname:<15}{salary}')
        salary = salary.replace(',', '.')
        salary = float(salary)
        total_salary += salary
        employees_number += 1
        if salary < 20000:
            low_salaried_employees.append(surname)
    if low_salaried_employees:
        print(f'{"*" * 37}\nСотрудники с окладом меньше 20000,00:')
        for i, el in enumerate(low_salaried_employees, 1):
            print(f'{i}) {el}')
    print(f'{"*" * 34}\nСредний оклад составляет: {total_salary / employees_number:.2f}')
