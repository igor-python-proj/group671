from abc import ABC, abstractmethod


# PEP-8
# абстрактный класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        pass


# конкретные классы
class Dog(Animal):
    def make_sound(self):
        print("гав-гав")

    def test(self):
        print("test in dog")


class Cat(Animal):
    def make_sound(self):
        print("мяу")


puppy = Dog()
puppy.make_sound()
