# 8 variant YasminaTuk
class Person:
    def __init__(self, name, birth_year, email, contacts):
        self.name = name
        self.birth_year = birth_year
        self.email = email
        self.list_contacts = [contacts]

    def get_age(self):
        return 2026-int(self.birth_year)
    
    def is_adult(self):
        if self.get_age() >= 18:
            return print("Vzrosliy")
        return print("Malenkiy")
    
    def add_contact(self, contact):
        if contact not in self.list_contacts:
            self.list_contacts.append(contact)
    
    def list_all_contacts(self):
        print(self.list_contacts)

    def str(self):
        print(f"person:{self.name} ({self.get_age()})")
    
    def len(self):
        print(len(self.list_contacts))

    
class Doctor(Person):
    def __init__(self, name, birth_year, email, contacts, specialization, patients):
        super().__init__(name, birth_year, email, contacts)
        self.specialization = specialization
        self.patients = patients

    def is_adult(self):
        if self.get_age() >= 25:
            return print("Vzrosliy")
        return print("Malenkiy")
    
    def get_qualification(self, qual):
        print(f"qualificazia: {qual}")
    
    def get_profession(self, prof):
        print(f"professia: {prof}")

    def list_all_contacts(self):
        print(f"zvonite, pishite, {self.list_contacts}, vash vrach {self.name} ({self.specialization})")

    def call(self):
        print("prinimaet patienta")


    def iter(self):
        for i in self.patients:
            print(i)

    def len(self):
        print(len(self.patients))
    

    

P1 = Person("anna", 2009, "123@.com", "+7777777")
D1 = Doctor("alim", 2001, "1234567@344", "+345678", "pediatr", ['alidar', 'amir', 'anna'])
print(P1.get_age())
print(P1.is_adult())
print(P1.add_contact('asdfgh'))
print(P1.list_all_contacts())
print(D1.is_adult())
print(D1.get_qualification("vrach"))
print(D1.get_profession("superVrach"))
print(D1.list_all_contacts())
print(D1.iter())
print(D1.len())
print(D1.call())
print(D1.str())