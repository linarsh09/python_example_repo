class Animal()
    def __init__(self, name, age, species, weight, diet)
        self.__name = name
        self.__age = age
        self.__species = species
        self.__weight = weight
	self.__diet = diet
    def get_eat(self):
	    return self.__eat
    def get_sleep(self):
	    return self
    def get_age(self):
	    return self._age
    def  is_adult(self):
        return self.get_age()>20
    def get_diet_info(self):
            return print('diet')
    def get_description(self):
            return self.description
a = Animal('Жора', 120, 'млекопитающее', 300,['колбаса, капуста, молоко']
print(a)
class Dog(Animal)
    super().__init__(self, name, age, species, weight, diet, breed)
        self.__breed = breed
    def get_breed(self):
            return print('вабалабадабдаб')