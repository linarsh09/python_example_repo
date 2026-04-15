class Car:
    def __init__(self, brand, model, speed=0):
        self.__brand = brand
        self.__model = model
        self.__speed = speed

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Скорость не может быть отрицательной!")

    def accelerate(self, value):
        if value > 0:
            self.__speed += value
        else:
            print("Ускорение должно быть положительным числом!")

    def brake(self, value):
        if value > 0:
            self.__speed = max(0, self.__speed - value)
        else:
            print("Торможение должно быть положительным числом!")

    def info(self):
        print(f" {self.__brand}  {self.__model}  {self.__speed} км/ч")


car = Car("", 54)

car.info()
car.accelerate(230)
print("", car.get_speed(), "км/ч")

car.brake(300)
print(car.get_speed(), "км/ч")