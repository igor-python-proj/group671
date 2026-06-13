# родительский класс, суперкласс
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"Машина модели {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color


# дочерний класс, ребенок, наследник, подкласс
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)  # обращение к родит методу
        self.number = number

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Автобус номер {self.number} едет в {destination}")


class Truck(Car):
    def change_color(self, new_color):
        self.color = new_color
        print(f"цвет грузовика изменен на {new_color}")


if __name__ == "__main__":
    # сработает только при прямом запуске модуля
    print("in car module")
    car_1 = Car("black", "BMW")
    print(car_1.color)
    print(car_1)

    # для чего __main__.py
    # какие есть паттерны организации файлов/кода в python
