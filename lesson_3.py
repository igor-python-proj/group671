class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False
        self.__max_speed = 0

    def _calculate_fuel(self):
        print(self._fined)
        return 0

    def __test(self):
        print(self.__max_speed)

    def drive_to(self, destination):
        print("max speed:", self.__max_speed)
        print(f"Машина модели {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.__test()
        self.color = new_color

    # геттер
    def get_max_speed(self):
        return self.__max_speed

    # сеттер
    def set_max_speed(self, new_max_speed):
        if new_max_speed <= 0 or new_max_speed > 250:
            raise ValueError("Max speed is nonrealistic")
        self.__max_speed = new_max_speed

    @property
    def max_speed(self):
        # геттер
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed):
        print("new max spedd в сеттере", new_max_speed)
        if new_max_speed <= 0 or new_max_speed > 250:
            raise ValueError("Max speed is nonrealistic")
        self.__max_speed = new_max_speed

car_1 = Car("black", "BMW")
print(car_1.color)
print("Max speed of a car", car_1.get_max_speed())
# car_1.set_max_speed(-200) # вызовет ошибку
car_1.set_max_speed(200)
print("Max speed of a car", car_1.max_speed)
car_1.max_speed = 198
print("Max speed of a car", car_1.max_speed)
car_1.drive_to("Каракол")
car_1.change_color("blue")
# car_1.color = "blue"
print(car_1.color)
car_1.model = "Subaru"
print("Car ids fined:", car_1._fined)
car_1._fined = True
car_1._calculate_fuel()
# print(car_1.__max_speed) # Ошибка - обращение к приватному атрибуту
print(car_1._Car__max_speed) # такое можно только для быстрого теста
car_1.__max_speed = 20 # не настоящий __max_speed из класса Car
car_1.drive_to("Bishkek")