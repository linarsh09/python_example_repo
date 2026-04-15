class Car:
    def __init__(self, brand:str, model:str, speed:int):
        self.__brand = brand
        self.__model = model
        self.__speed = speed

    def accelerate(self, speed):
        self.__speed += speed

    def brake(self, speed):
        self.__speed -= speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed
car = Car("BMW", "M5", 280)
car.accelerate(120)
print(car.get_speed())
car.brake(60)
print(car.get_speed())
car.set_speed(90)
print(car.get_speed())