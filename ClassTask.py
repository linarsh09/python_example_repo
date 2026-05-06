class Animal():
    def __init__(self, name, age, species, weight, diet):
        self.__name = name
        self.__age = age
        self.__species = species
        self.__weight = weight
	    self.__diet = diet
    def eat(self):
	    return print('Животное ест')
    def get_weight(self):
        return self.__weight
    def sleep(self):
	    return print('сон')
    def get_age(self):
	    return self.__age
    def  is_adult(self):
        return self.get_age()>20
    def get_diet_info(self):
            for i in diet:
                print(i)
    def get_description(self):
        return print('chenibud')
    def set_age(self, age):
        self.__age = age
    def set_name(self, name):
        self.__name = name
    def set_species(self, species):
        self.__species = species
    def set_weight(self, weight):
        self.__weight = weight
    def set_diet(self, diet):
        self.__diet = diet
    def make_sound(self):
        return print('Издаваемый звук')
    def __str__(self):
        return f"Animal: {self.__name} имя {self.__age} возраст {self.__species} вид {self,__weight} вес {self.__diet} диета"
    def __add__(self, other):
        if(isinstance(other, Animal)):
            return self.__age + other.__age
    def __lt__(self, other):
        if(isinstance(other, Animal)):
            return self.get_weight() < other.get__weight()
    def __contains__(self, index):
        for i in self.__diet:
            if i == index:
                return True
        return False
a = Animal('Жора', 120, 'млекопитающее', 300,['колбаса, капуста, молоко'])
print(a.get_age())
a.set_age(50)
print(a.get_age())
class Dog(Animal):
    def __init__(self, name, age, species, weight, diet, breed):
        super().__init__(name, age, species, weight, diet)
        self.__breed = breed
    def bark(self):
            return print('лай')
    def eat(self):
	    return print('собака ест')
    def make_sound(self):
        return self.bark()
    def get_diet_info(self):
            for i in diet:
                print('собака', i)