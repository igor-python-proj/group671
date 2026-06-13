class Animal:
    def move(self):
        print("--- move in Animal ---")
        print("Животное двигается")


class Flying(Animal):
    def move(self):
        print("--- move in Flying ---")
        super().move()
        print("летает")
        print("--- end move in Flying ---")

    def catch_meal(self):
        print("Ловит еду на лету")


class Swimming(Animal):
    def move(self):
        print("--- move in Swimming ---")
        print("плавает")
        print("--- end move in Swimming ---")


class Duck(Flying, Swimming):
    def move(self):
        print("--- move in Duck ---")
        super().move()
        print("утка плавает и летает")
        print("--- end move in Duck ---")


duck = Duck()
duck.move()
print("-- MRO --")
# MRO - method resolution order - порядок поиска метода
print(Duck.mro())
duck.catch_meal()
print(Flying.mro())
Flying().move()