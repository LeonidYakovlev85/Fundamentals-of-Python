# Так и не понял условие задачи.
# Для чего мы создаём отдельный класс, когда всё можно реализовать созданием функции?
# Что имеется в виду под проверкой порядка режимов? Ведь, как я понял, режим задан програмно и
# пользователь на него повлиять не может...

class TrafficLight:
    __color = None

    def running(self):
        from time import sleep, localtime
        from colorama import Fore
        # Правильно ли инициализировать списки в теле метода? Иначе они станут атрибутами класса, а это врядли нужно.
        traffic_light_colors = ['Red', 'Yellow', 'Green', 'Yellow']
        delay_time = [7, 2, 7, 2]
        letter_color = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.YELLOW]
        i = 0
        while True:
            # Как правильно ссылаться? TrafficLight.__color или self.__color?
            # (если писать TrafficLight.__color, то Пайчарм предлагает вынести функцию за пределы класса)
            if localtime().tm_hour > 6:  # Основной режим 06:00 -- 00:00
                self.__color = traffic_light_colors[i % 4]
                print(letter_color[i % 4] + self.__color)
                sleep(delay_time[i % 4])
                i += 1
            else:  # Дежурный режим 00:00 -- 06:00
                self.__color = traffic_light_colors[1]
                print(letter_color[1] + self.__color)
                sleep(1)


traffic_lights = TrafficLight()
# print(traffic_lights._TrafficLight__color)  # Не стал выводить на печать, так как значение атрибута -- None
traffic_lights.running()
