# 4 variant

class Employee():
    def__init__(self, name, employee_id, position, salary, work_hours):
        self.__name = name
        self.__employee_id = employee_id
        self.__position = position
        self.__salary = salary
        self.__work_hours = work_hours
        
        
        def get_name(self):
            return self.__name
        def set_name(self, name):
            return name
            
        def get_employee_id(self):
            return self.__employee_id
        def set_employee_id(self, id):
            return id
           
        def get_position(self):
            return self.__position
        def set_position(self, position)
            return position
            
        def get_salary(self):
            return self.__salary
        def set_salary(self, salary):
            return salary
            
        def get_work_hours(self):
            return self.__work_hours
        def set_work_hours(self, work_hours):
            return work_hours
            
        def give_raise(self, amount):
            self.__salary += 
            
        def get_total_hours():
            sum = self.__work_hours
            return sum
            
        def display_info():
            return 
            
class Manager(Employee):
    def__init__(self, name, employee_id, position, salary, work_hours, team_size):
        super().__init(name, employee_id, position, salary, work_hours, team_size):
            self.__team_size = team_size
            def get_bonus(self):
                if self.__team_size >= 10:
                    bonus = 10%
                if self.__team_size>=20:
                    bonus = 20%
            def give_raise(self):
                self._salary = self.__salary + self.__salary * bonus
                
        
        
