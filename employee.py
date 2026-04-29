class Employee():
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary
    def work(self):
        print("работа")

    def get_bonus(self):
        if self.__salary > 50000:
            return self.__salary // 10
        elif self.__salary > 100000:
            return self.__salary // 20
        else:
            return self.__salary
    
class Manager(Employee):
    def __init__(self):
        super().__init__()
    def work(self): # переопределение
        print("работа менеджера")
    # def work(self, var) - сокрытие
class Developer():
    def __init__(self):
        super().__init__()
    def work(self): # переопределение
        print("работа разработчика")
