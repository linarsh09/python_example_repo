class animal
 def __init__(self, name, age, species, weight, diet, leep):
     super().__init__(name, age "собака")
        self.__name = name
        self.__age = age
        self.__species = species
        self.__weight = weight
        self.__diet = diet  # список продуктов
#геттеры
    def get_name(self):
        return self.__name 

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_weight(self):
        return self.__weight

    def get_diet(self):
        return self.__diet
#сеттеры
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_species(self, species):
        self.__species = species

    def set_weight(self, weight):
        self.__weight = weight

    def set_diet(self, diet):
        self.__diet = diet

 #методы
    def eat(self):
        return f"{self.__name} ест обычную еду."

    def sleep(self):
        return f"{self.__name} спит."

    def get_description(self):
        return f"{self.__name}, {self.__species}, возраст: {self.__age}, вес: {self.__weight}"

    def is_adult(self):
        return self.__age >= 1

    def get_diet_info(self):
        result = "Диета: "
        for food in self.__diet:
            result += food + " "
        return result

    def make_sound(self):
        return "Животное издает звук"
#перегрузки
    def __str__(self):
        return f"{self.__name} ({self.__species}), возраст: {self.__age}, вес: {self.__weight}"

    def __add__(self, other):
        return self.__age + other.__age

    def __lt__(self, other):
        return self.__weight < other.__weight

    def __contains__(self, item):
        for food in self.__diet:
            if food == item:
                return True
        return False

class Dog(Animal):
    def __init__(self, name, age, weight, diet, breed):
        super().__init__(name, age, "Собака", weight, diet)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

#переопределения
    def eat(self):
        return f"{self.get_name()} (собака) ест корм."

    def bark(self):
        return f"{self.get_name()} лает!"

    def make_sound(self):
        return "Гав-гав!"

    def get_diet_info(self):
        result = "Собачья диета: "
        for food in self.get_diet():
            result += food + " "
        return result




   

       



