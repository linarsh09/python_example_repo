class car:
    def __init__(self,brand:str,model:str,speed:int):
        self.__brand = brand
        self.__model = model
        self.__speed = speed
    def accelerate(self,speed):
        self.__speed = speed
    def brake(self,speed):
        self.__speed -=speed
    def get_speed(self):
        return self.__speed
    def set_speed(self,speed):
        self.__speed=speed
car=car("Toyota","Supra",300)

car.accelerate(300)
print(car.get_speed())

car.brake(150)
print(car.get_speed())

car.set_speed(200)
print(car.get_speed())

        