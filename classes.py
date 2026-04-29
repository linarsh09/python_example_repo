# 3 вариант

class Car:
    def __init__(self, brand, model, year, speed, fuel):
	self.__brand = brand
	self.__model = model
	self.__year = year
	self.__speed = speed
	self.__fuel = fuel
    def get_brand(self):
	return self.__brand
    def set_brand(self, brand):
	self.__brand = brand
    def get_model(self):
	return self.__model
    def set_model(self, model):
	self.__model = model
    def get_year(self):
	return self.__year
    def set_year(self, year):
	self.__year = year
    def get_speed(self):
	return self.__speed
    def set_year(self, speed):
	self.__speed = speed
    def get_fuel(self):
	return self.__fuel
    def set_year(self, fuel):
	self.__speed = fuel
    def accelerate(self, amount):
	self.__speed += amount
    def brake(self, amount):
	self.__speed -= amount
    def get_info(self):
	return f"Car: {self.brand} {self.model} ({self.year}) - {self.speed} км/ч"
    def __str__(self):
	return self.get_info()
    def __mul__(self, n):
	if not isinstance(n, int):
	    return None
	return self.__speed * n
    def __sub__(self, other):
	if not isinstance(other, Car):
	    return None
	return self.__speed - other.get_speed()
    def __le__(self, other):
	if not isinstance(other, Car):
	    return None
	return self.__year <= other.get_year()
    def get_range(self):
	return "car range"
    def refuel(self):
	for i in range(self.__fuel, 101):
	    self.__fuel += i
	    print(f"заправка {self.fuel}%")

class ElectricCar(Car):
    def __init__(self, brand, model, year, speed, fuel, battery_level):
	super().__init__(brand, model, year, speed, fuel)
	self.__battery_level = battery_level
    def accelerate(self, amount):
	self.battery_level -= amount
    def charge(self, amount):
	self.__battery_level += amount
    def get_range(self):
	return "electric car range"
    def refuel(self):
	for i in range(self.__battery_level, 101):
	    self.__battery_level += i
	    print(f"заправка {self.__battery_level}%")
	