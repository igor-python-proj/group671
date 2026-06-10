class Animal:
    def move(self):
        print("Животное двигается")

class Flying(Animal):
    def move(self):
        print("летает")

    def catch_meal(self):
        print("Ловит еду на лету")

class Swimming(Animal):
    def move(self):
        print("плавает")

class Duck(Flying, Swimming):
    def move(self):
        print("утка плавает и летает")

duck = Duck()
duck.move()
# MRO - method resolution order - порядок поиска метода
print(Duck.mro())
duck.catch_meal()
print(Flying.mro())