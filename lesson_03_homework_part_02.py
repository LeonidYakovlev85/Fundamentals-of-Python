def user_data(name, surname, age, city, email, phone_number):
    """Выводит на экран данные пользователя в одну строку

    Пояснение:
    Имеется в виду в одну строку с точки зрения компьютера.
    Если я правильно понял, то \n - просто делает разрыв строки, но не создаёт новой

    """
    print(f'\n'
          f'Здравствуйте! Вы - {name} {surname}.\n'
          f'Город, в котором Вы живёте, - {city}. \n'
          f'Скорее всего Вы родились в {2020 - int(age)}-м году. \n'
          f'Ваш электронный адрес: {email}. \n'
          f'Номер Вашего телефона - {phone_number}.'
          )


user_surname = input("Введите Вашу фамилию: ")
user_name = input("Введите Ваше имя: ")
user_age = input("Сколько вам полных лет? ")
user_city = input("В каком городе Вы живёте? ")
user_email = input("Какой у Вас электронный адрес? ")
user_phone_number = input("И последнее: напишите номер Вашего телефона: ")
user_data(
    email=user_email, age=user_age,
    phone_number=user_phone_number, surname=user_surname,
    name=user_name, city=user_city
)
